#Autor: Carlos Juarez
#Fecha: 25/03/25
#Descripción: Programa para definir si un número es positivo o negativo o cero
# limitado a n<=100 y n>=-100
#Version 3
n = float(input('Ingrese un número: '))
if n>100 or n<-100:
    print('El número está fuera de los limites')
elif n==0:
    print(f'{n} es neutro')
elif n>0:
    print(f'{n} es positivo')
else:
    print(f'{n} es negativo')

