# https://www.notion.so/mau-dev/Funciones-Lambda-y-Programaci-n-Funcional-en-Python-589e0e140f1c45018f8585747a9adb8a
numeros = [1, 2, 3, 4, 5, 6]

impares = list(filter(lambda x: x % 2 != 0, numeros))
print(impares)  # Salida: [1, 3, 5]

pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Salida: [2, 4, 6]

from functools import reduce

numeros = [1, 2, 3, 4]
suma = reduce(lambda x, y: x + y, numeros)
print(suma)  # Salida: 10

sumar_diez = lambda x: x + 10
print(sumar_diez(5))  # Salida: 15

cuadrados = list(map(lambda x: x ** 2, numeros))
print(cuadrados)  # Salida: [1, 4, 9, 16, 25]