#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 00:16:58 2023

@author: simon
"""

import pandas as pd


accelerometer_df = pd.read_csv('data/accelerometer.csv', index_col=0)


x_plot = accelerometer_df['x'].plot(title='Accelerometer Data (x)')