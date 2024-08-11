def saludar(nombre):
    return f"Hola, {nombre}!"

print(saludar("Ana"))  # Imprime: Hola, Ana!

def sumar(a, b):
    return a + b

print(sumar(3, 4))  # Imprime: 7

def saludar(nombre="Mundo"):
    return f"Hola, {nombre}!"

print(saludar())          # Imprime: Hola, Mundo!
print(saludar("Carlos"))  # Imprime: Hola, Carlos!

sumar = lambda a, b: a + b
print(sumar(5, 3))  # Imprime: 8

def operacion(func, a, b):
    return func(a, b)

def sumar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

print(operacion(sumar, 2, 3))        # Imprime: 5
print(operacion(multiplicar, 2, 3))  # Imprime: 6

def decorador(func):
    def envoltura():
        print("Antes de la función")
        func()
        print("Después de la función")
    return envoltura

@decorador
def saludar():
    print("Hola!")

saludar()

def operaciones(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division

s, r, m, d = operaciones(10, 5)
print(f"Suma: {s}, Resta: {r}, Multiplicación: {m}, División: {d}")