
def decorador(clase):

    class Envol:
        def __init__(self, *args):
            self.instancia = clase(*args)

        def __getattr__(self, nombre):
            print('Buscando el atributo')
            print('El atributo es:', nombre)
            return getattr(self.instancia, nombre)
        
        def __setattr__(self, nombre, valor):
            self.__dict__[nombre] = valor
            print('Modificando el atributo ' + nombre)

    return Envol    

@decorador
class Auto:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

auto = Auto('Ford', 'Fiesta')
print(auto.marca)

auto.marca = 'Chevrolet'
print(auto.marca)
