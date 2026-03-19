# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
Descripcion Operaciones aritmeticas
"""
a = int(input('Ingrese un entero:'))
b = int(input ('Ingrese otro entero'))
# potencia
res = a**b
print(f'{a}**{b}={res}')

res = a/b
print(f'{a}/{b}={res}')
print(f'El tipo de resultado es {type(res)}')

res = a%b
print(f'{a}%{b}={res}')
print(f'El tipo de resultado es {type(res)}')

res = a*b
print(f'{a}*{b}={res}')

res = a+b
print(f'{a}+{b}={res}')

res = a-b
print(f'{a}-{b}={res}')