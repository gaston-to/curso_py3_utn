# crea una clase que instancia un servidor

import socket

class MiServer:
    """
    Clase que instancia un servidor
    """
    
    def __init__(self, dir, entrada):
        """
        Inicializa el servidor con la dirección y el puerto de entrada
        """
        self.dir = dir
        self.entrada = entrada
        self.servidor = None
        
    def lanzar_servidor(self, numero):
        """
        Lanza el servidor
        """
        self.servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # reusar puerto
        self.servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            self.servidor.bind((self.dir, self.entrada))
            self.servidor.listen(numero)
            print(f"Servidor lanzado en {self.dir}:{self.entrada}")
            while True:
                print("Esperando por cliente ...")
                client, dir_cl = self.servidor.accept()
                print(f"Conexión aceptada de {dir_cl}")
                data = client.recv(1024)
                print(f"Se recibió {data}, tipo de info {type(data)}")
                client.send(f"Recibido: {data.decode('UTF-8')}".encode("UTF-8"))
                client.close()
        except socket.error as e:
            print(f"Error de socket: {e}")
        except KeyboardInterrupt:
            print("Servidor apagado")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if self.servidor is not None:
                self.servidor.close()
                print("Servidor cerrado")
        
if __name__ == '__main__':
    serv = MiServer('localhost', 9999)
    serv.lanzar_servidor(5)
