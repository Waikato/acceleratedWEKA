#!/usr/bin/env python3

import glob
import json
import os
import shutil
import subprocess
import sys
import platform
import urllib.parse as urlparse
from pathlib import Path
from contextlib import contextmanager
from tempfile import TemporaryDirectory as tempdir
from distutils.dir_util import copy_tree


class Extractor(object):
    """Extractor base class, platform specific extractors should inherit
    from this class.
    """

    def __init__(self, weka_config):
        self.weka_name = weka_config["name"]
        self.weka_version = weka_config["version"]
        self.base_url = weka_config["base_url"]
        self.patch_url_text = weka_config["patch_url_ext"]
        self.weka_blob = weka_config["blob"]
        self.conda_prefix = os.environ.get("CONDA_PREFIX")
        self.prefix = os.environ["PREFIX"]
        self.src_dir = Path(self.conda_prefix) / "pkgs" / "weka"
        self.blob_dir = Path(self.conda_prefix) / "pkgs" / self.weka_name
        os.makedirs(self.blob_dir, exist_ok=True)

    def download(self, url, target_full_path):
        cmd = ["wget", url, "-O", target_full_path, "-q"]
        try:
            subprocess.check_call(cmd)
        except subprocess.CalledProcessError as exc:
            raise exc

    def download_blobs(self):
        """Downloads the binary blobs to the $BLOB_DIR
        """
        dl_url = urlparse.urljoin(self.base_url, self.weka_blob)
        dl_path = os.path.join(self.blob_dir, self.weka_blob)

        if os.path.isfile(dl_path):
            print("re-using previously downloaded %s" % (dl_path))
        else:
            print("downloading %s to %s" % (dl_url, dl_path))
        self.download(dl_url, dl_path)

    def extract(self, *args):
        raise NotImplementedError("%s.extract(..)" % (type(self).__name__))

    def copy_files(self, source, destination, ignore=None):
        dest = Path(destination)
        if dest.exists() and dest.is_dir():
            shutil.rmtree(dest, ignore_errors=True)
        elif dest.exists() and dest.is_file():
            dest.unlink()

        shutil.copytree(source, destination, symlinks=True, ignore=ignore, ignore_dangling_symlinks=True)


class LinuxExtractor(Extractor):
    """The Linux Extractor
    """

    def extract(self):
        # For better error messages
        if os.path.exists("/tmp/weka-installer.log"):
            try:
                os.remove("/tmp/weka-installer.log")
            except OSError as e:
                raise RuntimeError(
                    "Failed to remove /tmp/weka-installer.log") from e

        print("Extracting on Linux")
        runfile = self.blob_dir / self.weka_blob
        os.chmod(runfile, 0o777)

        with tempdir() as tmpdir:
            cmd = [
                "unzip",
                str(runfile),
                "-d",
                tmpdir
            ]
            subprocess.run(cmd, env=os.environ.copy(), check=True)
            if os.path.exists("/tmp/weka-installer.log"):
                os.remove("/tmp/weka-installer.log")
            weka_path = Path(tmpdir) / f'weka-{self.weka_version.replace(".", "-")}'

            if not os.path.isdir(weka_path):
                print('STATUS:', status)
                for fn in glob.glob('/tmp/weka_install_*.log'):
                    f = open(fn, 'r')
                    print('-'*100, fn)
                    print(f.read())
                    print('-'*100)
                    f.close()
                raise RuntimeError(
                    'Something went wrong in executing `{}`: directory `{}` does not exist'
                    .format(' '.join(cmd), weka_path))

            self.copy_files(weka_path, self.src_dir)
        os.remove(runfile)


def check_platform():
    plt = sys.platform
    if plt.startswith("linux") or plt.startswith("win"):
        return
    else:
        raise RuntimeError("Unsupported platform: %s" % (plt))


def set_config():
    """Set necessary configurations"""

    weka = {}
    prefix = Path(os.environ["PREFIX"])
    extra_args = dict()
    with open(prefix / "bin" / "accelerated-weka-extra-args.json", "r") as f:
        extra_args = json.loads(f.read())

    weka["version"] = os.environ["PKG_VERSION"]
    weka["name"] = os.environ["PKG_NAME"]
    weka["buildnum"] = os.environ["PKG_BUILDNUM"]
    weka["version_build"] = extra_args["version_build"]
    weka["release"] = extra_args["release"]

    url_download = os.environ.get(
        "PROXY_DEV_DOWNLOAD_WEKA", "https://sourceforge.net/projects/weka/files/"
    )
    url_prod_ext = f'weka-{weka["release"].replace(".", "-")}/{weka["version"]}/'
    weka["base_url"] = urlparse.urljoin(url_download, url_prod_ext)
    weka["patch_url_ext"] = f""

    if sys.platform.startswith("win"):
        weka["blob"] = f'weka-{weka["version"].replace(".", "-")}-azul-zulu-windows.exe'
    else:
        weka["blob"] = f'weka-{weka["version"].replace(".", "-")}-azul-zulu-linux.zip'

    return weka


def _main():

    print("Running Post installation")

    os.environ['DISPLAY'] = ''

    acc_weka_config = set_config()

    # get an extractor
    check_platform()
    extractor = LinuxExtractor(acc_weka_config)

    # download binaries
    extractor.download_blobs()

    # Extract
    extractor.extract()


if __name__ == "__main__":
    _main()
