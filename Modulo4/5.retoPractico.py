"""
Realizar uan palicación qeu permite registrar profesores y estudiantes, los cuales se guarden en una listagradlñasd.
cada profesor o estudiante tiene como atributos su nombre, edad, especialidad/grado. Además, cada persona
tiene un metodo que mestra su información. Crear un menu de opciones que permita ingresar profesores o 
estudiantes, mostrar todos los profesores y estuddiantes, o salir del programa
"""
from Modelos.profesor import Profesor
from Modelos.estudiante import Estudiante


def ingresar_datos_persona(tipo):
    nombre = input(f"Ingrese el nombre {tipo}: ")
    edad = int(input(f"Ingrese la edad {tipo}: "))
    return nombre, edad
    
def ingresar_profesor():
    nombre, edad = ingresar_datos_persona("profesor")
    especialidad = input("Ingrese la especialidad: ")
    profesor = Profesor(nombre, edad, especialidad)
    return profesor

def ingresar_estudiante():
    nombre, edad = ingresar_datos_persona("estudiante")
    grado = input("Ingrese el grado: ")
    estudiante = Estudiante(nombre, edad, grado)
    return estudiante

def mostrar_profesores(lista_profesores):
    for profesor in lista_profesores:
        print(profesor)

def mostrar_estudiantes(lista_estudiantes):
    for estudiante in lista_estudiantes:
        print(estudiante)

def menu():
    menu = """ \n
    1. Ingresar un profesor
    2. Ingresar un estudiante
    3. Mostrar todos los profesores
    4. Mostrar todos los estudiantes
    5. Salir
    """
    print(menu)
    opcion = int(input("Ingrese una opción: "))
    return opcion
        
menu()
def principal():
    lista_profesores = []
    lista_estudiantes = []
    while(True):
        opcion = menu()
        if opcion == 1:
            profesor = ingresar_profesor()
            lista_profesores.append(profesor)
        elif opcion == 2:
            estudiante = ingresar_estudiante()
            lista_estudiantes.append(estudiante)
        elif opcion == 3:
            print("____Profesores____")
            mostrar_profesores(lista_profesores)
        elif opcion == 4:
            print("____Estudiantes____")
            mostrar_estudiantes(lista_estudiantes)
        elif opcion == 5:
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    principal()

