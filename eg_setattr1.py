'''
De como se emplea __setattr__ para interceptar la asignación de atributos
'''

class MiCLase:

    def __init__(self, nombre):
        self._nombre = nombre

    
    def __getattr__(self, atributo):
        if atributo == 'nombre':
            return self._nombre
        else:
            raise AttributeError(f'El atributo {atributo} no existe')

    def __setattr__(self, atributo, valor):

        if atributo == 'nombre':
            atributo = '_nombre'
        
        self.__dict__[atributo] = valor
    

objeto = MiCLase('Olivia Newton')
print(objeto.nombre) # Olivia Newton
objeto.nombre = 'Olivia Newton-John'
print(objeto.nombre) # Olivia Newton-John
