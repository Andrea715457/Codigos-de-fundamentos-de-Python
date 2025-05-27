"""
Variables: Represnetacin simbolica de algun elemento
"""

#Ejemplos
variable = 10
nombre = "Juan"
edad = 30
es_estudiante = True

#nomenclarura de variables
"""
Camel case: nombreEstudiante
Snake case: nombre_estudiante, _nombre_estudiante
pescal case: NombreEstudiante
lower case: nombreestudiante
UPPER case: NOMBREESTUDIANTE
snake Case uppercase: NOMBRE_ ESTUDIANTE
"""

#ejemplo de representación de variables
valor_hora = 100
cantidad_hora = 2
salario = valor_hora + cantidad_hora
print(salario)

#tipos de datos
#string
nombre = "Juan"
#int
edad = 30
#float
estatura = 1.75
#boolean
es_estudiante = True
tiene_trabajo = False

print(nombre)

apellido = input("Ingrese su apellido: ")
print(apellido)

#Siempre que ingrese algo por telcado es un string

print(type(apellido))

#ejercicio: Ingresar dos numeros por la consola y sumarlos

primer_numero = int(input("Ingrese un numero: "))
segundo_numero = int(input("Ingrese un numero: "))
resultado = int(primer_numero) + int(segundo_numero)
print(resultado)

numero = "hola"
print(type(numero))
numero = 10
print(type(numero))
print(numero)