#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 00:10:37 2023

@author: simon
"""

import pandas as pd


accelerometer_df = pd.read_csv('data/accelerometer.csv', index_col=0)


accelerometer_plot = accelerometer_df.plot(title='Accelerometer Data')