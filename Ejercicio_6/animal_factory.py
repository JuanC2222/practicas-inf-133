from animal import Animal

class AnimalFactory:
    @staticmethod
    def create_animal(id, nombre, especie, genero, edad, peso):
        return Animal(id, nombre, especie, genero, edad, peso)
