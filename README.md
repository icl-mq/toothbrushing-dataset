# Toothbrushing Dataset

## Description

This repository contains the dataset to accompany the paper ``Dataset: Toothbrushing Data and Analysis of its Potential Use in
Human Activity Recognition Applications``. Data from 62 toothbrushing sessions recording using two devices - wrist worn and attached to the brush. The device has a 3D accelerometer and gyroscope.

## Getting Started

We recommend using python 3.6 and start with the [/src/example-1.ipynb](/src/example-1.ipynb) notebook. This notebook contains a step by step guide on how to run an analysis on the dataset including how to load the files, perform basic preprocessing, graphs and fitting a simple classifier.

The data files are stored using `git-lfs` which needs to be installed separately. Please consult https://docs.github.com/en/github/managing-large-files/installing-git-large-file-storage in order to enable `git-lfs` on your platform.

The datasets are located in the data folder. Each subfolder represents a single brushing session. The folder naming convention includes metadata as follows:

## Experiment Metadata

Each experiment is contained in a separate folder under [/data](/data). The folders and files within the folder have the following naming convention:

```
S{subject}-S{session}-{gender}-{hand}-{sensor-location}-{age}-{brush}-{location}-{sensor}

where:
  subject: id of subject (1--17)
  session: is of session for subject (1--5)
  gender: subjects gender (M or F)
  hand: subject is right or left handed (R or L)
  sensor-location: device location, attached to brush or on wrist (A or W)
  age: subject age
  brush: electric or manual (E or M)
  location: id of location (1-5)
    1: North Facing (Washroom 1 Building 1)
    2: West Facing (Washroom 2 Building 2)
    3: North Facing (Washroom 3 Building 3)
    4: East Facing (Washroom 4 Building 2)
    5: North Facing (Washroom 5 Building 2)
  sensor: accelerometer or gyroscope (A or G)
```

Within each folder are 4 csv files containing the sensor data. The naming convention follows the parent folder convention. For labelled experiments an additional labels.json file is included contains the start and end timestamps for each activity and the activity name.

## Unlabelled Activities

Following the brushing protocol is difficult at first, in early experiments some users didn't follow the correct order and either skipped or duplicated activities. The following activities are included for completeness but are unlabelled:

```
S4-S2-F-R-AW-26-M-1-AG
S5-S2-M-R-AW-40-M-2-AG
S7-S1-M-R-AW-31-M-2-AG
S7-S2-M-R-AW-31-M-2-AG
S7-S3-M-R-AW-31-M-2-AG
S8-S1-M-R-AW-31-M-2-AG
S8-S2-M-R-AW-31-M-2-AG
S9-S2-M-R-AW-30-M-2-AG
S10-S1-M-R-AW-30-E-3-AG
S11-S1-F-R-AW-30-M-3-AG
S13-S1-F-R-AW-30-M-4-AG
S13-S3-F-R-AW-30-M-4-AG
S14-S2-F-R-AW-35-M-5-AG
S15-S2-F-R-AW-30-M-5-AG
S16-S1-F-R-AW-28-M-5-AG
S16-S2-F-R-AW-28-M-5-AG
S16-S2-F-R-AW-28-M-5-AG
S16-S3-F-R-AW-28-M-5-AG
S17-S2-M-R-AW-40-M-2-AG
```