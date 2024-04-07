# app/routes.py
from flask import Flask, jsonify, request
from flask_cors import CORS
from .models import Animal

app = Flask(__name__)
CORS(app)

animales = []

@app.route('/animales', methods=['POST'])
def crear_animal():
    datos = request.json
    animal = Animal(**datos)
    animales.append(animal.__dict__)
    return jsonify({"mensaje": "Animal creado exitosamente"}), 201

@app.route('/animales', methods=['GET'])
def listar_animales():
    return jsonify(animales)

@app.route('/animales', methods=['GET'])
def buscar_animales():
    especie = request.args.get('especie')
    genero = request.args.get('genero')
    
    if especie:
        resultado = [animal for animal in animales if animal['especie'] == especie]
        return jsonify(resultado)
    elif genero:
        resultado = [animal for animal in animales if animal['genero'] == genero]
        return jsonify(resultado)
    else:
        return jsonify(animales)

@app.route('/animales/<int:id>', methods=['PUT'])
def actualizar_animal(id):
    for animal in animales:
        if animal['id'] == id:
            datos = request.json
            animal.update(datos)
            return jsonify({"mensaje": "Animal actualizado exitosamente"}), 200
    return jsonify({"mensaje": "Animal no encontrado"}), 404

@app.route('/animales/<int:id>', methods=['DELETE'])
def eliminar_animal(id):
    global animales
    animales = [animal for animal in animales if animal['id'] != id]
    return jsonify({"mensaje": "Animal eliminado exitosamente"}), 200
