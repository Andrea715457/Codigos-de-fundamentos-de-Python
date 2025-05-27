#Operadores logicos, aritmeticos y boleanos

#operadores aritmeticos
suma = 5 + 5
resta = 5 - 5
multiplicacion = 5 * 5
division = 5 / 5
modulo = 5 % 5 #el residuo de una division 
exponente = 5 ** 2
division_entera = 5 // 2 #redondear una cifa a entero

print(suma, resta, multiplicacion, division, modulo, exponente, division_entera)

#operadores relacionales

mayor_que = 5 > 5
menor_que = 1 < 5
mayor_igual = 5 >= 5
menor_igual = 5 <= 5
igual = 5 == 5
diferente = 5 != 5

print(mayor_que, menor_que, mayor_igual, menor_igual, igual, diferente)

#operadores booleanos
and_logico = True and False
or_logico = True or False
print (and_logico, or_logico)

#ejemplo de usuarios y contraseñas
user = True
password = True
print("Inicio de sesión ", user and password)

#ejerccicio
a = 10
b = 5
c = 7
resultado2 = (a + b) * c
resultado = (a > b) and (a > c)
print(resultado)
print(resultado2)

#ejercicio

es_adulto = True
es_pensionado = True
es_adulto = not es_adulto
print("Es adulto y es pensionado ", es_adulto and es_pensionado)