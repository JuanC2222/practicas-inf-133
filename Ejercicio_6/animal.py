from dataclasses import dataclass

@dataclass
class Animal:
    id: int
    nombre: str
    especie: str
    genero: str
    edad: int
    peso: float

animales = [
    Animal(id=1, nombre="León", especie="Panthera leo", genero="macho", edad=5, peso=200.0),
    Animal(id=2, nombre="Águila calva", especie="Haliaeetus leucocephalus", genero="hembra", edad=10, peso=6.0),
    Animal(id=3, nombre="Cocodrilo del Nilo", especie="Crocodylus niloticus", genero="macho", edad=15, peso=500.0)
]
