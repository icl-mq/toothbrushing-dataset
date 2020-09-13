"""
Module providing functions to read datasets
"""

import os, glob, json
from collections import defaultdict
from pathlib import Path
import scipy.signal
import pandas as pd
import numpy as np


def _read_file(filename):
    """
    Each file should have the same structure

    epoch, timestamp and elapsed columns reprenting sample time and 3 data channels
    """

    # read raw file
    df=pd.read_csv(filename)

    # drop unused columns
    df = df.drop(["epoc (ms)","elapsed (s)"],axis=1)

    # convert timestamp to datetime
    df["timestamp"] = pd.to_datetime(df["timestamp (+1000)"], format='%Y-%m-%dT%H.%M.%S.%f')

    df = df.drop(["timestamp (+1000)"],axis=1)

    # index on timestamp
    df = df.set_index("timestamp")

    return df



def _interpolate(df, new_index, limit=1): # 5 milliseconds  
    return df.reindex(df.index | new_index).fillna(method='ffill', limit=limit).loc[new_index]

    

def read_sensor_data(
    path:str,                  # location of experiments
    experiment:str,            # experiment folder
    device:str,                # name of device (W1, W2)):
    freq="5L",                 # "5L" = 5ms = 200Hz
    ) ->  pd.DataFrame:         
    """ loads raw sensor data into dataframe """
    experiment_path = os.path.join(path, experiment)
    accelerometer_filename = glob.glob(os.path.join(experiment_path, f"*{device}*_Accelerometer.csv"))[0]
    gyroscope_filename = glob.glob(os.path.join(experiment_path, f"*{device}*_Gyroscope.csv"))[0]
    magnetometer_filename = glob.glob(os.path.join(experiment_path, f"*{device}*_Magnetometer.csv"))[0]

    # read the three sensors
    accelerometer = _read_file(accelerometer_filename)
    gyroscope = _read_file(gyroscope_filename)
    magnetometer = _read_file(magnetometer_filename)

    # in order to join we need to resample and interpolate
    start = np.max([
        accelerometer.index.min().ceil(freq), 
        gyroscope.index.min().ceil(freq), 
        magnetometer.index.min().ceil(freq)
        ])
    end = np.min([
        accelerometer.index.max().floor(freq), 
        gyroscope.index.max().floor(freq), 
        magnetometer.index.max().floor(freq)
        ])
    new_index = pd.date_range(start, end, freq=freq)

    accelerometer = _interpolate(accelerometer, new_index)
    gyroscope = _interpolate(gyroscope, new_index)
    magnetometer = _interpolate(magnetometer, new_index, limit=10) # sample rate is 1/10th of the other 2 sensors

    df = pd.concat((
        accelerometer,
        gyroscope,
        magnetometer
        ), axis=1)
    return df


def load_dataset(
    path,
    experiment, 
    device,
    timezone="Australia/Sydney",
    freq="5L"
    ):
    # load data
    df = read_sensor_data(path=path,experiment=experiment,device=device,freq=freq)
    df.index = df.index.tz_localize(timezone)
    df.index.name = 'timestamp'

    # load labels
    filename = os.path.join(path, experiment, f'labels.json')
    with open(filename, 'r') as fp:
        labels = json.load(fp)

    labels = pd.DataFrame.from_dict(labels, orient='index', columns=["from","to"])
    labels["from"] = pd.to_datetime(labels["from"]).dt.tz_convert(timezone) # have to convert from fixed offset
    labels["to"] = pd.to_datetime(labels["to"]).dt.tz_convert(timezone)
    labels = labels.sort_values("from")

    # locate the activities
    start = labels["from"].min()
    end = labels["to"].max()
    df = df[start:end]

    # label the activities
    start_idx = np.searchsorted(labels["from"].values, df.index.values)-1
    end_idx = np.searchsorted(labels["to"].values, df.index.values)
    mask = (start_idx == end_idx)

    df['label']=None
    df.loc[mask,'label']=labels.index[start_idx[mask]]
    df["label"]=df["label"].bfill() # hack mainly to fix first row missing label

    return df.drop("label", axis=1), df["label"]

