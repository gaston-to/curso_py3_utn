# crea una clase que instancia un servidor

import socket

class MiServer():
    
    def __init__(self, dir, entrada):
        self.dir = dir
        self.entrada = entrada
        
    def lanzar_servidor(self, numero):
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # reusar puerto
        servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            servidor.bind((self.dir, self.entrada))
            servidor.listen(numero)
            print("Esperando por cliente ...")
            client, dir_cl = servidor.accept()
            print(f"Conexión aceptada de {client} desde {dir_cl}")
            data = client.recv(1024)
            print(f"se recibió {data}, tipo de info {data.__class__}")
            client.send(f"Recibido: {data}".encode("UTF-8"))
            client.close()
        except Exception as e:
            print(f"Error: {e}")
        
if __name__ == '__main__':
    serv = MiServer('localhost', 9999)
    serv.lanzar_servidor(5)
