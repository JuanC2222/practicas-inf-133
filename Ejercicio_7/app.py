from flask import Flask, request, jsonify
from partida import Partida

app = Flask(__name__)
partidas_singleton = Partida()

@app.route('/partidas', methods=['POST'])
def crear_partida():
    datos = request.json
    partidas_singleton.crear_partida(datos['elemento'])
    return jsonify({"mensaje": "Partida creada exitosamente"}), 201

@app.route('/partidas', methods=['GET'])
def listar_partidas():
    return jsonify(partidas_singleton.listar_partidas())

@app.route('/partidas/perdidas', methods=['GET'])
def listar_partidas_perdidas():
    return jsonify(partidas_singleton.listar_partidas_por_resultado("perdió"))

@app.route('/partidas/ganadas', methods=['GET'])
def listar_partidas_ganadas():
    return jsonify(partidas_singleton.listar_partidas_por_resultado("ganó"))

if __name__ == '__main__':
    app.run(debug=True)
