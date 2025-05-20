# Autor: Carlos Juarez
# Fecha: 2025-05-20
# Descripcion: Gràficas de e(x) y sin(x) y comparaciòn con series de taylor

# importar módulos o librerias que se necesitan
import numpy as np
import matplotlib.pyplot as plt
import math 

# función para Taylor de e(x)
def exponencialN(x,N):
    acumulador = 0
    for n in range(0,N):
        acumulador += x**n/math.factorial(n)
    return acumulador
def senoN(x,N):
    acumulador = 0
    for n in range(0,N):
        acumulador += (-1)**n*x**(2*n+1)/math.factorial(2*n+1)
    return acumulador

opc = int(input('1. Graficar e(x)\n2.Graficar sin(x)\nSu opción es:'))
match opc:
    case 1:
        N = int(input('Cantidad de terminos de la serie: '))
        xi = float(input('Valor inicial de x: '))
        xf = float(input('Valor final de x: '))
        x = np.arange(xi,xf,0.1)
        ymejor = np.exp(x)
        yserie = exponencialN(x,N)
        errorabsoluto = np.abs(ymejor-yserie)
        plt.figure()
        plt.plot(x,ymejor,x,yserie)
        plt.legend(['Numpy','Serie'])
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('y=e(x)')
        plt.show()
        plt.figure()
        plt.plot(x,errorabsoluto)
        plt.title('Gràfica del error')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()


print(yserie)

