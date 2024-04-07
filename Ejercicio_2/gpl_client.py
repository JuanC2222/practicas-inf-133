import requests

# Definir la URL del servidor GraphQL
url = 'http://localhost:8000/graphql'

# Definir la consulta GraphQL para obtener la lista de todas las plantas
query_lista_plantas = """
{
    plantas {
        nombreComun
        especie
        edad
        altura
        frutos
    }
}
"""

# Solicitud POST al servidor GraphQL para obtener la lista de todas las plantas
response = requests.post(url, json={'query': query_lista_plantas})
print(response.text)

# Definir la consulta GraphQL con parámetros para obtener información de una planta por su ID
query_planta_por_id = """
{
    plantaPorId(id: 2) {
        nombreComun
        especie
        edad
        altura
        frutos
    }
}
"""

# Solicitud POST al servidor GraphQL para obtener información de una planta por su ID
response = requests.post(url, json={'query': query_planta_por_id})
print(response.text)

# Definir la consulta GraphQL para crear una nueva planta
query_crear_planta = """
mutation {
    crearPlanta(
        nombreComun: "Rosa"
        especie: "Rosa gallica"
        edad: 12
        altura: 50
        frutos: false
    ) {
        planta {
            id
            nombreComun
            especie
            edad
            altura
            frutos
        }
    }
}
"""

# Solicitud POST al servidor GraphQL para crear una nueva planta
response = requests.post(url, json={'query': query_crear_planta})
print(response.text)

# Definir la consulta GraphQL para eliminar una planta por su ID
query_eliminar_planta = """
mutation {
    eliminarPlanta(id: 3) {
        planta {
            id
            nombreComun
            especie
            edad
            altura
            frutos
        }
    }
}
"""

# Solicitud POST al servidor GraphQL para eliminar una planta por su ID
response = requests.post(url, json={'query': query_eliminar_planta})
print(response.text)

# Lista de todas las plantas después de la eliminación
response = requests.post(url, json={'query': query_lista_plantas})
print(response.text)
