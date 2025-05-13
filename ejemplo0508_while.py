#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  8 11:59:29 2025

@author: carlosjuarez
"""
import math
x = float(input('x ='))
acum = 0
E = 1e-6
n = 0
L1 = []
L2 = []
while x**n/math.factorial(n)>E:
    acum = acum + x**n/math.factorial(n)
    n += 1

print(f'e({x})={acum}')
