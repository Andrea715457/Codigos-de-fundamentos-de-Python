#COndisionales: if, elif, else

#ejemplo 1: usuario y contraseña

user = "Andrea"
password = "1234"

user_input = input("Ingrese el usuario: ")
password_input = input("Ingrese la contraseña: ")

if (user_input == user and password_input == password):
    print("Bienvenido")
else:
    print("Usuario o contraseña incorrecto")

#Ejemplo 2 elif

nota = int(input("Ingrese una nota: "))
if nota >= 90:
    print("A")
elif nota >=80:
    print("B")
elif nota >= 70:
    print("C")
else:
    print("D")

"""
Ciclos repeticviones:
for y while
"""
#Ejemplo de while

contador = 1
while contador < 11:
    print(contador)
    contador += 1

#Ejemplo de for
for i in range(1,11):
    print(i)


usuario = "Andrea"
password = "1234"
intentos = 3

while intentos > 0:
    user_input = input("Ingrese el usuario: ")
    password_input = input("Ingrese la contraseña: ")

    if (user_input == user and password_input == password):
        print("Bienvenido")
    else:
        print("Usuario o contraseña incorrecto")
        intentos -=1
        print(f"Le quedan ${intentos} intentos")
        if intentos == 0:
            print("Usuario y contraseña bloqueadas")