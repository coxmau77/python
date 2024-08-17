# https://www.notion.so/mau-dev/Manejo-de-Excepciones-en-Python-y-uso-de-pass-40bf2addf6f44f379a57d43cab9b013c

# ejemplo N°1
# try:
#     resultado = 10 / 0
# except ZeroDivisionError:
#     print("No se puede dividir por cero.")

# ejemplo N°2
# try:
#     valor = int(input("Ingresa un número: "))
#     resultado = 10 / valor
#     print("Resultado: ", resultado)
# except ValueError:
#     print("Por favor, ingresa un número válido.")
# except ZeroDivisionError:
#     print("No se puede dividir por cero.")

def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)

print_exception_hierarchy(Exception)

