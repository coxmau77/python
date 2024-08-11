mi_lista = [1, 2, 3]
mi_lista.append(4)
print(mi_lista)  # Salida: [1, 2, 3, 4]

mi_lista.extend([4, 5, 6])
print(mi_lista)  # Salida: [1, 2, 3, 4, 5, 6]

mi_lista.insert(1, 'a')
print(mi_lista)  # Salida: [1, 'a', 2, 3, 4, 4, 5, 6]

mi_lista.remove(2)
print(mi_lista)  # Salida: [1, 'a', 3, 4, 4, 5, 6]

mi_lista = [1, 2, 3]
elemento = mi_lista.pop(1)
print(elemento)  # Salida: 2
print(mi_lista)  # Salida: [1, 3]