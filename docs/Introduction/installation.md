# Installation

Accelerated WEKA was designed to provide an easy installation process. It can be done via the conda work with Python 3.8 and above. Installation can be done via `pip`:
Accelerated WEKA simplifies the installation process by using the [conda environment](https://docs.conda.io/en/latest/), making straightforward to use it from the beginning. Once you have conda installed, Accelerated WEKA can be installed by issuing the following command:

```sh
conda create -n accelweka -c rapidsai -c nvidia -c conda-forge  -c waikato weka
```

Conda will take care of the configuration of dependencies, and after finishing the installation, you can start using Accelerated WEKA immediately by activating the newly created environment.
```sh
conda activate accelweka
```

And finally, launching WEKA GUI
```sh
weka
```

Alternatively, you can run stuff from the command line:

```sh
weka -main weka.Run .RandomRBF -n 100000 -a 500 > RBFa500n100k.arff
weka -memory 48g -main weka.Run weka.classifiers.rapids.CuMLClassifier -split-percentage 80 -learner RandomForestClassifier -t $(pwd)/RBFa5kn1k.arff -py-command python
```

Or Programatically through Java.

Feel welcome to [open an issue on GitHub](https://github.com/Waikato/acceleratedWEKA/issues/new) if you are having any trouble.