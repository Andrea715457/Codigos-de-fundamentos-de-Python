"""
Realizar un juego de papel piedra y tijeras haciendo uso de funciones
"""
import random
jugadas = ["piedra", "papel", "tijeras"]

def jugada_maquina():
    return random.choice(jugadas)

def jugada_usuario():
    return int(input("Ingrese una opcion: "))
def ganar():
    opcion_usuario = jugada_usuario()
    print("Tu jugada es: ",jugadas[opcion_usuario - 1])
    opcion_maquina = jugada_maquina()
    print("Jugada de la maquina: ",opcion_maquina)

    if (jugadas[opcion_usuario - 1] == "piedra"):
        if (opcion_maquina == "papel"):
            print("Perdiste")
        elif (opcion_maquina == "tijeras"):
            print("Ganaste")
        else:
            print("Empate")
    if (jugadas[opcion_usuario - 1] == "papel"):
        if (opcion_maquina == "tijeras"):
            print("Perdiste")
        elif (opcion_maquina == "piedra"):
            print("Ganaste")
        else:
            print("Empate")
    if (jugadas[opcion_usuario - 1] == "tijeras"):
        if (opcion_maquina == "piedra"):
            print("Perdiste")
        elif (opcion_maquina == "papel"):
            print("Ganaste")
        else:
            print("Empate")
    return 0


def  menu():
    print("Bienvenido al juego de piedra, papel y tijeras")
    print("Elije una opción: \n")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijeras\n")
    ganar()
    return 0

menu()
print("\n")
pregunta = input("Desea juegar de nuevo? (si/no): ")
while (pregunta == "si"):
    menu()
    print("\n")
    pregunta = input("Desea juegar de nuevo? (si/no): ")

print("\n") 
print("Gracias por jugar")