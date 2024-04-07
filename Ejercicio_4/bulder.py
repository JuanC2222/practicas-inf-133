from flask import Flask, request, jsonify

app = Flask(__name__)

pacientes = []

class Paciente:
    def __init__(self, ci, nombre, apellido, edad, genero, diagnostico, doctor):
        self.ci = ci
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero
        self.diagnostico = diagnostico
        self.doctor = doctor

class PacienteBuilder:
    def __init__(self):
        self.ci = None
        self.nombre = None
        self.apellido = None
        self.edad = None
        self.genero = None
        self.diagnostico = None
        self.doctor = None

    def set_ci(self, ci):
        self.ci = ci
        return self

    def set_nombre(self, nombre):
        self.nombre = nombre
        return self

    def set_apellido(self, apellido):
        self.apellido = apellido
        return self

    def set_edad(self, edad):
        self.edad = edad
        return self

    def set_genero(self, genero):
        self.genero = genero
        return self

    def set_diagnostico(self, diagnostico):
        self.diagnostico = diagnostico
        return self

    def set_doctor(self, doctor):
        self.doctor = doctor
        return self

    def build(self):
        return Paciente(
            self.ci,
            self.nombre,
            self.apellido,
            self.edad,
            self.genero,
            self.diagnostico,
            self.doctor
        )

@app.route('/pacientes', methods=['POST'])
def crear_paciente():
    datos = request.json
    paciente_builder = PacienteBuilder()
    paciente = paciente_builder\
        .set_ci(datos['ci'])\
        .set_nombre(datos['nombre'])\
        .set_apellido(datos['apellido'])\
        .set_edad(datos['edad'])\
        .set_genero(datos['genero'])\
        .set_diagnostico(datos['diagnostico'])\
        .set_doctor(datos['doctor'])\
        .build()
    pacientes.append(paciente)
    return jsonify({"mensaje": "Paciente creado exitosamente"}), 201

@app.route('/pacientes', methods=['GET'])
def listar_pacientes():
    return jsonify([paciente.__dict__ for paciente in pacientes])

@app.route('/pacientes/<ci>', methods=['GET'])
def obtener_paciente(ci):
    for paciente in pacientes:
        if paciente.ci == ci:
            return jsonify(paciente.__dict__)
    return jsonify({"mensaje": "Paciente no encontrado"}), 404

@app.route('/pacientes', methods=['GET'])
def buscar_pacientes():
    diagnostico = request.args.get('diagnostico')
    doctor = request.args.get('doctor')

    if diagnostico:
        pacientes_filtrados = [paciente.__dict__ for paciente in pacientes if paciente.diagnostico == diagnostico]
        return jsonify(pacientes_filtrados)
    elif doctor:
        pacientes_filtrados = [paciente.__dict__ for paciente in pacientes if paciente.doctor == doctor]
        return jsonify(pacientes_filtrados)
    else:
        return jsonify([paciente.__dict__ for paciente in pacientes])

@app.route('/pacientes/<ci>', methods=['PUT'])
def actualizar_paciente(ci):
    datos = request.json
    for paciente in pacientes:
        if paciente.ci == ci:
            paciente.nombre = datos['nombre']
            paciente.apellido = datos['apellido']
            paciente.edad = datos['edad']
            paciente.genero = datos['genero']
            paciente.diagnostico = datos['diagnostico']
            paciente.doctor = datos['doctor']
            return jsonify({"mensaje": "Paciente actualizado exitosamente"}), 200
    return jsonify({"mensaje": "Paciente no encontrado"}), 404

@app.route('/pacientes/<ci>', methods=['DELETE'])
def eliminar_paciente(ci):
    global pacientes
    pacientes = [paciente for paciente in pacientes if paciente.ci != ci]
    return jsonify({"mensaje": "Paciente eliminado exitosamente"}), 200

if __name__ == '__main__':
    app.run(debug=True)
