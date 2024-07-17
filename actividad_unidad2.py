
class Descriptor:

    def __get__(self, instancia, clase):
        print('Accediendo al atributo')
        return instancia._nombre

    def __set__(self, instancia, valor):
        print('Modificando el atributo')
        instancia._nombre = valor

    def __delete__(self, instancia):
        print('Eliminando el atributo')
        del instancia._nombre

class DescriptorSalario:

    def __get__(self, instancia, clase):
        print('Accediendo al atributo')
        return instancia._salario

    def __set__(self, instancia, valor):
        print('Modificando el atributo')
        
        if valor < 0:
            raise ValueError('El salario no puede ser negativo')
        else:
            instancia._salario = valor

    def __delete__(self, instancia):
        print('Eliminando el atributo')
        del instancia._salario

class DescriptorEdad:

    def __get__(self, instancia, clase):
        print('Accediendo al atributo')
        return instancia._edad

    def __set__(self, instancia, valor):
        print('Modificando el atributo')
        
        if valor < 18:
            raise ValueError('La edad no puede ser menor a 18 años')
        elif valor > 65:
            raise ValueError('El empleado debe jubilarse')
        else:
            instancia._edad = valor

    def __delete__(self, instancia):
        print('Eliminando el atributo')
        del instancia._edad

class Empleados:

    nombre = Descriptor()
    salario = DescriptorSalario()

    def __init__(self, nombre, edad, salario):
        self._nombre = nombre

        if salario < 0:
            raise ValueError('El salario no puede ser negativo')
        else:
            self._salario = salario

        if edad < 18:
            raise ValueError('La edad no puede ser menor a 18 años')
        elif edad > 65:
            raise ValueError('El empleado debe jubilarse')
        else:
            self._edad = edad

emp1 = Empleados('Juan', 65, 1000)
print(emp1.nombre)
print(emp1.salario)

emp1.salario = -5