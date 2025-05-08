numeros = input("Introduce una lista de números separados por comas: ")
print(numeros)
numeros = numeros.split(",")
print(numeros)
for i in range(len(numeros)):
    numeros[i] = int(numeros[i])
print(numeros)