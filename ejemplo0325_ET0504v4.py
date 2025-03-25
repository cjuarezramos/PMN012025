#Autor: Carlos Juarez
#Fecha: 25/03/25
#Descripción: Programa para definir si un número es positivo o negativo o cero
# limitado a n<=100 y n>=-100
#Version 4
n = float(input('Ingrese número: '))
if n<=100 and n>=-100:
    if n == 0:
        print(f'{n} es neutro')
    elif n > 0:
        print(f'{n} es positivo')
    else:
        print(f'{n} es negativo')
else:
    print('Esta fuera del rango')
    

