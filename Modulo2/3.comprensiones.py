
"""
Comprensiones de dolecciones
"""

#Compresion de listas
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cuadrados = [numero**2 for numero in numeros]
print(cuadrados)

#Filtros de comprensiones
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

#Coversion de mayusculas en una lista
palabras = ["Hola", "mundo", "python"]
print([palabra.upper() for palabra in palabras])

#Comprension de diccionarios
diccionario = {i: i**2 for i in range(1, 6)}
print(diccionario)
print(diccionario.keys())
print(diccionario.values())
print(diccionario.items())

#filtrar y transfromar un diccionario
diccionario = {i: i**2 for i in range(1, 6) if i % 2 == 0}
print(diccionario)


palabras = ["Hola", "mundo", "python"]
longitudes = {palabra: len(palabra) for palabra in palabras}
print(longitudes)
print({len(palabra) for palabra in palabras})