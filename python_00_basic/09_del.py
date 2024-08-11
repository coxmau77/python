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

lista = [1, 2, 3, 4, 5]
print(lista) # Salida: [1, 2, 3, 4, 5]
sub_lista = lista[:]
print(sub_lista)  # Salida: [1, 2, 3, 4, 5]

a = 1000
b = 1000

print(id(a))  # Identificador de a
print(id(b))  # Identificador de b

# Comprobar si son el mismo objeto
print(id(a) == id(b))  # Salida: True (En algunos casos Python reutiliza los enteros pequeños)

lista1 = [1, 2, 3]
lista2 = [1, 2, 3]

print(id(lista1))  # Identificador de lista1
print(id(lista2))  # Identificador de lista2

lista3 = lista1[:]
print(id(lista1))  # Identificador de lista1: 1797960267712
print(id(lista3))  # Identificador de lista3:1797960267584

print(lista1)
print(lista2)
print(lista3)

lista1.append(7)

print(lista1)
print(lista2)
print(lista3)