# segundo enfoque del ejemplo de notas
# Autor: Carlos Juarez
# Fecha: 13/03/2025

N = int(input('Número de evaluaciones: '))
# nombre de variables tipo lista
nomb_eva = []
pond_eva = []
nota_eva = []
puntos_eva = []
# listado de evaluaciones
for i in range(N):
    nomb = input('Nombre de la evaluación ' + str(i + 1) + ': ')
    nomb_eva.append(nomb)
for i in range(N):
    pond = float(input('Ponderación de la evaluación ' + str(i + 1) + ': '))
    pond_eva.append(pond)
for i in range(N): 
    nota = float(input('Nota de la evaluación ' + str(i + 1) + ': '))
    nota_eva.append(nota)
for i in range(N):
    puntos = pond_eva[i] * nota_eva[i]
    puntos_eva.append(puntos)

puntos_totales = sum(puntos_eva)
print('Evaluación\tPonderación\tNota\tPuntos')
for i in range(N):
    print(nomb_eva[i], '\t', pond_eva[i], '\t', nota_eva[i], '\t', puntos_eva[i])   
print('Puntos totales:', puntos_totales)

# no hay copilot



