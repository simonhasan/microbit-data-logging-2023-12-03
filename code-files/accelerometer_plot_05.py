#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 00:28:11 2023

@author: simon
"""

import pandas as pd
import matplotlib.pyplot as plt

accelerometer_df = pd.read_csv('data/accelerometer.csv', index_col=0)

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharey=True)
ax1.plot(accelerometer_df['x'], label='x')
ax1.set_title('x')


ax2.plot(accelerometer_df['y'], label='y', color='red')
ax2.set_title('y')

ax3.plot(accelerometer_df['z'], label='z', color='green')
ax3.set_title('z')

fig.suptitle('Accelerometer Data')
fig.legend()

plt.show()