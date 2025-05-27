"""
Las clases y metodos abstractos son una caracteristisca importe en la programación orientada a objetos
(POO). En python , las clases abstractas permiten definir una intterfaz común para un grupo de clases dericadas,
asegurando que ciertas metodologias sean implementadas por todas las subclases debe implementar los métodos abstractos definidos en la clase base
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass

    @abstractmethod
    def moverse(self):
        pass

class Perro(Animal):
    def sonido(self):
        return "Guau!"
    def moverse(self):
        return "Camina en 4 patas"
    
class Gato(Animal):
    def sonido(self):
        return "Miau!"
    def moverse(self):
        return "Camina en 4 patas"
    
perro=Perro()
print(perro.sonido())
print(perro.moverse())

gato=Gato()
print(gato.sonido())
print(gato.moverse())