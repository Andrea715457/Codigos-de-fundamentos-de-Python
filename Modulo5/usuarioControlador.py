from usuario import Usuario
from flask import jsonify

class UsuarioControlador:
    def __init__(self):
        self.usuarios = [
            Usuario(1, "Juan", "juan@gmail.com", "contraseña123"),
            Usuario(2, "María", "maria@gmail.com", "contraseña456"),
            Usuario(3, "Pedro", "pedro@gmail.com", "contraseña789")
        ]

    def obtener_usuarios(self):
        usuarios = [usuario.__dict__ for usuario in self.usuarios]
        return jsonify(usuarios)
    
    def buscar_usuario(self, id):
        for usuario in self.usuarios:
            if usuario.id == id:
                return jsonify(usuario.__dict__)
        return jsonify({"error": "Usuario no encontrado"}), 404

    def crear_usuario(self, usuario_entrada):
        nuevo_usuario = Usuario(id, usuario_entrada["nombre"], usuario_entrada["correo"], usuario_entrada["contraseña"])
        self.usuarios.append(nuevo_usuario)
        return jsonify(nuevo_usuario.__dict__)

    def actualizar_usuario(self, id, usuario_actualizado):
        for usuario in self.usuarios:
            if usuario.id == id:
               actualizar_usuario = Usuario(id, usuario_actualizado["nombre"], usuario_actualizado["correo"], usuario_actualizado["contraseña"])
               return jsonify(actualizar_usuario.__dict__)
            return jsonify({"error": "Usuario no encontrado"}), 404
        
    def eliminar_usuario(self, id):
        for usuario in self.usuarios:
            if usuario.id == id:
                nombre = usuario.nombre
                self.usuarios.remove(usuario)
                return jsonify({"mensaje": f"Usuario {nombre} eliminado correctamente"})
            return jsonify({"error": "Usuario no encontrado"}), 404
