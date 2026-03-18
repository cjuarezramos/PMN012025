#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 11:05:27 2026

@author: carlosjuarez
"""
a = int(input('Ingrese un nùmero entero:'))
b = int(input('Ingrese otro número entero:'))
# potencia
print(f'{a}^{b}={a**b}')
# multiplicacion
print(f'{a}*{b}={a*b}')
# division
res = a/b
print(f'{a}/{b}={a/b}')
print(f'Tipo de variable = {type(res)}')
# modulo
res = a%b
print(f'{a}%{b}={res}')
print(f'Tipo variable={type(res)}')

print(f'{a}+{b}={a+b}')
print(f'{a}-{b}={a-b}')



