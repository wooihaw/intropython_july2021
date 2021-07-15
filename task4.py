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

word_freq = Counter(allwords)
print(f'The most common 10 words are {word_freq.most_common(10)}')
print(f'The word "alice" appears {word_freq["alice"]} times in the text.')