# Convertir una cadena a flotante
cadena = "3.14"
flotante = float(cadena)
print(flotante)  # Imprime: 3.14
print(type(flotante))  # Imprime: <class 'float'>

# Convertir un entero a flotante
entero = 10
flotante = float(entero)
print(flotante)  # Imprime: 10.0

# Convertir un entero a booleano
entero = 1
booleano = bool(entero)
print(booleano)  # Imprime: True

entero = 0
booleano = bool(entero)
print(booleano)  # Imprime: False

# Convertir una cadena vacía a booleano
cadena = ""
booleano = bool(cadena)
print(booleano)  # Imprime: False

cadena = " "
booleano = bool(cadena)
print(booleano)  # Imprime: True