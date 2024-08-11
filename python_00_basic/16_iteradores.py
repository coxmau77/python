# Creamos una lista simple
from operator import index


mi_lista = [1, 2, 3, 4]

# Convertimos la lista en un iterador
iterador = iter(mi_lista)

# Usamos el método next() para obtener los elementos uno por uno
print(next(iter(mi_lista)))  # Imprime: 1
print(next(iterador))  # Imprime: 1
print(next(iterador))  # Imprime: 2
print(next(iterador))  # Imprime: 3
print(next(iterador))  # Imprime: 4

# Si intentamos hacer next() de nuevo, lanzará una excepción StopIteration
# print(next(iterador))  # Imprime: ERROR StopIteration
index = 0

while index < len(mi_lista):
    print(f"mi_lista[{index + 1}] >> {mi_lista[index]}")
    index += 1

mi_string = "Python"

# Iterar con índice y valor
for indice, caracter in enumerate(mi_string):
    print(f"Índice: {indice}, Carácter: {caracter}")

mi_lista = [10, 15, 20, 25, 30, 35, 40]

# Iterar sobre la lista usando range
numeros_impares = []
numeros_pares = []
for i in range(len(mi_lista)):
    if mi_lista[i] % 2 != 0:
        numeros_impares.append(mi_lista[i])
    else:
        numeros_pares.append(mi_lista[i])

print("Números impares:", numeros_impares)
print("Números pares:", numeros_pares)

limit = 10

odd_iter = iter(range( 1, limit + 1, 2 ))

for num in odd_iter:
    print(num)