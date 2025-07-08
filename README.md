<p align="center">
     <img src="./docs/img/acc_weka_logo.jpg" width="500">
</p>

# acceleratedWEKA - easy GPU support using WEKA

<!-- [![GitHub release](https://img.shields.io/github/release/Waikato/acceleratedWEKA.svg)](https://GitHub.com/Waikato/acceleratedWEKA/releases/) -->
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)
<!-- [![Build Status](https://travis-ci.com/Waikato/acceleratedWEKA.svg?branch=master)](https://travis-ci.com/Waikato/acceleratedWEKA) -->
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Waikato/acceleratedWEKA/issues)

<!-- AcceleratedWEKA is the automation process to install and use popular WEKA packages that provide GPU-accelerated algorithms. Some of these packages require several configuration steps that might constitute a barrier for those users that are not well versed in configuring systems.
AcceleratedWEKA uses the Conda environment to install and configure the software and environment required to fully leverage the GPU-accelerated algorithms from the aforementioned packages.  -->

Accelerated WEKA unifies the [WEKA software](https://ml.cms.waikato.ac.nz/weka/), a well-known and open-source Java software, with new technologies that leverage the GPU to shorten the execution time of ML algorithms.
It has two benefits aimed at users without expertise in system configuration and coding: an easy installation and a GUI that guides the configuration and execution of the ML tasks.
Accelerated WEKA is a collection of packages available for WEKA (e.g., [WDL4J](https://deeplearning.cms.waikato.ac.nz), [wekaPython](https://weka.sourceforge.io/packageMetaData/wekaPython/index.html), and [wekaRAPIDS](https://github.com/Waikato/wekaRAPIDS)). Accelerated WEKA can be easiy installed and anyone can extend it to support new tools and algorithms.


## Installing acceleratedWEKA

Accelerated WEKA was designed to provide an easy installation process.
Accelerated WEKA simplifies the installation process by using the [conda environment](https://docs.conda.io/en/latest/). This makes straightforward to use Accelerated WEKA from the beginning. Once you have conda installed, Accelerated WEKA can be installed by issuing the following two commands: 

#### Creating the conda environment
```bash
$ conda create --solver=libmamba -n accelweka -c rapidsai -c conda-forge -c nvidia -c waikato weka
```

#### Activating the conda environment
```bash
$ conda activate accelweka
```

Conda takes care of the configuration of dependencies. This means the required libraries will be installed and automatically configured. You do not need to go through any manual setup.

After finishing the installation and activation steps, you can start using Accelerated WEKA immediately by launching the WEKA GUI:
```bash
$ weka
```

The WEKA package is located in:
```
/path/to/conda/env/pkgs/weka
```

## Using acceleratedWEKA
As most of Weka, AcceleratedWEKA's functionality is accessible in two ways:

- Using the Weka workbench GUI
<!-- - Programming with Weka in Java -->
- Via the commandline interface

Both ways are explained in the [getting-started](https://waikato.github.io/acceleratedWEKA/user_guide/getting_started/) documentation. 

A simple example that creates a dataset and runs a Support Vector Machine with it would look like the following:
```bash
$ weka -main weka.Run .RandomRBF -n 10000 -a 5000 > RBFa5kn10k.arff

$ weka -memory 12g -main weka.Run weka.classifiers.rapids.CuMLClassifier -split-percentage 80 -learner SVC -t $(pwd)/RBFa5kn10k.arff -py-command python
```



which results in:

```
Options: -learner SVC -py-command python 

=== Classifier model (full training set) ===

SVC()

Time taken to build model: 24.93 seconds

Time taken to test model on training data: 13.3 seconds

=== Error on training data ===

Correctly Classified Instances       10000              100      %
Incorrectly Classified Instances         0                0      %
Kappa statistic                          1     
Mean absolute error                      0     
Root mean squared error                  0     
Relative absolute error                  0      %
Root relative squared error              0      %
Total Number of Instances            10000     


=== Detailed Accuracy By Class ===

                 TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
                 1.000    0.000    1.000      1.000    1.000      1.000    1.000     1.000     c0
                 1.000    0.000    1.000      1.000    1.000      1.000    1.000     1.000     c1
Weighted Avg.    1.000    0.000    1.000      1.000    1.000      1.000    1.000     1.000     


=== Confusion Matrix ===

    a    b   <-- classified as
 5185    0 |    a = c0
    0 4815 |    b = c1

Time taken to test model on test split: 1.13 seconds

=== Error on test split ===

Correctly Classified Instances        2000              100      %
Incorrectly Classified Instances         0                0      %
Kappa statistic                          1     
Mean absolute error                      0     
Root mean squared error                  0     
Relative absolute error                  0      %
Root relative squared error              0      %
Total Number of Instances             2000     


=== Detailed Accuracy By Class ===

                 TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
                 1.000    0.000    1.000      1.000    1.000      1.000    1.000     1.000     c0
                 1.000    0.000    1.000      1.000    1.000      1.000    1.000     1.000     c1
Weighted Avg.    1.000    0.000    1.000      1.000    1.000      1.000    1.000     1.000     


=== Confusion Matrix ===

    a    b   <-- classified as
 1041    0 |    a = c0
    0  959 |    b = c1
```

## Documentation
The full documentation, giving installation instructions and getting started guides, is available at [https://waikato.github.io/acceleratedWEKA/](https://waikato.github.io/acceleratedWEKA/).


## Citation

Please cite the following paper if using this package in an academic publication:

Cassales, G. W., Liu, J. J., & Bifet, A. (2025). Accelerated Weka: GPU Machine Learning with Weka Workbench. Neurocomputing, 646, 130432. https://doi.org/10.1016/j.neucom.2025.130432

BibTex:

```
@article{CASSALES2025130432,
title = {Accelerated Weka: GPU Machine Learning with Weka Workbench},
journal = {Neurocomputing},
volume = {646},
pages = {130432},
year = {2025},
issn = {0925-2312},
doi = {https://doi.org/10.1016/j.neucom.2025.130432},
url = {https://www.sciencedirect.com/science/article/pii/S092523122501104X},
author = {Guilherme Weigert Cassales and Justin Jia Liu and Albert Bifet},
keywords = {GPU, Machine learning software, Classification, Ensemble methods, Open-source software},
}
```


## Related projects
- [WEKA](https://www.cs.waikato.ac.nz/ml/weka/)
- [wekaPython](http://markahall.blogspot.co.nz/2015/06/cpython-integration-in-weka.html)
- [wekaDeeplearning4j](https://deeplearning.cms.waikato.ac.nz/)
- [wekaRAPIDS](https://github.com/Waikato/wekaRAPIDS)



## Misc.
Original code by Justin Liu
