x = 10

if x > 5:
    print("x es mayor que 5")

x = 3

if x > 5:
    print("x es mayor que 5")
else:
    print("x es 5 o menor")

x = 5

if x > 5:
    print("> x es mayor que 5")
elif x == 5:
    print("== x es igual a 5")
else:
    print("else x es menor que 5")

x = 10
y = 20

if x > 5 and y > 15:
    print("x es mayor que 5 y y es mayor que 15")

x = 10
y = 5
z = 20

if (x > 5 and y < 15) or z == 20:
    print("La condición es verdadera")

x = 10
y = 5

if x > 5 or y > 15:
    print("Al menos una condición es verdadera")

x = 10
y = 5

if not (x > 5 and y < 10):
    print("La condición es falsa")
else:
    print("La condición es verdadera")

is_member = True
age = 15

if is_member:
        if age >= 15:
            print("Tienes acceso, eres miembro y tu edad es mayor igual a 15 años")
        else:
            print("No tienes acceso,eres miembro pero eres menor a 15 años")
else:
    print("<<<< SiN ACCESO >>>>")