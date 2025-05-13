datos_evaluaciones = input('Ingrese informacion de las evaluaciones')
datos_evaluaciones = datos_evaluaciones.split(',')  # Convertir la cadena de texto en una lista
print(datos_evaluaciones)
nombre_evaluaciones = datos_evaluaciones[0:len(datos_evaluaciones):2]
print(nombre_evaluaciones)
ponderaciones_evaluaciones = datos_evaluaciones[1:len(datos_evaluaciones):2]
print(ponderaciones_evaluaciones)
for i in range(len(ponderaciones_evaluaciones)):
    ponderaciones_evaluaciones[i] = float(ponderaciones_evaluaciones[i])  # Convertir cada elemento a float
print(ponderaciones_evaluaciones)