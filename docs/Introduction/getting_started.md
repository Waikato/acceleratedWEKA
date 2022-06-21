## Running a quick example with the GUI


## Running a quick example with the command line

To run a quick example with the command line there are two easy steps.

1. First, let's create a small dataset just to get the hang of how to use Accelerated WEKA (except the new learner classes, it is the same as using standard WEKA):
```sh
weka -main weka.Run .RandomRBF -n 10000 -a 50 > RBFa50n10k.arff
```

2. Let's go through the arguments of the above command:  
    - **weka** is the main program, if you are using this command alone it launches the GUI. If you insert other arguments it can run tasks from the terminal.
    - **-main weka.Run** indicates that we want to run the class *weka.Run*. In other words, we want to run straight from the command line, as opposed to the default *weka.gui.GUIChooser* that launches the GUI.
    - **.RandomRBF** is the class that we want to use. This is a relative reference for the generator class that creates datasets with a Radial function.
    - **-n 10000** is one of the possible arguments for the *RandomRBF* class, it indicates that we want a dataset with ten thousand instances.
    - **-a 50** is another one of the *RandomRBF* arguments, it sets the number of attributes on the dataset to 50.
    - **>> RBFa50n10k.arff** is the bash *append operator* followed by the *file name* that we want to write to.

3. Then, let's use the newly created dataset to run some of the new RAPIDS algorithms using the GPU.
```sh
 weka -memory 48g -main weka.Run weka.classifiers.rapids.CuMLClassifier -split-percentage 80 -learner RandomForestClassifier -t $(pwd)/RBFa5kn10k.arff -py-command python
```

4. Again, let's go through the arguments of the above command:
    - **-memory 48g** sets the JVM maximum heap to 48 gigabytes.
    - **weka.classifiers.rapids.CuMLClassifier** is the class responsible for integrating RAPIDS to WEKA.
    - **-split-percentage 80** means that we want to split the dataset into two smaller ones. We should train with 80% of the dataset and test with the remaining 20%.
    - **-learner RandomForestClassifier** indicates which RAPIDS classifier/regressor we want to use in our experiment.
    - **-t $(pwd)/RBFa5kn10k.arff** sets the previously created dataset as the input for our experiment.
    - **-py-command python** is an optional command just to make sure we are using the correct python command and to modify the python call in case we need to.

5. After the code is run, you will get the result. Check accuracy and time taken.

6. Now, let's run another RAPIDS learner with the same dataset. This time, try using the Support Vector classifier (SVC):
```sh
weka -memory 48g -main weka.Run weka.classifiers.rapids.CuMLClassifier -split-percentage 80 -learner SVC -t $(pwd)/RBFa5kn10k.arff -py-command python
```

7. Notice the only difference is the argument of the **-learner** option.

8. Compare the results with the RandomForestClassifier.

9. Feel free to explore the other supported learners from RAPIDS. You can find a comprehensive list of them in [Features]().