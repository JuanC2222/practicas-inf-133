from zeep import Client
client = Client('http://localhost:8000')

a = 5; b =5;

# Sumar
result_suma = client.service.Sumar(a, b)
print("Suma:", result_suma)

# Restar
result_resta = client.service.Restar(a, b)
print("Resta:", result_resta)

# Multiplicar
result_multiplicacion = client.service.Multiplicar(a, b)
print("Multiplicación:", result_multiplicacion)

# Dividir
result_division = client.service.Dividir(a, b)
print("División:", result_division)
