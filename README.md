# Toothbrushing Dataset

## Description

This repository contains the dataset to accompany the paper Dataset: Tooth Brushing Monitoring using A Smart Toothbrush. Data from 57 toothbrushing sessions recording using two devices - wrist worn and attached to the brush. The device has a 3D acceleromter and gyroscope.

GIT Large File Support (git-lfs) must be installed to use the data. See https://docs.github.com/en/github/managing-large-files/installing-git-large-file-storage for installation instructions.

## Getting Started

We recommend using python 3.x and start with the [this](/src/example-1.ipynb) notebook. The data files are stored using `git-lfs` which needs to be installed separately. Please consult you platform git documentation in order to enable `git-lfs`.

The datasets are located in the data folder. Each subfolder represents a single brushing session. The folder naming convention is as follows:

## Detailed Documentation

Each experiment is contained in a separate folder under [this](/data). The folders and files within the folder have the following naming convention:

```
S{subject}-S{session}-{gender}-{hand}-{position}-{age}-{brush}-{location}-{sensor}

where:
  subject: id of subject (1-16)
  session: is of session for subject (1-5)
  gender: subjects gender (M or F)
  hand: subject is right or left handed (R or L)
  age: subject age
  location: id of location (1-5)
  sensor: accelerometer or gyroscope (A or G)
```

Within each folder are 4 csv files containing the sensor data. The naming convention follows the parent folder convention. For labelled experiments an additional labels.json file is included contains the start and end timestamps for each activity and the activity name.
