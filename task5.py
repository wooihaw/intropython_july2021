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

cases_8000 = df['Cases'] > 8000
print(f'There are {sum(cases_8000)} days with more than 8000 cases')
print(df[cases_8000])

# Plot bar chart for cases per month
m_groups = df.groupby(df.index.to_period('M'))
m_groups['Cases'].sum().plot.bar()
plt.title('Monthly new cases')
plt.show()

# Plot bar chart for total cases for each day of the week
d_groups = df.groupby(df.index.day_name())
d_groups['Cases'].sum().plot.bar()
plt.title('Total new cases for each day of the week')
plt.show()