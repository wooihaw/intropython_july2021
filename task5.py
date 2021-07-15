# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 17:12:20 2021

@author: wooihaw
"""
# Task 5
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/wooihaw/datasets/main/covid19_malaysia.csv')
print(df.sample(10))

df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
