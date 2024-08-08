a = 10
b = 5
resultado = a + b
print(resultado)  # Imprime: 15

a = 10
b = 5
resultado = a - b
print(resultado)  # Imprime: 5

a = 10
b = 5
resultado = a * b
print(resultado)  # Imprime: 50

a = 10
b = 5
resultado = a / b
print(resultado)  # Imprime: 2.0

a = 10
b = 3
resultado = a // b
print(resultado)  # Imprime: 3

a = 10
b = 3
resultado = a % b
print(resultado)  # Imprime: 1

a = 2
b = 3
resultado = a ** b
print(resultado)  # Imprime: 8

# Operadores de atajo u Operadores de asignación compuesta
x = 5
print(x)  # Imprime: 5
x += 3  # Equivalente a x = x + 3
print(x)  # Imprime: 8

y = 10
y -= 4  # Equivalente a y = y - 4
print(y)  # Imprime: 6

z = 7
z *= 2  # Equivalente a z = z * 2
print(z)  # Imprime: 14

a = 20
a /= 4  # Equivalente a a = a / 4
print(a)  # Imprime: 5.0

b = 15
b //= 2  # Equivalente a b = b // 2
print(b)  # Imprime: 7

c = 9
c %= 4  # Equivalente a c = c % 4
print(c)  # Imprime: 1

q = 10
q %= 2  # Equivalente a c = c % 2
print(q)  # Imprime: 0

d = 3
d **= 2  # Equivalente a d = d ** 2
print(d)  # Imprime: 9

# Sin operador de atajo
x = x + 5

# Con operador de atajo
x += 5

mensaje = "Hola"
mensaje += " Mundo"  # Equivalente a mensaje = mensaje + " Mundo"
print(mensaje)  # Imprime: Hola Mundo

lista = [1, 2, 3]
lista *= 2  # Equivalente a lista = lista * 2
print(lista)  # Imprime: [1, 2, 3, 1, 2, 3]

# ¿Qué es PEMDAS y cómo afecta nuestras operaciones?
operation = (2 + 3) * 4
print(operation)  # Resultado: 20

lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = [3, 2, 1]
print(lista1 == lista2)  # Imprime: True
print(lista1 == lista3)  # Imprime: False

a = "Hola"
b = "Mundo"
print(a == b)  # Imprime: False
print(a != b)  # Imprime: True
print(a < b)   # Imprime: True (comparación lexicográfica)