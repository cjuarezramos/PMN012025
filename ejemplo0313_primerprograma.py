#Programa para mostrar una tabla de de notas
#Autor: Carlos Juarez
#Fecha: 13/03/2025

nomb_eva1 = input('Nombre de la evaluación 1')
nomb_eva2 = input('Nombre de la evaluación 2')
nomb_eva3 = input('Nombre de la evaluación 3')
nomb_eva4 = input('Nombre de la evaluación 4')
nomb_eva5 = input('Nombre de la evaluación 5') 
nomb_eva6 = input('Nombre de la evaluación 6')
pond_eva1 = float(input('Ponderación de la evaluación 1'))
pond_eva2 = float(input('Ponderación de la evaluación 2'))
pond_eva3 = float(input('Ponderación de la evaluación 3'))
pond_eva4 = float(input('Ponderación de la evaluación 4'))
pond_eva5 = float(input('Ponderación de la evaluación 5'))
pond_eva6 = float(input('Ponderación de la evaluación 6'))
nota_eva1 = float(input('Nota de la evaluación 1'))
nota_eva2 = float(input('Nota de la evaluación 2'))
nota_eva3 = float(input('Nota de la evaluación 3'))
nota_eva4 = float(input('Nota de la evaluación 4'))
nota_eva5 = float(input('Nota de la evaluación 5'))
nota_eva6 = float(input('Nota de la evaluación 6'))
puntos_eva1 = pond_eva1 * nota_eva1
puntos_eva2 = pond_eva2 * nota_eva2
puntos_eva3 = pond_eva3 * nota_eva3
puntos_eva4 = pond_eva4 * nota_eva4
puntos_eva5 = pond_eva5 * nota_eva5
puntos_eva6 = pond_eva6 * nota_eva6
puntos_totales = puntos_eva1 + puntos_eva2 + puntos_eva3 + puntos_eva4 + puntos_eva5 + puntos_eva6
print('Evaluación\tPonderación\tNota\tPuntos')
print(nomb_eva1, '\t', pond_eva1, '\t', nota_eva1, '\t', puntos_eva1)
print(nomb_eva2, '\t', pond_eva2, '\t', nota_eva2, '\t', puntos_eva2)
print(nomb_eva3, '\t', pond_eva3, '\t', nota_eva3, '\t', puntos_eva3)
print(nomb_eva4, '\t', pond_eva4, '\t', nota_eva4, '\t', puntos_eva4)
print(nomb_eva5, '\t', pond_eva5, '\t', nota_eva5, '\t', puntos_eva5)
print(nomb_eva6, '\t', pond_eva6, '\t', nota_eva6, '\t', puntos_eva6)
print('Puntos totales:', puntos_totales)
