#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 19:19:04 2023

@author: simon
"""

import pandas as pd


light_df = pd.read_csv('data/light.csv', index_col=0)


light_plot = light_df.plot(title='Light Sensor Data')
