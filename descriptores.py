class AccederMail:

    def __get__(self, instancia, clase):
        return instancia._mail + '.net'

    def __set__(self, instancia, valor):
        if '@' not in valor:
            raise ValueError('El correo debe contener un @')
        print('Modificando el correo')
        instancia._mail = valor


class Descriptor:
    def __get__(self, instancia, clase):
        print('Accediendo al atributo')
        return instancia._atributo

    def __set__(self, instancia, valor):
        print('Modificando el atributo')
        instancia._atributo = valor

    def __delete__(self, instancia):
        print('Eliminando el atributo')
        del instancia._atributo

class MiClase:
    atributo = Descriptor()
    mail = AccederMail()

    def __init__(self, valor, _mail):
        self._atributo = valor
        self._mail = _mail

obj1 = MiClase('Juan', 'juan@gmail')
print(obj1.atributo)  # Salida: 'Accediendo al atributo' Juan
print(obj1._mail)  # Salida: 'juan@gmail'
print(obj1.mail)  # Salida: '
obj1.atributo = 'Pedro'
print('---'*2)
print(obj1.atributo) 

print('\n')
obj1.mail = 'pedro@gmail' # Salida: 'Modificando el correo'
print(obj1.mail)
