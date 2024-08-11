tupla_vacia = ()  # Tupla vacía
tupla_numeros = (1, 2, 3)
tupla_mixta = ("hola", 42, True)

def saludar(nombre, edad):
    print("Hola,", nombre, ". Tienes", edad, "años.")

persona = ("Ana", 25)
saludar(*persona)  # Desempaqueta la tupla como argumentos

for letra in ("a", "e", "i", "o", "u"):
    print(letra)