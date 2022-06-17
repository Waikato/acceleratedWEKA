#!/usr/bin/env bash
set -o pipefail

WEKA_EXE="$CONDA_PREFIX"/bin/weka

create_launch_file_linux() {
  cp "$PREFIX"/bin/weka "$WEKA_EXE"
}

echo "Begin post-link.sh"

python "$PREFIX"/bin/accelerated-weka-post-install.py

test -d "$CONDA_PREFIX"/pkgs/weka || exit 1

mkdir -p "$CONDA_PREFIX"/bin
mkdir -p "$CONDA_PREFIX"/lib
mkdir -p "$CONDA_PREFIX"/include

shopt -s nullglob

create_launch_file_linux

"$WEKA_EXE" -main weka.core.WekaPackageManager -refresh-cache &> /dev/null

"$WEKA_EXE" -main weka.core.WekaPackageManager -uninstall-package wekaPython &> /dev/null
"$WEKA_EXE" -main weka.core.WekaPackageManager -uninstall-package wekaDeeplearning4j &> /dev/null
"$WEKA_EXE" -main weka.core.WekaPackageManager -uninstall-package netlibNativeLinux &> /dev/null
"$WEKA_EXE" -main weka.core.WekaPackageManager -uninstall-package wekaRAPIDS &> /dev/null

"$WEKA_EXE" -main weka.core.WekaPackageManager -install-package wekaPython &> /dev/null
"$WEKA_EXE" -main weka.core.WekaPackageManager -install-package wekaDeeplearning4j &> /dev/null
"$WEKA_EXE" -main weka.core.WekaPackageManager -install-package netlibNativeLinux &> /dev/null
"$WEKA_EXE" -main weka.core.WekaPackageManager -install-package wekaRAPIDS &> /dev/null

shopt -u nullglob
