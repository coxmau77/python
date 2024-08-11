numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    print(number)

for number in numbers:
    cuadrado = number ** 2
    print(f"El cuadrado de {number} es {cuadrado}")

for i in range(5):
    print(i)

for i in range(2, 6):
    print(i)

fruits = ["Pera","Sandía","Ananá","Kiwi","Uva","Manzana"]
for fruit in fruits:
    print(fruit)
    if fruit == "Kiwi":
        print(f"Encontramos el {fruit} en la lista")

cadena = "Hola, mundo!"
vocales = "aeiouAEIOU"
nueva_cadena = ""
for letra in cadena:
    if letra in vocales:
        continue  # Si la letra es una vocal, la omitimos
    nueva_cadena += letra
print(nueva_cadena)