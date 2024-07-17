'''
Muestra cómo se puede sobreescribir el método __getattr__ para interceptar 
la lectura de un atributo
'''

class MiClase:
    def __init__(self, mail, nombre):
        self._mail = mail
        self._nombre = nombre

    def __getattr__(self, atributo):
        if atributo == 'mail':
            return 'No tienes permiso para leer el mail'
        elif atributo == 'nombre':
            return f'El cliente es {self._nombre}'
        else:
            raise AttributeError(f'El atributo {atributo} no existe')
        
objeto = MiClase('juanlo', 'Juan López')
print(objeto.mail) # No tienes permiso para leer el mail
print(objeto.nombre) # El cliente es Juan López
print(objeto.edad)  # AttributeError: El atributo edad no existe