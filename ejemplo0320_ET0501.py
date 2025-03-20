# Autor: Carlos Juarez
# Fecha: 20/03/25
# Descripción: Ejemplo de clases ET0501 pide dos numeros y 
# da como resultado cociente y residuo
a = int(input('Ingrese un número entero: ')) # input para solicitar algo al usuario
b = int(input('Ingrese otro número entero: ')) # int para convertir a entero
# Calcular cociente
cociente = a//b # // calcula el entero de la division o cociente
residuo = a % b # % calcula el módulo o residuo de la división
# Imprimir resultados
print(f"Cociente de {a}/{b} es {cociente}")
print(f"Residuo de {a}/{b} es {residuo}")
