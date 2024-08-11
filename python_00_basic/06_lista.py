to_do = [
    'Salir a caminar',
    'Ir a almorzar',
    'Prácticas de código',
    'Repasar teoía'
]

print(to_do)

numbers = [1, 2, 3, 4, 'cinco']

print(numbers)
print(type(numbers))

numbers *= 2
print(numbers) # Imprime: [1, 2, 3, 4, 'cinco', 1, 2, 3, 4, 'cinco']

# Crear una lista
mi_lista = [1, 2, 3, "cuatro", 5.0]

# Acceder a elementos de la lista (indexación empieza en 0)
print(mi_lista[0])  # Salida: 1
print(mi_lista[3])  # Salida: "cuatro"

# Agregar un elemento al final de la lista
mi_lista.append(6)
print(mi_lista)  # Salida: [1, 'dos', 3, 'cuatro', 5.0, 6]

# Eliminar un elemento de la lista
mi_lista.remove("cuatro")
print(mi_lista)  # Salida: [1, 'dos', 3, 5.0, 6]

mix = ["string", 1, 1.99, True, ['a','e','i','o','u']]
print(mix)
print("Cuantos elementos contiene? >> ", len(mix))
print("Elemento 1 >> ", mix[0])
print("Elemento 2 >> ", mix[2])
print("Elemento 3 >> ", mix[3])
print("Elemento 4 >> ", mix[4])
print("Elemento 4 >> ", mix[-1])

mi_lista = [10, 20, 30, 40, 50, 60, 70, 80]
sub_lista = mi_lista[1:4]
print(sub_lista)  # Salida: [20, 30, 40]

sub_lista = mi_lista[0:7:2]
print(sub_lista)  # Salida: [10, 30, 50, 70]

sub_lista = mi_lista[:4]  # Desde el inicio hasta el índice 4 (excluido)
print(sub_lista)  # Salida: [10, 20, 30, 40]

sub_lista = mi_lista[2:]  # Desde el índice 2 hasta el final
print(sub_lista)  # Salida: [30, 40, 50, 60, 70, 80]

sub_lista = mi_lista[::2]  # Desde el inicio hasta el final, saltando de dos en dos
print(sub_lista)  # Salida: [10, 30, 50, 70]

sub_lista = mi_lista[::-1]
print(mi_lista)   # Salida: [10, 20, 30, 40, 50, 60, 70, 80]
print(sub_lista)  # Salida: [80, 70, 60, 50, 40, 30, 20, 10]