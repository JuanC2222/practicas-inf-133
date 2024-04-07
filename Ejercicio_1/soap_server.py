from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

# Define la función del servicio para saludar
def saludar(nombre):
    return "¡Hola, {}!".format(nombre)

# Define las funciones del servicio para las operaciones matemáticas
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero."
    return a / b

# Creamos la ruta del servidor SOAP
dispatcher = SoapDispatcher(
    "ejemplo-soap-server",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns=True,
)

# Registramos los servicios
dispatcher.register_function("Sumar", sumar, returns={"resultado": int}, args={"a": int, "b": int})
dispatcher.register_function("Restar", restar, returns={"resultado": int}, args={"a": int, "b": int})
dispatcher.register_function("Multiplicar", multiplicar, returns={"resultado": int}, args={"a": int, "b": int})
dispatcher.register_function("Dividir", dividir, returns={"resultado": float}, args={"a": int, "b": int})

# Iniciamos el servidor HTTP
server = HTTPServer(("0.0.0.0", 8000), SOAPHandler)
server.dispatcher = dispatcher
print("Servidor SOAP iniciado en http://localhost:8000/")
server.serve_forever()
