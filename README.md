# toothbrushing-dataset

This repository contains the dataset to accompany TODO:

GIT Large File Support (git-lfs) must be installed to use the data. See https://docs.github.com/en/github/managing-large-files/installing-git-large-file-storage for installation instructions.

The datasets are located in the data folder. Each subfolder represents a single brusing session. The folder naming convention is as follows:

S{subject}-S{session}-{gender}-{hand}-{position}-{age}-{brush}-{location}-{sensor}

subject: id of subject (1-16)

session: is of session for subject (1-5)

gender: subjects gender (M or F)

hand: subject is right or left handed (R or L)

age: subject age

location: id of location (1-5)

sensor: accelerometer or gyroscope (A or G)

Within each folder are 4 csv files containing the sensor data. The naming convention follows the parent folder convention. For labelled experiments an additional labels.json file is included contains the start and end timestamps for each activity and the activity name.
