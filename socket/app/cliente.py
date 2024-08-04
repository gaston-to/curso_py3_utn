import socket

Host, Port = "localhost", 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mensaje = "Hola Servidor!"
sock.connect((Host, Port))
sock.send(mensaje.encode("UTF-8"))
recibido = sock.recv(1024)
print(recibido)
sock.close()
# ===== FIN ENVIO Y RECEPCIÓN DE DATOS =================
