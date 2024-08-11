numeros = [1, 2, 3, 4, 5, 6]
impares = list(filter(lambda x: x % 2 != 0, numeros))
print(impares)  # Salida: [1, 3, 5]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Salida: [2, 4, 6]

from functools import reduce
numeros = [1, 2, 3, 4]
suma = reduce(lambda x, y: x + y, numeros)
print(suma)  # Salida: 10