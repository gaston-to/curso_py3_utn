import socket

# crear socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# enlazar el socket a una dirección y puerto
server.bind(('localhost', 9000))

# establecer tiempo de espera en segundos
server.settimeout(60)

try:
    # escuchar conexiones entrantes
    server.listen(1)
    print("Servidor escuchando en el puerto 9000")

    # aceptar conexiones entrantes
    client_socket, client_address = server.accept()
    print(f"Conexión aceptada desde {client_address}")

    # Recibir datos del cliente
    data = client_socket.recv(1024)
    print(f"Datos recibidos: {data.decode('utf-8')}")

    # Enviar respuesta al cliente
    client_socket.send("Hola cliente - datos recibidos".encode('utf-8'))

    # cerrar conexión
    client_socket.close()

except socket.timeout:
    print("Tiempo de espera agotado. Cerrando el servidor.")

finally:
    server.close()
