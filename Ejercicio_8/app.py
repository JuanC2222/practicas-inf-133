from flask import Flask, request, jsonify

app = Flask(__name__)

mensajes = []
ultimo_id = 0

class Mensaje:
    def __init__(self, contenido):
        global ultimo_id
        self.id = ultimo_id + 1
        self.contenido = contenido
        self.contenido_encriptado = self.encriptar(contenido)
        ultimo_id = self.id
    
    def encriptar(self, texto):
        texto_encriptado = ""
        for caracter in texto:
            if caracter.isalpha():
                codigo = ord(caracter)
                codigo_encriptado = codigo + 3
                if caracter.islower():
                    if codigo_encriptado > ord('z'):
                        codigo_encriptado -= 26
                elif caracter.isupper():
                    if codigo_encriptado > ord('Z'):
                        codigo_encriptado -= 26
                texto_encriptado += chr(codigo_encriptado)
            else:
                texto_encriptado += caracter
        return texto_encriptado

@app.route('/mensajes', methods=['POST'])
def crear_mensaje():
    datos = request.json
    contenido = datos['contenido']
    mensaje = Mensaje(contenido)
    mensajes.append(mensaje)
    return jsonify({"mensaje": "Mensaje creado exitosamente", "id": mensaje.id}), 201

@app.route('/mensajes', methods=['GET'])
def listar_mensajes():
    return jsonify([{"id": mensaje.id, "contenido": mensaje.contenido} for mensaje in mensajes])

@app.route('/mensajes/<int:id>', methods=['GET'])
def obtener_mensaje(id):
    for mensaje in mensajes:
        if mensaje.id == id:
            return jsonify({"id": mensaje.id, "contenido": mensaje.contenido, "contenido_encriptado": mensaje.contenido_encriptado})
    return jsonify({"mensaje": "Mensaje no encontrado"}), 404

@app.route('/mensajes/<int:id>', methods=['PUT'])
def actualizar_mensaje(id):
    datos = request.json
    for mensaje in mensajes:
        if mensaje.id == id:
            mensaje.contenido = datos['contenido']
            mensaje.contenido_encriptado = mensaje.encriptar(datos['contenido'])
            return jsonify({"mensaje": "Mensaje actualizado exitosamente"}), 200
    return jsonify({"mensaje": "Mensaje no encontrado"}), 404

@app.route('/mensajes/<int:id>', methods=['DELETE'])
def eliminar_mensaje(id):
    global mensajes
    mensajes = [mensaje for mensaje in mensajes if mensaje.id != id]
    return jsonify({"mensaje": "Mensaje eliminado exitosamente"}), 200

if __name__ == '__main__':
    app.run(debug=True)
