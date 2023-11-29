#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 00:18:51 2023

@author: simon
"""

import pandas as pd
import matplotlib.pyplot as plt

accelerometer_df = pd.read_csv('data/accelerometer.csv', index_col=0)


fig, axes = plt.subplots(nrows=3)

accelerometer_df['x'].plot(ax=axes[0])
accelerometer_df['y'].plot(ax=axes[1], color='red')
accelerometer_df['z'].plot(ax=axes[2], color='green')

fig.suptitle('Accelerometer Data')
fig.legend()

plt.show()
