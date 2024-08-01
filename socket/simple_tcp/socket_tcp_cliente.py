# Lado del cliente
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Conectar al servidor
try:
    client.connect(('localhost', 9000))
    print("Conexión establecida con el servidor")
except ConnectionRefusedError:
    print("No se pudo establecer conexión con el servidor")
    exit()

# Enviar datos al servidor
client.send("Hola servidor".encode('utf-8'))

# Recibir respuesta del servidor
response = client.recv(1024)
print(f"Respuesta del servidor: {response.decode('utf-8')}")

# Cerrar conexión
client.close()
