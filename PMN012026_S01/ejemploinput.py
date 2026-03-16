#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 12:31:59 2026

@author: carlosjuarez
# instruccion input
"""
r = input('Ingrese el radio = ') # ingresa como texto
r = float(r) # cambiar a flotante
pi = 3.1416

A = pi*r**2
P = 2*pi*r
# f significa sustituir en la cadena de texto
# el valor de la variable
# \n significa salto de linea
print(f'El área es {A}\nEl perimetro es {P}')