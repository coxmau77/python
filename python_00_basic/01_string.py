from turtle import clear


userName = "MAU26"
print(userName)
print(type(userName))

character = "x"
print(type(character))

char_example = 'A'
print(char_example)        # Imprime: A
print(type(char_example))  # Imprime: <class 'str'>

string_example = "Hello"
print(string_example)        # Imprime: Hello
print(type(string_example))  # Imprime: <class 'str'>

string_simple = 'Hola'
print(string_simple)  # Imprime: Hola

string_triple_simple = '''Este es un string
que abarca múltiples
líneas.'''
print(string_triple_simple)

string_triple_doble = """Este es otro string
que también abarca múltiples
líneas."""
print(string_triple_doble)

mensaje = 'Ella dijo: "Hola"'
print(mensaje)  # Imprime: Ella dijo: "Hola"

mensaje = "It's a wonderful day!"
print(mensaje)  # Imprime: It's a wonderful day!

# Indexacion
myName = "Mauricio"
print(myName[0]) # Imprime: M
print(myName[-2]) # Imprime: i

# Concatenación 
string1 = "Hola"
string2 = "Mundo"
resultado = string1 + " " + string2
print(resultado)  # Imprime: Hola Mundo

nombre = "Juan"
apellido = "Pérez"
nombre_completo = nombre + " " + apellido
print(nombre_completo)  # Imprime: Juan Pérez

edad = 30
mensaje = "Tengo " + str(edad) + " años."
print(mensaje)  # Imprime: Tengo 30 años.

saludo = "Hola"
saludo += " "
saludo += "Mundo"
print(saludo)  # Imprime: Hola Mundo

palabras = ["Hola", "Mundo", "desde", "Python"]
mensaje_A = " ".join(palabras)
mensaje_B = " *#$ ".join(palabras)
print(mensaje_A)  # Imprime: Hola Mundo desde Python
print(mensaje_B)  # Imprime: Hola *#$ Mundo *#$ desde *#$ Python

# replicación
mensaje = "Hola"
repeticiones = mensaje * 3
print(repeticiones)  # Imprime: HolaHolaHola

lista = [1, 2, 3]
repeticiones_lista = lista * 2
print(repeticiones_lista)  # Imprime: [1, 2, 3, 1, 2, 3]

ceros = [0] * 5
print(ceros)  # Imprime: [0, 0, 0, 0, 0]

tupla = (1, 2, 3)
repeticiones_tupla = tupla * 2
print(repeticiones_tupla)  # Imprime: (1, 2, 3, 1, 2, 3)

txt = "texto jemplo"
print(txt * 3)
print(3 * txt)

# len()
tupla = (1, 2, 3)
longitud_tupla = len(tupla)
print(longitud_tupla)  # Imprime: 3

diccionario = {"a": 1, "b": 2, "c": 3}
longitud_diccionario = len(diccionario)
print(longitud_diccionario)  # Imprime: 3

# Métodos 
mensaje = "hola mundo"
print(mensaje.upper())  # Imprime: HOLA MUNDO

mensaje = "hola mundo"
print(mensaje.capitalize())  # Imprime: Hola mundo

mensaje = "hola mundo"
print(mensaje.title())  # Imprime: Hola Mundo

mensaje = "  hola mundo  "
print(mensaje.strip())  # Imprime: hola mundo

mensaje = "hola mundo"
print(mensaje.replace("mundo", "Python"))  # Imprime: hola Python

mensaje = "hola mundo"
print(mensaje.split())  # Imprime: ['hola', 'mundo']

lista = ['hola', 'mundo']
print(" ".join(lista))  # Imprime: hola mundo
print(" *x/* ".join(lista))  # Imprime: hola *x/* mundo
print("".join(lista))  # Imprime: holamundo
print("-".join(lista))  # Imprime: hola-mundo

mensaje = "hola mundo"
print(mensaje.find("mundo"))  # Imprime: 5

mensaje = "EL bebe, bebe el biberon"
print(mensaje.count("bebe"))  # Imprime: 2

mensaje = "hola mundo"
print(mensaje.startswith("hola"))  # Imprime: True
print(mensaje.startswith("Hola"))  # Imprime: False

mensaje = "hola mundo"
print(mensaje.endswith("mundo"))  # Imprime: True
print(mensaje.endswith("mundo!"))  # Imprime: False