# https://www.notion.so/mau-dev/Recursividad-054901757456411dbb1d9bb31a6b0f11?pvs=25#5b004ddfeb38435984d0f03483de65ef
def factorial(n):
    if n == 0 or n == 1:  # Caso base
        return 1
    else:
        return n * factorial(n - 1)  # Caso recursivo

# Ejemplo de uso
print(factorial(5))  # Resultado: 120

factorial_5 = print(factorial(5)) # Resultado: 120

factorial_de_5 = factorial(5)
print(factorial_de_5) # Resultado: 120

def fibonacci(n):
    if n == 0:  # Caso base 1
        return 0
    elif n == 1:  # Caso base 2
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Caso recursivo

# Ejemplo de uso
number = 6 # Resultado: 8
# number = 0 # Resultado: 0
print(fibonacci(number))  

def suma_naturales(n):
    if n == 1:  # Caso base
        return 1
    else:
        return n + suma_naturales(n - 1)  # Caso recursivo

# Ejemplo de uso
print(suma_naturales(5))  # Resultado: 15