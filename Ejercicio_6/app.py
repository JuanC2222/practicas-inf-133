from flask import Flask, request, jsonify
from animal import animales
from animal_factory import AnimalFactory

app = Flask(__name__)

@app.route('/animales', methods=['POST'])
def crear_animal():
    datos = request.json
    animal = AnimalFactory.create_animal(**datos)
    animales.append(animal)
    return jsonify({"mensaje": "Animal creado exitosamente"}), 201

@app.route('/animales', methods=['GET'])
def listar_animales():
    return jsonify([animal.__dict__ for animal in animales])

@app.route('/animales/especie/<especie>', methods=['GET'])
def buscar_por_especie(especie):
    animales_especie = [animal.__dict__ for animal in animales if animal.especie == especie]
    return jsonify(animales_especie)

@app.route('/animales/genero/<genero>', methods=['GET'])
def buscar_por_genero(genero):
    animales_genero = [animal.__dict__ for animal in animales if animal.genero == genero]
    return jsonify(animales_genero)

@app.route('/animales/<int:id>', methods=['PUT'])
def actualizar_animal(id):
    for animal in animales:
        if animal.id == id:
            datos = request.json
            animal.nombre = datos['nombre']
            animal.especie = datos['especie']
            animal.genero = datos['genero']
            animal.edad = datos['edad']
            animal.peso = datos['peso']
            return jsonify({"mensaje": "Animal actualizado exitosamente"})
    return jsonify({"mensaje": "Animal no encontrado"}), 404

@app.route('/animales/<int:id>', methods=['DELETE'])
def eliminar_animal(id):
    global animales
    animales = [animal for animal in animales if animal.id != id]
    return jsonify({"mensaje": "Animal eliminado exitosamente"})

if __name__ == '__main__':
    app.run(debug=True)
