"""
La encapsulacion es otro de los principios fundamentales de la programacion orientada a objetos (POO). En python

Tipos de encapsulación 

Atributos Públicos:
Son accesibles desde cualquier lugar, tanto dentro como fuera de la clase
No tiene prefijos especiales.

Atributos Protegidos:
Son accesibles dentro de la clase y en las subclases
Se denotan con un guin bajo inicial(_atributo)

Atributos Privados:
Son accesibkes solo dentro de clases donde se definen.
Se denotan con dos guies bajos iniciales(__atributos)
"""

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre #privado
        self.__edad = edad #privado
        self.__cedula = "38903462" #privado

    def mostrar_edad(selft):
        if selft.__edad<0:
            print("Edad valida")
            return
        print(selft.__edad)

    def mostrar_cedula(selft):
        print(selft.__cedula)

    def mostrar_nombre(selft):
        print(selft.__nombre)

    def asignar_nombre(selft, nuevo_nombre):
        selft.__nombre = nuevo_nombre

    def asignar_edad(selft, nueva_edad):
        selft.__edad = nueva_edad
    
    def asignar_cedula(selft, nueva_cedula):
        selft.__cedula = nueva_cedula

persona = Persona("Juan", 30)
persona.mostrar_nombre()
persona.mostrar_cedula()
persona.mostrar_edad()

persona.asignar_nombre("Pedro")
persona.asignar_edad(23)
persona.asignar_cedula("23425356")
persona.mostrar_nombre()
persona.mostrar_cedula()
persona.mostrar_edad()