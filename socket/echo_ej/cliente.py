import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('localhost', 12345))
cliente.send(b'Hola, servidor')
respuesta = cliente.recv(1024)
print('Respuesta del servidor:', respuesta.decode())
cliente.close()
