# Enteros positivos
a = 10
print(a)  # Imprime: 10
print(type(a))  # Imprime: <class 'int'>

# Enteros negativos
b = -5
print(b)  # Imprime: -5

# Cero
c = 0
print(c)  # Imprime: 0

# Suma
suma = 5 + 3
print(suma)  # Imprime: 8

# Resta
resta = 10 - 2
print(resta)  # Imprime: 8

# Multiplicación
multiplicacion = 4 * 3
print(multiplicacion)  # Imprime: 12

# División
division = 10 // 2  # División entera
print(division)  # Imprime: 5

# Módulo (resto de la división)
modulo = 10 % 3
print(modulo)  # Imprime: 1

print(type(10 % 2 == 0)) # Imprime: <class 'bool'>

# Flotante positivo
d = 3.14
print(d)  # Imprime: 3.14
print(type(d))  # Imprime: <class 'float'>

# Flotante negativo
e = -2.718
print(e)  # Imprime: -2.718

# Flotante con notación científica
f = 1.23e4  # 1.23 x 10^4
o = 1.23E4  # 1.23 x 10^4
print(f)  # Imprime: 12300.0
print(type(f))  # Imprime: <class 'float'>
print(o)  # Imprime: 12300.0

t = 1.23e-4 
print(t) # Imprime: 0.000123
print(type(t)) # Imprime: <class 'float'>

# Suma
suma_float = 1.5 + 2.3
print(suma_float)  # Imprime: 3.8

# Resta
resta_float = 5.7 - 2.2
print(resta_float)  # Imprime: 3.5

# Multiplicación
multiplicacion_float = 3.0 * 2.5
print(multiplicacion_float)  # Imprime: 7.5

# División
division_float = 7.5 / 2.5
print(division_float)  # Imprime: 3.0

# Verdadero
g = True
print(g)  # Imprime: True

# Falso
h = False
print(h)  # Imprime: False
print(type(h))  # Imprime: <class 'bool'>

# Operadores lógicos
verdadero = True
falso = False

# AND lógico
and_logico = verdadero and falso
print(and_logico)  # Imprime: False

# OR lógico
or_logico = verdadero or falso
print(or_logico)  # Imprime: True

# NOT lógico
not_logico = not verdadero
print(not_logico)  # Imprime: False

frase = "Aprendiendo Python"
author = "Mauricio"
print("Frase: {}, Autor: {}".format(frase, author)) # Imprime: Frase: Aprendiendo Python, Autor: Mauricio

valor = 3.14159
print("Valor: {:.2f}".format(valor)) # Imprime: Valor: 3.14