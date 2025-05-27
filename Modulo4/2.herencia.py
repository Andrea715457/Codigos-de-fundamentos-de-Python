"""
Herencia es un concepto ene lq ue una clase puede heredar atributos y metodos de otra clase.
Esto permite  reutilizar codigo y crear clases mas especificas a partir de uan clase base.
"""

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        raise NotImplementedError("El metodo arrancar debe ser implementado en la subclase")

    def detener(self):
       raise NotImplementedError("El metodo arrancar debe ser implementado en la subclase")

class Carro(Vehiculo):
    def __init__(self, marca, modelo, tipo_combustible):
        super().__init__(marca, modelo)
        self.tipo_combustible = tipo_combustible
    
    def arrancar(self):
        print("El vehiculo", self.marca, self.modelo, "ha arrancado")

    def detener(self):
        print("El vehiculo", self.marca, self.modelo, "ha detenido")


class Moto(Vehiculo):
    def __init__(self, marca, modelo, tipo_motor):
        super().__init__(marca, modelo)
        self.tipo_motor = tipo_motor
    
    def arrancar(self):
        print("El vehiculo", self.marca, self.modelo, "ha arrancado")

    def detener(self):
        print("El vehiculo", self.marca, self.modelo, "ha detenido")


carro1 = Carro("Toyota", "Corolla", "Gasolina")
carro1.arrancar()
carro1.detener()

moto1 = Moto("Honda", "CBR", "4 tiempos")
moto1.arrancar()
moto1.detener()