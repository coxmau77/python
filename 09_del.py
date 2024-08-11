x = 10
print(x) # Salida: 10
del x
# print(x)  # Esto causará un error porque `x` ya no existe

mi_lista = [1, 2, 3, 4, 5]
del mi_lista[2]
print(mi_lista)  # Salida: [1, 2, 4, 5]

mi_lista = [1, 2, 3, 4, 5]
del mi_lista[1:4]
print(mi_lista)  # Salida: [1, 5]

mi_diccionario = {'a': 1, 'b': 2, 'c': 3}
del mi_diccionario['b']
print(mi_diccionario)  # Salida: {'a': 1, 'c': 3}

mi_lista_anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
del mi_lista_anidada[1][2]  # Elimina el número 6 de la segunda sublista
print(mi_lista_anidada)  # Salida: [[1, 2, 3], [4, 5], [7, 8, 9]]
