"""
Colecciones en python 
> listas y las tuplas
"""

lista = [1, 2, 3, 4, 5]
lista_elementos = ["Hola", 2, True, 3.14, [1, 2, 3]]

print(lista)
print(lista_elementos)

#acceso a elementos de la lista
print(lista[0])
print(lista_elementos[1])
print(lista_elementos[4][1])
print(lista_elementos[-1])
print(lista_elementos[-1][0])
print(lista[0:3])
print(lista_elementos[1:])
print(lista_elementos[:3])
print(lista_elementos[1:4])
print(lista_elementos[1:4:2])

#modificar elementos de la lista
lista[0] = 10
print(lista)
lista[1] = 100
print(lista)
lista.insert(0, 50)
print(lista)
lista.append(60)
print(lista)
lista.extend([70, 80, 90])
print(lista)
lista.remove(100)
print(lista)
lista.pop()
print(lista)
lista.sort()
print(lista)
lista.reverse()
print(lista)
lista.clear()
print(lista)
del lista

#Tuplas en python -- son inmutables
tupla = (1, 2, 3, 4, 5)
print(tupla)
print(tupla[0])
print(tupla[1])
print(tupla[0:3])

#Manipulacion de tuplas

tupla = (1, 2, 3)
tupla = tupla + (4, 5, 6)
print(tupla)
tupla = tupla[:3] + (7, 8, 9)
print(tupla)
tupla = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla3 = tupla + tupla2
print(tupla3)

#Recorrer una lista y tupla
lista = [1, 2, 3, 4, 5]
for elemento in tupla:
    if (elemento == 3):
        break
    print(elemento)
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
    if (elemento == 3):
        break
    print(elemento)

nombre = "Andrea"
for letra in nombre:
    print(f"letra: {letra}")

nombres = ["Andrea", "Juan", "Maria", "Pedro"]
for nombre in nombres:
    print(f"nombre: {nombre}")

for nombre in nombres:
    for letra in nombre:
        print(letra, nombre, end = " - ")
