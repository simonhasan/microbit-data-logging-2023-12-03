#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 19:01:55 2023

@author: simon
"""

import pandas as pd

accelerometer_df = pd.read_csv('data/accelerometer.csv', index_col=0)
accelerometer_df.plot(title='Accelerometer Data')