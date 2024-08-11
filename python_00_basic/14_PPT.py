import random

# Opciones disponibles
opciones = ["piedra", "papel", "tijera"]

# Entrada del jugador
jugador = input("Elige piedra, papel o tijera: ").lower()

# Elección de la computadora
computadora = random.choice(opciones)

# Mostrar la elección de la computadora
print(f"La computadora eligió: {computadora}")

# Estructura condicional para determinar el ganador
if jugador == computadora:
    print("¡Es un empate!")
elif jugador == "piedra":
    if computadora == "tijera":
        print("¡Ganaste! Piedra aplasta tijera.")
    else:
        print("Perdiste. Papel envuelve piedra.")
elif jugador == "papel":
    if computadora == "piedra":
        print("¡Ganaste! Papel envuelve piedra.")
    else:
        print("Perdiste. Tijera corta papel.")
elif jugador == "tijera":
    if computadora == "papel":
        print("¡Ganaste! Tijera corta papel.")
    else:
        print("Perdiste. Piedra aplasta tijera.")
else:
    print("Opción no válida. Por favor, elige piedra, papel o tijera.")
