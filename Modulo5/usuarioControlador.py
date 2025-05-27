from usuario import Usuario
from flask import jsonify

class UssuarioControlador:
    def __init__(self):
        self.usuarios = [
            Usuario("Juan", "juan@gmail.com", "contraseña123"),
            Usuario("María", "maria@gmail.com", "contraseña456"),
            Usuario("Pedro", "pedro@gmail.com", "contraseña789")
        ]

    def obtener_usuarios(self):
        usuarios = [usuarios.__dict__ for usuario in usuarios]
        return jsonify(usuarios)
    
    def buscar_usuario(self, id):
        for usuario in self.usuarios:
            if usuario.id == id:
                return jsonify(usuario.__dict__)
        return jsonify({"error": "Usuario no encontrado"}), 404

    def crear_usuario(self, id, nombre, correo, contraseña):
        nuevo_usuario = Usuario(id, nombre, correo, contraseña)
        self.usuarios.append(nuevo_usuario)

    def actualizar_usuario(self, id):
        for usuario in self.usuarios:
            if usuario.id == id:
               pass

    def eliminar_usuario(self, id):
        for usuario in self.usuarios:
            if usuario.id == id:
                self.usuarios.remove(usuario)