class Usuario:
    def __init__(self, nombre, correo, contraseña):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña

    def saludo(self):
        return f"Nombre: {self.nombre}, Correo: {self.correo}, Contraseña: {self.contraseña}"
