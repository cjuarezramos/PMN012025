"""
Autor: Carlos Juárez
Fecha: 26/03/2025
Descripción: Ejercicio si un punto pertence a recta secciòn 01
"""
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))
m = float(input('pendiente = '))
b = float(input('intercepto = '))
y = m*x1 + b
if y == y1:
    print(f'({x1},{y1}) pertenece a y={m}x+{b}')
else:
    print(f'({x1},{y1}) NO pertenece a y={m}x+{b}')

