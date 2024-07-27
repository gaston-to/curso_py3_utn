"""
Se desarrolla de manera genérica el patrón observador conforme a Barreto.
El mismo corresponde al esquema UML que se encuentra en Wikipedia.
"""

# Se importa la librería abc para trabajar con clases abstractas.
from abc import ABC, abstractmethod

# se define la clase abstracta Sujeto, tambien llamado Notificador.
# Esta clase es la que se encarga de notificar a los observadores.

class Sujeto(ABC):
    def __init__(self):
        self.observadores = []

    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def eliminar_observador(self, observador):
        self.observadores.remove(observador)

    def notificar_observadores(self):
        for observador in self.observadores:
            observador.actualizar(self)

    @abstractmethod
    def obtener_estado(self):
        pass

    @abstractmethod
    def establecer_estado(self, estado):
        pass

# Se define la clase abstracta Observador.
# Esta clase es la que se encarga de recibir las notificaciones del sujeto.
# En este caso, el método actualizar recibe el sujeto que lo notifica.
# Se puede agregar un argumento adicional para enviar información adicional.
# En este caso, se envía el sujeto que lo notifica.
# 

class Observador(ABC):
    @abstractmethod
    def actualizar(self, sujeto):
        pass

# Se define la clase ConcretaSujeto que hereda de Sujeto.
# Esta clase es la que se encarga de notificar a los observadores.
# En este caso, se define un estado que es un entero.
# Se define un método para obtener el estado y otro para establecer el estado.
# Se define un método para cambiar el estado y notificar a los observadores.
#   

class ConcretoSujeto(Sujeto):
    def __init__(self):
        super().__init__()
        self.estado = 0

    def obtener_estado(self):
        return self.estado

    def establecer_estado(self, estado):
        self.estado = estado

    def cambiar_estado(self, estado):
        self.estado = estado
        self.notificar_observadores()

# Se define la clase ConcretoObservador que hereda de Observador.
# Esta clase es la que se encarga de recibir las notificaciones del sujeto.
# En este caso, se define un estado que es un entero.
# Se define un método para actualizar el estado.
# 

class ConcretoObservador(Observador):
    def __init__(self):
        self.estado = 0

    def actualizar(self, sujeto):
        self.estado = sujeto.obtener_estado()
            
    def obtener_estado(self):
        return self.estado
        
# Se define la función principal main.
# En esta función se crean un sujeto y un observador.
# Se agrega el observador al sujeto.
# Se cambia el estado del sujeto y se notifica a los observadores.
# Se imprime el estado del observador.
#

def main():
    sujeto = ConcretoSujeto()
    observador = ConcretoObservador()
    sujeto.agregar_observador(observador)
    sujeto.cambiar_estado(5)
    print(observador.obtener_estado())

# Se llama a la función principal main.
#

if __name__ == "__main__":
    main()
