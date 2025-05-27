"""
las funciones en python son bloques de codigo reutilizabre que realizan una tarea espeficica
"""

#Declarar una funcion
def saludo1():
    print("Hola mundo")

#Llamar a la funcion
saludo1()

#Declarar una funcion
def saludo2(mensaje):
    print(mensaje)

#Llamar a la funcion
saludo2("Hola, como estas?")

#Funcion sin parametros y con retorno
def mensaje():
    return "Hola mundo"

#funciones sin parametros y sin retorno
def saludo3():
    print("Hola mundo")

#Funciones con parametro y con retorno
def suma(numer1,numero2):
    resultado = numer1 + numero2
    return resultado

mensaje()
saludo3()
print(suma(5, 10))

#funciones con parametros por defectos
def resta(numero1,numero2=2):
    resultado = numero1 - numero2
    return resultado

print(resta(5, 10))
print(resta(5))

def mostrar_mensaje(men="Hola mundo"):
    return men

print(mostrar_mensaje("Hola grupo de python"))
print(mostrar_mensaje())

def calcular_area(base, altura):
    area = base * altura
    return area

print(calcular_area(5, 10))
print(calcular_area(6, 5))