"""
Diccionarios y conjuntos
Diccionarios: clave:valor
"""

#Crear diccionario
my_dic = {
    "Nombre": "Andrea",
    "Edad": 30,
    "Piudad": "Bucaramanga",
    "Pais": "Colombia",
    "Telefonos": ["3044818596", "3204163487"],
    "Correos": {
        "Gmail": ["Andrea715457@gmail.com"],
        "hotmail": ["Andrea715457@outlook.com"]
    }
}

#Acceder a los elementos del diccionario
print(my_dic["Nombre"])
print(my_dic["Edad"])
print(my_dic["Telefonos"])
print(my_dic["Correos"])
print(my_dic["Correos"]["Gmail"])

#traer las lleves
print(my_dic.keys())
print(my_dic.values())
print(my_dic.items())
print(len(my_dic))
print(my_dic.get("Edad"))

#modidicar el diccionario
my_dic["Edad"] = 31
print(my_dic)
my_dic.update({"Edad": 23})
print(my_dic)
my_dic.pop("Edad")
print(my_dic)
my_dic.clear()
print(my_dic)


"""
Conjuntos: coleccion desordebad de elementos unicos
"""
#ejemplo de conjuntos

conjunto_a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
conjunto_b = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
print(conjunto_a)
print(conjunto_b)
print(conjunto_a.union(conjunto_b))
print(conjunto_a.intersection(conjunto_b))
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))
print(conjunto_a.symmetric_difference(conjunto_b))

#Recorrer conjuntos
for elemento in conjunto_a:
    print(elemento)

my_dic = {
    "Nombre": "Andrea",
    "Edad": 30,
    "Piudad": "Bucaramanga",
    "Pais": "Colombia",
    "Telefonos": ["3044818596", "3204163487"],
    "Correos": {
        "Gmail": ["Andrea715457@gmail.com"],
        "hotmail": ["Andrea715457@outlook.com"]
    }
}

#recorrer diccionario
for clave, valor in my_dic.items():
    print(f"{clave} : {valor}")