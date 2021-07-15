# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 16:58:41 2021

@author: wooihaw
"""
# Task 4
from collections import Counter

with open('alice.txt', 'r') as f:
    s = f.read()
    
# print(s)
t = [c.lower() if c.isalpha() else ' ' for c in s]
w = ''.join(t)
allwords = w.split()
print(allwords)