# https://www.notion.so/mau-dev/Fundamentos-de-Programaci-n-Orientada-a-Objetos-en-Python-3ba6a14fdd7d47f89112545719c65e31

# Definición de la clase Persona
class Persona:
    # Método constructor: se llama automáticamente cuando se crea un objeto de esta clase
    def __init__(self, nombre, apellido, fecha_nacimiento):
        self.nombre = nombre  # Atributo nombre
        self.apellido = apellido  # Atributo apellido
        self.fecha_nacimiento = fecha_nacimiento  # Atributo fecha_nacimiento

    # Método para mostrar la información de la persona
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Fecha de Nacimiento: {self.fecha_nacimiento}")

# Creación de un objeto de la clase Persona
persona1 = Persona("Juan", "Pérez", "01/01/1990")

# Uso del método mostrar_informacion() para mostrar los datos de persona1
persona1.mostrar_informacion()

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
    
    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Se ha depositado {amount}. Saldo actual: {self.balance}")
        else:
            print("No se puede depositar, cuenta inactiva")
    
    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Se ha retirado {amount}. Saldo actual: {self.balance}")
            else:
                print("Fondos insuficientes")
        else:
            print("No se puede retirar, cuenta inactiva")
    
    def deactivate(self):
        self.is_active = False
        print("La cuenta ha sido desactivada")
    
    def activate(self):
        self.is_active = True
        print("La cuenta ha sido activada")

# Crear objetos de la clase BankAccount
cuenta1 = BankAccount("Ana", 500)
cuenta2 = BankAccount("Luis", 1000)

cuenta1.deposit(500)
cuenta2.withdraw(100)
cuenta1.deactivate()
cuenta1.deposit(200)
cuenta1.activate()
cuenta1.deposit(200)