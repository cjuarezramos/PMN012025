#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  8 11:34:27 2025

@author: carlosjuarez
"""
import math
x = float(input('x='))
N = int(input('N='))
acum = 0
for n in range(0,N+1):
    acum = acum + x**n/math.factorial(n)
    
print(math.exp(x))
print(f'e({x})={acum}')