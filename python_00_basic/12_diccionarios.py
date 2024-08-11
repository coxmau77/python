mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

print(mi_diccionario)

nombre = mi_diccionario["nombre"]
print(nombre)  # Imprimirá: Juan

mi_diccionario["profesion"] = "Programador"
profesion = mi_diccionario["profesion"]
print(mi_diccionario)
print(profesion)  # Imprimirá: Programador

print(mi_diccionario["edad"])  # Imprimirá: 30
mi_diccionario["edad"] = 31
print(mi_diccionario["edad"])  # Imprimirá: 31


print(
    mi_diccionario
)  # Imprimirá: {'nombre': 'Juan', 'edad': 31, 'ciudad': 'Madrid', 'profesion': 'Programador'}
print(mi_diccionario["ciudad"])  # Imprimirá: Madrid
del mi_diccionario["ciudad"]
# print(mi_diccionario['ciudad']) # Imprimirá: KeyError: 'ciudad'

contact = {"nombre":"pepe",
        "apellido":"argento",
        "altura":1.82,
        "edad":50,
        "socio":True}

print(contact)

contacts = {
    "pepe": {"apellido": "argento", "altura": 1.82, "edad": 50, "socio": True},
    "mony": {"apellido": "argento", "altura": 1.70, "edad": 45, "socio": False},
}

print(contacts)
print(contacts["pepe"])
print(contacts["pepe"]["altura"])

for nombre, info in contacts.items():
    print(f"Nombre: {nombre}")
    for clave, valor in info.items():
        print(f"  {clave}: {valor}")