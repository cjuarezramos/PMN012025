datos_evaluaciones = input('Ingrese informacion de evaluaciones')
# Separa los datos por comas
datos_evaluaciones = datos_evaluaciones.split(',')
print(datos_evaluaciones)

Nombre_evaluaciones = datos_evaluaciones[0:len(datos_evaluaciones):2]
Ponderaciones = datos_evaluaciones[1:len(datos_evaluaciones):2]
print(Nombre_evaluaciones)