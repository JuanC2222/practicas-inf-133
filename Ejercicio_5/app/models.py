# app/models.py
class Animal:
    def __init__(self, id, nombre, especie, genero, edad, peso):
        self.id = id
        self.nombre = nombre
        self.especie = especie
        self.genero = genero
        self.edad = edad
        self.peso = peso
