import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(5)

while True:
    client, addr = server.accept()
    print('Conexión establecida con', addr)
    data = client.recv(1024)
    print('Recibido:', data.decode())
    client.send(data)
    client.close()

server.close()
    