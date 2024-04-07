from flask import Flask, request, jsonify

app = Flask(__name__)

pacientes = [
    {
        "CI": "1234567",
        "nombre": "Juan",
        "apellido": "Perez",
        "edad": 35,
        "genero": "masculino",
        "diagnostico": "Diabetes",
        "doctor": "Pedro Pérez"
    },
    {
        "CI": "7654321",
        "nombre": "Maria",
        "apellido": "Gomez",
        "edad": 40,
        "genero": "femenino",
        "diagnostico": "Hipertensión",
        "doctor": "Ana García"
    }
]

@app.route('/pacientes', methods=['POST'])
def crear_paciente():
    datos = request.json
    pacientes.append(datos)
    return jsonify({"mensaje": "Paciente creado exitosamente"}), 201

@app.route('/pacientes', methods=['GET'])
def listar_pacientes():
    return jsonify(pacientes)

@app.route('/pacientes/<ci>', methods=['GET'])
def obtener_paciente(ci):
    for paciente in pacientes:
        if paciente['CI'] == ci:
            return jsonify(paciente)
    return jsonify({"mensaje": "Paciente no encontrado"}), 404

@app.route('/pacientes', methods=['GET'])
def buscar_pacientes():
    diagnostico = request.args.get('diagnostico')
    if diagnostico:
        return jsonify([paciente for paciente in pacientes if paciente['diagnostico'] == diagnostico])
    doctor = request.args.get('doctor')
    if doctor:
        return jsonify([paciente for paciente in pacientes if paciente['doctor'] == doctor])
    return jsonify(pacientes)

@app.route('/pacientes/<ci>', methods=['PUT'])
def actualizar_paciente(ci):
    for paciente in pacientes:
        if paciente['CI'] == ci:
            datos = request.json
            paciente.update(datos)
            return jsonify({"mensaje": "Paciente actualizado exitosamente"}), 200
    return jsonify({"mensaje": "Paciente no encontrado"}), 404

@app.route('/pacientes/<ci>', methods=['DELETE'])
def eliminar_paciente(ci):
    global pacientes
    pacientes = [paciente for paciente in pacientes if paciente['CI'] != ci]
    return jsonify({"mensaje": "Paciente eliminado exitosamente"}), 200

if __name__ == '__main__':
    app.run(debug=True)
