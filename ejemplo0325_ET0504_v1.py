#Autor: Carlos Juarez
#Fecha: 25/03/25
#Descripción: Programa para definir si un número es positivo o negativo o cero

n = float(input("Ingrese un número: "))
if n == 0:
    print(f'{n} es elemento neutro')
else:
    if n > 0:
        print(f'{n} es positivo')
    else:
        print(f'{n} es negativo')

