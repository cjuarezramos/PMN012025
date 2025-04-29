#Autor: Carlos Juarez
#Fecha: 29/04/2025
#Descripción: calculo de promedio y desviacion estandar de un conjunto de datos.

#Variables para almacenar los datos
n = []
solicitud = True
#Bucle para solicitar los datos al usuario
while solicitud:
    x = float(input('Ingrese un numero: '))
    n.append(x)
    #Condicion para salir del bucle
    solicitud = int(input('¿Desea ingresar otro numero? (1 continuar, 0 salir): '))

#Calculo del promedio
suma1 = 0
longn=len(n)
for i in range(longn):
    suma1 += n[i] # es igual a suma1 = suma1 + n[i]

xp=suma1/longn #promedio
print('El promedio es: ',xp)