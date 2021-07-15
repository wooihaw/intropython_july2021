# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 16:49:07 2021

@author: wooihaw
"""
# Task 3
import numpy as np

temperatures = []
with open('Heathrow.txt', 'r') as f:
    for line in f:
        temperatures.append(float(f.readline().strip()))
        
print(temperatures)