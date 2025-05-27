"""
Un modulo en python es un archivo que contiene definiciones y declaraciones de funciones que se pueden utilizar en otros archivos.

En este caso, el archivo modulo.py contiene las funciones sumar, restar, multiplicar y dividir. Estas funciones pueden ser utilizadas en otros archivos de Python utilizando la instrucción import. Por ejemplo, si se quiere utilizar la función sumar en otro archivo, se puede hacer lo siguiente:

un paquete en python permite coleccionar o agrupar un conjunto de modulos relacionados
"""

import math
import json
import datetime
from operaciones import suma as s, resta as r, multiplicacion as m, division as d

print("Suma desde el paquete operaciones ", s.suma(5, 10)) #Imprime 15
print("Multiplicacion desde el paquete operaciones ", m.multiplicacion(5, 10)) #Imprime 50

#ejemplos de math
print(math.pi) #Imprime el numero pi
print(math.sqrt(16)) #Imprime la raiz cuadrada 
print(math.pow(2, 3)) #Imprime 2 la potencia 3
print(math.floor(2.5)) #Imprime el entero mas bajo
print(math.ceil(2.5)) #Imprime el entero mas alto
print(math.log(10)) #Imprime el logaritmo natural
print(math.factorial(5)) #Imprime el factorial
print(math.sin(math.pi/2)) #Imprime el seno +

json.dumps({"nombre":"Juan", "edad":30}) #Covierte un diccionario a una cadena json
json.loads('{"nombre":"Juan", "edad":30}') #Convierte una cadena json a un diccionario

print(datetime.date.today()) #Imprime la fecha actual
print(datetime.datetime.now()) #Imprime la fecha y hora actual
print(datetime.datetime.now().strftime("%d/%m/%Y")) #Imprime la hora actual en formato dd/mm/aaaa

ahora = datetime.datetime.now()
print(ahora.year) #Imprime el año
print(ahora.month) #Imprime el mes
print(ahora.day) #Imprime el dia
print(ahora.hour) #Imprime la hora

