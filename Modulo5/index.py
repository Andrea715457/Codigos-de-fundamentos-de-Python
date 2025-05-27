from flask import Flask
from flask import jsonify
from usuarioControlador import UsuarioControlador

app = Flask(__name__)

usuarioControlador = UsuarioControlador()

@app.route('/usuarios')
def obtener_usuario():
    usuarios = usuarioControlador.obtener_usuarios()
    return usuarios
@app.route('/usuarios/<int:id>')
def obtener_usuario_id(id):
    usuario = usuarioControlador.buscar_usuario(id)
    if usuario:
        return jsonify(usuario.__dict__)
    else:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404
    
if __name__ == '__main__':
    app.run(debug=True)

