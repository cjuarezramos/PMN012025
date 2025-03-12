# Código de ejemplo en diapoisitivas sobre diseño de algoritmos
# Primer enfoque
#Autor: Carlos Juárez
#Fecha: 12/03/2025
nomb_eval1 = input("Ingrese el nombre del primer evaluado: ")
nomb_eval2 = input("Ingrese el nombre del segundo evaluado: ")
nomb_eval3 = input("Ingrese el nombre del tercer evaluado: ")
nomb_eval4 = input("Ingrese el nombre del cuarto evaluado: ")
nomb_eval5 = input("Ingrese el nombre del quinto evaluado: ")
nomb_eval6 = input("Ingrese el nombre del sexto evaluado: ")
pond_eval1 = float(input("Ingrese la ponderación del primer evaluado: "))
pond_eval2 = float(input("Ingrese la ponderación del segundo evaluado: "))
pond_eval3 = float(input("Ingrese la ponderación del tercer evaluado: "))
pond_eval4 = float(input("Ingrese la ponderación del cuarto evaluado: "))
pond_eval5 = float(input("Ingrese la ponderación del quinto evaluado: "))
pond_eval6 = float(input("Ingrese la ponderación del sexto evaluado: "))
nota_eval1 = float(input("Ingrese la nota del primer evaluado: "))
nota_eval2 = float(input("Ingrese la nota del segundo evaluado: "))
nota_eval3 = float(input("Ingrese la nota del tercer evaluado: "))
nota_eval4 = float(input("Ingrese la nota del cuarto evaluado: "))
nota_eval5 = float(input("Ingrese la nota del quinto evaluado: "))
nota_eval6 = float(input("Ingrese la nota del sexto evaluado: "))
punto_eval1 = pond_eval1 * nota_eval1
punto_eval2 = pond_eval2 * nota_eval2
punto_eval3 = pond_eval3 * nota_eval3
punto_eval4 = pond_eval4 * nota_eval4
punto_eval5 = pond_eval5 * nota_eval5
punto_eval6 = pond_eval6 * nota_eval6
nota_final = punto_eval1 + punto_eval2 + punto_eval3 + punto_eval4 + punto_eval5 + punto_eval6
print("Nombre de evaluación    Ponderación    Nota    Puntos obtenidos")
print(nomb_eval1, "    ", pond_eval1, "    ", nota_eval1, "    ", punto_eval1)
print(nomb_eval2, "    ", pond_eval2, "    ", nota_eval2, "    ", punto_eval2)
print(nomb_eval3, "    ", pond_eval3, "    ", nota_eval3, "    ", punto_eval3)
print(nomb_eval4, "    ", pond_eval4, "    ", nota_eval4, "    ", punto_eval4)
print(nomb_eval5, "    ", pond_eval5, "    ", nota_eval5, "    ", punto_eval5)
print(nomb_eval6, "    ", pond_eval6, "    ", nota_eval6, "    ", punto_eval6)
print("Nota final: ", nota_final)
