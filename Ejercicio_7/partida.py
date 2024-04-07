import random

class Partida:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.partidas = []

    def crear_partida(self, elemento_jugador):
        id_partida = len(self.partidas) + 1
        elementos = ["piedra", "papel", "tijera"]
        elemento_servidor = random.choice(elementos)
        resultado = self.calcular_resultado(elemento_jugador, elemento_servidor)
        self.partidas.append({
            "id": id_partida,
            "elemento": elemento_jugador,
            "elemento_servidor": elemento_servidor,
            "resultado": resultado
        })

    def calcular_resultado(self, elemento_jugador, elemento_servidor):
        if elemento_jugador == elemento_servidor:
            return "empató"
        if (elemento_jugador == "piedra" and elemento_servidor == "tijera") or \
           (elemento_jugador == "tijera" and elemento_servidor == "papel") or \
           (elemento_jugador == "papel" and elemento_servidor == "piedra"):
            return "ganó"
        return "perdió"

    def listar_partidas(self):
        return self.partidas

    def listar_partidas_por_resultado(self, resultado):
        return [partida for partida in self.partidas if partida["resultado"] == resultado]
