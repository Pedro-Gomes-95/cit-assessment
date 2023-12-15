# cit-assessment

This repository is meant for the CIT technical challenge.

It has the following structure:

```
|-- data                      The folder containing the original dataset as well as the train and test sets.
|  |-- automobile.zip         The zip file with the original dataset.
|  |-- imports-85.data        The original data.
|  |-- imports-85.names       Details on the dataset. 
|  |-- train.csv              The training data (the target variable is included).
|  |-- test.csv               The test data (the target variable is included).
|-- model
|  |-- pipeline.pkl           The best performing model.
|-- utils
|  |-- utils.py               File with auxiliary functions for plotting.
|-- assignment.ipynb          The Jupyter notebook containing the analysis.
|-- presentation.pdf          The PowerPoint presentation.
