# Definimos un generador simple
def mi_generador():
    yield 1
    yield 2
    yield 3
    yield 1.99
    yield "cinco"

# Creamos el generador
gen = mi_generador()

# Obtenemos los valores uno por uno
print(next(gen))  # Imprime: 1
print(next(gen))  # Imprime: 2
print(next(gen))  # Imprime: 3
print(next(gen))  # Imprime: 1.99
print(next(gen))  # Imprime: cinco

# Al igual que con los iteradores, si seguimos llamando a next(), se lanzará una excepción StopIteration

for value in mi_generador():
    print(value)

# Fibonacci
# 0 1 1 2 3 5 8 13 21 34...

def fibonacci(limit):
    a,b = 0,1
    while a < limit:
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)