# Código de ejemplo en diapoisitivas sobre diseño de algoritmos
# Segundo enfoque
#Autor: Carlos Juárez
#Fecha: 12/03/2025
nomb_eval = input("Ingrese el listado de evaluaciones separadas por comas: ")
nomb_eval = nomb_eval.split(",")    # Se convierte la cadena en una lista

pond_eval = []
nota_eval = []
punto_eval = []

for i in nomb_eval:
    print('Ingrese la ponderación de ' + i + ': ')
    pond_eval.append(float(input()))
    print('Ingrese la nota de ' + i + ':')
    nota_eval.append(float(input()))

n = len(nomb_eval)
i = 1

while i <= n:
    punto_eval.append(pond_eval[i-1] * nota_eval[i-1])
    i += 1 

nota_final = sum(punto_eval)

print("Nombre de evaluación    Ponderación    Nota    Puntos obtenidos")
for i in range(n):
    print(nomb_eval[i], "    ", pond_eval[i], "    ", nota_eval[i], "    ", punto_eval[i])  
print("Nota final: ", nota_final)

