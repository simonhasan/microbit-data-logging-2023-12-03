#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 00:36:38 2023

@author: simon
"""

import pandas as pd
import matplotlib.pyplot as plt

accelerometer_df = pd.read_csv('data/accelerometer.csv', index_col=0)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True)
ax1.plot(accelerometer_df['x'])
ax1.set_title('x')
ax1.set_xlabel('Time (ms)')

ax2.plot(accelerometer_df['y'], color='red')
ax2.set_title('y')
ax2.set_xlabel('Time (ms)')

ax3.plot(accelerometer_df['z'], color='green')
ax3.set_title('z')
ax3.set_xlabel('Time (ms)')

fig.suptitle('Accelerometer Data')

plt.show()
