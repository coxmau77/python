numeros = [3, 7, 2, 8, 5]
mayor = max(numeros)
print(mayor)  # Salida: 8

menor = min(numeros)
print(menor)  # Salida: 2

palabras = ["manzana", "naranja", "banana", "pera"]
print(max(palabras))  # Salida: "pera"
print(min(palabras))  # Salida: "banana"
# Encontrar la palabra más larga
print(max(palabras, key=len))  # Salida: "naranja"
# Encontrar la palabra más corta
print(min(palabras, key=len))  # Salida: "pera"