"""
La programación orientada a objetos es un paradigma de programación que permite crear objetod y trabajar con ellos
En python, la programación orientada a objetos de implementa mediante clases y objetos
Las clases son plantillas para crear objetos, y los objetos son instancias de las clases
En python, todas las clases heredan de la clase object
"""

class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print("Hola, mi nombre es", self.nombre, self.apellido)

#Instanciar un objeto de la clase Usuario
usuario = Usuario("Juan", "Perez")
usuario2 = Usuario("Maria", "Gomez")
usuario3 = Usuario("Pedro", "Gonzalez")

#accedo a los atributos del objeto
print(usuario.nombre, usuario.apellido)
print(usuario2.nombre, usuario2.apellido)
print(usuario3.nombre, usuario3.apellido)

#modifiar objeto

usuario.nombre = "Jose"
usuario.apellido = "Gomez"

print(usuario.nombre, usuario.apellido)

"""
Definir una clase para factura
"""

class Factura:
    def __init__(self, decripcion, iva, importe):
        self.decripcion = decripcion
        self.iva = iva
        self.importe = importe

    def imprimir(self):
        print("Factura", self.decripcion, self.iva, self.importe)