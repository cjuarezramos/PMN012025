"""
Autor: Carlos Juárez
Fecha: 26/03/2025
Descripción: Ejercicio para calcular areas de rectangulo y circulo
Version 2
"""
print('Este programa calcular superfices, las opciones son')
print('\t1. Rectangulo\n\t2. Circulo')
opcion = int(input('Ingrese su opción: '))

if opcion == 1:
    base = float(input('Ingrese la base del rectangulo: '))
    altura = float(input('Ingrese la altura del rectangulo: '))
    Area = base * altura
    print(f'La superficie del rectangulo es: {Area}m^2')
elif opcion == 2:
    radio = float(input('Ingrese radio del circulo: '))
    Area = 3.1416*radio**2
    print(f'La superficie del circulo es: {Area}m^2')
else:
    print('Ha elegido una opción incorrecta')

