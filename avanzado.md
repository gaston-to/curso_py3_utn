# Python 3

## Indice

- [Python 3](#python-3)
  - [Indice](#indice)
  - [Unidad 1: Programación orientada a objetos](#unidad-1-programación-orientada-a-objetos)
    - [Lección 1: Delegación](#lección-1-delegación)
    - [Lección 2: Sobrecarga de operadores](#lección-2-sobrecarga-de-operadores)
      - [Uso de `__str__`](#uso-de-__str__)
      - [Uso de `__getitem__`](#uso-de-__getitem__)
      - [Uso de `__setitem__`](#uso-de-__setitem__)
      - [Uso de `__iter__` y `__next__`](#uso-de-__iter__-y-__next__)
    - [Lección 3: Slots](#lección-3-slots)
  - [Unidad 2: Manipulación de atributos](#unidad-2-manipulación-de-atributos)
    - [Lección 1: Creación de atributos](#lección-1-creación-de-atributos)
      - [Manejo de atributos con `property`](#manejo-de-atributos-con-property)
      - [Manejo de atributos con decoradores](#manejo-de-atributos-con-decoradores)
    - [Lección 2: Herencia de atributos](#lección-2-herencia-de-atributos)
    - [Leccion 3: Descriptor de atributos](#leccion-3-descriptor-de-atributos)
    - [Lección 4: Métodos especiales](#lección-4-métodos-especiales)
      - [Uso de `__getattr__`](#uso-de-__getattr__)
      - [Uso de `___setattr__`](#uso-de-___setattr__)
      - [Uso de `__delattr__`](#uso-de-__delattr__)
  - [Unidad 3: Decoradores](#unidad-3-decoradores)
    - [Lección 1. Función como decorador](#lección-1-función-como-decorador)
    - [Lección 2. Clase como decorador](#lección-2-clase-como-decorador)
    - [Lección 3. Decoradores de clase](#lección-3-decoradores-de-clase)
    - [Lección 4. Apilamiento de decoradores](#lección-4-apilamiento-de-decoradores)
    - [Lección 5. Decoradores con argumentos](#lección-5-decoradores-con-argumentos)
  - [Unidad 4. Patrones de Desarrollo](#unidad-4-patrones-de-desarrollo)
    - [Lección 1. Patrón Observador](#lección-1-patrón-observador)
      - [Implementación del patrón Observador en Python](#implementación-del-patrón-observador-en-python)
  - [Unidad 5: Socket](#unidad-5-socket)
    - [Lección 1. Servidor de sockets](#lección-1-servidor-de-sockets)
    - [Lección 2. Cliente de sockets](#lección-2-cliente-de-sockets)
    - [Ejemplo 1. Echo Server](#ejemplo-1-echo-server)

## Unidad 1: Programación orientada a objetos

En Python, la programación orientada a objetos (POO) es un paradigma de programación que se basa en la creación de clases y objetos para modelar y resolver problemas. En la POO, los objetos son instancias de clases que contienen atributos y métodos que definen su comportamiento y estado. Las clases son plantillas que definen la estructura y el comportamiento de los objetos, y se utilizan para crear instancias de objetos con características y comportamientos específicos. La POO en Python se basa en los conceptos de encapsulación, herencia, polimorfismo y abstracción, que permiten crear programas más modulares, reutilizables y fáciles de mantener.

En esta unidad, exploraremos los conceptos fundamentales de la programación orientada a objetos en Python, incluida la delegación, la sobrecarga de operadores, los `__slots__` y otros métodos especiales que se utilizan para personalizar el comportamiento de las clases y objetos. Aprenderemos cómo implementar estos conceptos en Python y cómo utilizarlos para crear programas más eficientes y fáciles de mantener.

### Lección 1: Delegación

Delegación en Python se refiere a la capacidad de un objeto de transferir la responsabilidad de ciertas tareas a otro objeto. Esto se logra mediante la creación de una relación de composición entre los objetos, donde uno de ellos delega ciertas operaciones al otro. La delegación puede ser útil para dividir la lógica de un programa en componentes más pequeños y reutilizables. En Python, se puede implementar la delegación utilizando la composición y llamando a los métodos del objeto delegado cuando sea necesario.
La delegación en Python se puede implementar utilizando la composición y llamando a los métodos del objeto delegado cuando sea necesario. Aquí tienes un ejemplo de pseudocódigo y código para ilustrar cómo se puede lograr esto:

Pseudocódigo:

```ps
Clase ObjetoDelegado:
    def metodo_delegado(self):
        # Lógica del método delegado

Clase ObjetoDelegador:
    def __init__(self):
        self.delegado = ObjetoDelegado()

    def metodo_delegador(self):
        # Lógica del método delegador
        self.delegado.metodo_delegado()
```

Código en Python:

```python
class ObjetoDelegado:
    def metodo_delegado(self):
        # Lógica del método delegado

class ObjetoDelegador:
    def __init__(self):
        self.delegado = ObjetoDelegado()

    def metodo_delegador(self):
        # Lógica del método delegador
        self.delegado.metodo_delegado()
```

En este ejemplo, la clase `ObjetoDelegador` tiene una instancia de la clase `ObjetoDelegado` como atributo. Cuando se llama al método `metodo_delegador` en `ObjetoDelegador`, este método a su vez llama al método `metodo_delegado` en `ObjetoDelegado`, delegando la responsabilidad de ejecutar esa parte de la lógica al objeto delegado.

### Lección 2: Sobrecarga de operadores

La sobrecarga de operadores en Python se refiere a la capacidad de una clase de definir el comportamiento de los operadores integrados de Python, como `+`, `-`, `*`, `/`, `==`, `!=`, etc. Esto se logra mediante la implementación de métodos especiales en la clase que se llaman cuando se utiliza un operador en instancias de esa clase. La sobrecarga de operadores puede ser útil para personalizar el comportamiento de los operadores en una clase y hacer que las instancias de esa clase se comporten de manera similar a los tipos de datos integrados de Python. Aquí tienes un ejemplo de pseudocódigo y código para ilustrar cómo se puede lograr esto:

Código en Python:

```python
class MiClase:
    def __init__(self, valor):
        self.valor = valor

    def __add__(self, otro):
        return self.valor + otro.valor

    def __sub__(self, otro):
        return self.valor - otro.valor
    
    def __mul__(self, otro):
        return self.valor * otro.valor

    def __truediv__(self, otro):
        return self.valor / otro.valor

    def __eq__(self, otro):
        return self.valor == otro.valor

    def __ne__(self, otro):
        return self.valor != otro.valor
```

En este ejemplo, la clase `MiClase` define los métodos especiales `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__eq__` y `__ne__` para sobrecargar los operadores `+`, `-`, `*`, `/`, `==` y `!=`, respectivamente. Cuando se utilizan estos operadores en instancias de `MiClase`, los métodos especiales correspondientes se llaman y se devuelve el resultado deseado. Esto permite personalizar el comportamiento de los operadores en la clase y hacer que las instancias de esa clase se comporten de manera similar a los tipos de datos integrados de Python.

#### Uso de `__str__`

El método `__str__` en Python se utiliza para definir cómo se debe representar una instancia de una clase como una cadena de texto. Este método se llama automáticamente cuando se utiliza la función `str()` en una instancia de la clase, o cuando se imprime la instancia directamente con `print()`. Al definir el método `__str__` en una clase, se puede personalizar la representación de la instancia como una cadena de texto, lo que puede ser útil para proporcionar información legible sobre el objeto. Aquí tienes un ejemplo de pseudocódigo y código para ilustrar cómo se puede lograr esto:

Código en Python:

```python
class MiClase:
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return f'Valor: {self.valor}'
```

Salida:

```python
objeto = MiClase(42)
print(objeto)
# Salida: Valor: 42
```

#### Uso de `__getitem__`

El método `__getitem__` en Python se utiliza para permitir el acceso a los elementos de una instancia de una clase mediante indexación, es decir, utilizando corchetes `[]`. Al definir el método `__getitem__` en una clase, se puede personalizar cómo se accede a los elementos de la instancia, lo que puede ser útil para proporcionar una interfaz similar a la de una lista o diccionario. Aquí tienes un ejemplo de pseudocódigo y código para ilustrar cómo se puede lograr esto:

Código en Python:

```python
class MiClase:
    def __init__(self, valores):
        self.valores = valores

    def __getitem__(self, indice):
        return self.valores[indice]
```

Salida:

```python
objeto = MiClase([1, 2, 3, 4, 5])
print(objeto[2])
# Salida: 3
```

En este ejemplo, la clase `MiClase` define el método `__getitem__` para permitir el acceso a los elementos de la lista `valores` mediante indexación. Cuando se accede a un elemento de la instancia de `MiClase` utilizando corchetes `[]`, se llama al método `__getitem__` y se devuelve el elemento correspondiente de la lista `valores`. Esto permite personalizar cómo se accede a los elementos de la instancia y proporcionar una interfaz similar a la de una lista o diccionario.

#### Uso de `__setitem__`

El método `__setitem__` en Python se utiliza para permitir la asignación de valores a los elementos de una instancia de una clase mediante indexación, es decir, utilizando corchetes `[]`. Al definir el método `__setitem__` en una clase, se puede personalizar cómo se asignan valores a los elementos de la instancia, lo que puede ser útil para proporcionar una interfaz similar a la de una lista o diccionario. Aquí tienes un ejemplo de pseudocódigo y código para ilustrar cómo se puede lograr esto:

Código en Python:

```python

class MiClase:
    def __init__(self, valores):
        self.valores = valores

    def __setitem__(self, indice, valor):
        self.valores[indice] = valor
```

Salida:

```python
objeto = MiClase([1, 2, 3, 4, 5])
objeto[2] = 42
print(objeto.valores)
# Salida: [1, 2, 42, 4, 5]
```

En este ejemplo, la clase `MiClase` define el método `__setitem__` para permitir la asignación de valores a los elementos de la lista `valores` mediante indexación. Cuando se asigna un valor a un elemento de la instancia de `MiClase` utilizando corchetes `[]`, se llama al método `__setitem__` y se asigna el valor correspondiente al elemento de la lista `valores`. Esto permite personalizar cómo se asignan valores a los elementos de la instancia y proporcionar una interfaz similar a la de una lista o diccionario.

#### Uso de `__iter__` y `__next__`

El método `__iter__` en Python se utiliza para devolver un iterador sobre una instancia de una clase, lo que permite recorrer los elementos de la instancia utilizando un bucle `for`. Al definir el método `__iter__` en una clase, se puede personalizar cómo se itera sobre los elementos de la instancia, lo que puede ser útil para proporcionar una interfaz similar a la de una lista o diccionario. Aquí tienes un ejemplo de pseudocódigo y código para ilustrar cómo se puede lograr esto:

Código en Python:

```python
class MiClase:
    def __init__(self, valores):
        self.valores = valores
        self.indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice < len(self.valores):
            valor = self.valores[self.indice]
            self.indice += 1
            return valor
        else:
            raise StopIteration
```

Salida:

```python

objeto = MiClase([1, 2, 3, 4, 5])
for valor in objeto:
    print(valor)
# Salida:
# 1
# 2
# 3
# 4
# 5
```

En este ejemplo, la clase `MiClase` define los métodos `__iter__` y `__next__` para permitir la iteración sobre los elementos de la lista `valores`. Cuando se utiliza un bucle `for` para recorrer los elementos de la instancia de `MiClase`, se llama al método `__iter__` para obtener un iterador y al método `__next__` para obtener los elementos sucesivos de la lista `valores`. Esto permite personalizar cómo se itera sobre los elementos de la instancia y proporcionar una interfaz similar a la de una lista o diccionario.

- Ejemplo 2: Ejemplifica con una clase que obtiene una lista de numeros, la ordena y retorna la raiz cuadrada de los elementos

```python
import math

class RaizCuadrada:
    def __init__(self, valores):
        self.valores = sorted(valores)
        self.indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice < len(self.valores):
            valor = math.sqrt(self.valores[self.indice])
            self.indice += 1
            return valor
        else:
            raise StopIteration

valores = [9, 16, 4, 25, 36]
raices = RaizCuadrada(valores)

for raiz in raices:
    print(raiz)

# Salida:
# 2.0
# 3.0
# 4.0
# 5.0
# 6.0
```

En este ejemplo, la clase `RaizCuadrada` define los métodos `__iter__` y `__next__` para permitir la iteración sobre los elementos de la lista `valores`, ordenados y con la raíz cuadrada de cada elemento. Cuando se utiliza un bucle `for` para recorrer los elementos de la instancia de `RaizCuadrada`, se llama al método `__iter__` para obtener un iterador y al método `__next__` para obtener los elementos sucesivos de la lista `valores`. Esto permite personalizar cómo se itera sobre los elementos de la instancia y proporcionar una interfaz similar a la de una lista o diccionario.

### Lección 3: Slots

Los `__slots__` en Python se utilizan para restringir los atributos que una instancia de una clase puede tener. Al definir `__slots__` en una clase, se especifica una lista de nombres de atributos válidos para esa clase, lo que impide la creación de nuevos atributos en las instancias de esa clase. Esto puede ser útil para optimizar el uso de memoria y evitar errores tipográficos al acceder a los atributos de una instancia. Aquí tienes un ejemplo de pseudocódigo y código para ilustrar cómo se puede lograr esto:

Código en Python:

```python
class MiClase:
    __slots__ = ['atributo1', 'atributo2']

    def __init__(self, valor1, valor2):
        self.atributo1 = valor1
        self.atributo2 = valor2

objeto = MiClase(42, 'Hola')
objeto.atributo1 = 100
objeto.atributo2 = 'Mundo'
objeto.atributo3 = True  # Error: AttributeError: 'MiClase' object has no attribute 'atributo3'
```

## Unidad 2: Manipulación de atributos

En Python, los atributos de una clase son variables que se utilizan para almacenar información sobre las instancias de esa clase. Los atributos pueden ser de diferentes tipos, como enteros, cadenas, listas, diccionarios, funciones, etc., y se utilizan para representar el estado de un objeto y definir su comportamiento. Los atributos de una clase se pueden acceder y modificar utilizando la notación de punto (`objeto.atributo`) o la función `getattr()` y `setattr()`. En esta unidad, exploraremos cómo manipular los atributos de una clase en Python, incluida la creación, acceso, modificación y eliminación de atributos, así como el uso de los métodos `__getattr__`, `__setattr__`, `__delattr__` y `__dir__` para personalizar el comportamiento de los atributos de una clase.

### Lección 1: Creación de atributos

En Python, los atributos de una clase se crean asignando valores a variables dentro de la definición de la clase o dentro de los métodos de la clase. Los atributos pueden ser de diferentes tipos, como enteros, cadenas, listas, diccionarios, funciones, etc., y se utilizan para representar el estado de un objeto y definir su comportamiento. Aquí tienes un ejemplo de pseudocódigo y código para ilustrar cómo se pueden crear atributos en una clase:

Código en Python:

```python
class MiClase:
    atributo1 = 42
    atributo2 = 'Hola'
    
    def __init__(self, valor):
        self.atributo3 = valor
        
objeto = MiClase(100)
print(objeto.atributo1)  # Salida: 42
print(objeto.atributo2)  # Salida: 'Hola'
print(objeto.atributo3)  # Salida: 100
```

En este ejemplo, la clase `MiClase` define tres atributos: `atributo1`, `atributo2` y `atributo3`. Los dos primeros son atributos de clase, que se comparten entre todas las instancias de la clase, mientras que el tercero es un atributo de instancia, que es específico de cada instancia de la clase. Los atributos se pueden acceder utilizando la notación de punto (`objeto.atributo`) y se pueden modificar asignando nuevos valores a ellos.

- Ejemplo 2: Ejemplifica con una clase que tiene un atributo de clase y un atributo de instancia

```python
class Persona:
    especie = 'Humano'

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

juan = Persona('Juan', 30)
print(juan.especie)  # Salida: 'Humano'
print(juan.nombre)   # Salida: 'Juan'
print(juan.edad)     # Salida: 30
```

En este ejemplo, la clase `Persona` define un atributo de clase `especie` y dos atributos de instancia `nombre` y `edad`. El atributo de clase `especie` se comparte entre todas las instancias de la clase, mientras que los atributos de instancia `nombre` y `edad` son específicos de cada instancia de la clase. Los atributos se pueden acceder utilizando la notación de punto (`objeto.atributo`) y se pueden modificar asignando nuevos valores a ellos.

#### Manejo de atributos con `property`

En Python, la función `property()` se utiliza para crear propiedades de atributos en una clase, lo que permite personalizar cómo se accede, modifica y elimina un atributo. Las propiedades de atributos se definen mediante métodos `getter`, `setter` y `deleter`, que se llaman automáticamente cuando se accede, modifica o elimina un atributo de la clase. Esto puede ser útil para validar los valores de los atributos, realizar cálculos adicionales al acceder o modificar un atributo, o realizar acciones específicas al eliminar un atributo. Aquí tienes un ejemplo de pseudocódigo y código para ilustrar cómo se puede lograr esto:

Código en Python:

```python
class MiClase:
    def __init__(self, valor):
        self._atributo = valor

    def get_atributo(self):
        return self._atributo

    def set_atributo(self, valor):
        self._atributo = valor

    def del_atributo(self):
        del self._atributo

    atributo = property(get_atributo, set_atributo, del_atributo)

objeto = MiClase(42)
print(objeto.atributo)  # Salida: 42
objeto.atributo = 100
print(objeto.atributo)  # Salida: 100
del objeto.atributo
print(objeto.atributo)  # Error: AttributeError: 'MiClase' object has no attribute '_atributo'
```

En este ejemplo, la clase `MiClase` define un atributo `_atributo` y los métodos `get_atributo`, `set_atributo` y `del_atributo` para personalizar cómo se accede, modifica y elimina el atributo. La función `property()` se utiliza para crear una propiedad de atributo `atributo` que llama a los métodos correspondientes al acceder, modificar o eliminar el atributo. Esto permite personalizar el comportamiento de los atributos de la clase y realizar acciones adicionales al acceder, modificar o eliminar un atributo.

**porque se usa `_atributo` en lugar de `atributo` en el ejemplo anterior?**

El uso de `_atributo` en lugar de `atributo` en el ejemplo anterior es una convención de nomenclatura común en Python para indicar que el atributo es "privado" y no debe ser accedido directamente desde fuera de la clase. En Python, no hay verdaderos atributos privados, pero el uso de un guion bajo al principio del nombre del atributo (`_atributo`) es una convención que indica que el atributo no debe ser accedido directamente desde fuera de la clase. En su lugar, se debe acceder al atributo a través de métodos `getter` y `setter` que permiten personalizar cómo se accede y modifica el atributo. Esto ayuda a encapsular la lógica de la clase y a prevenir errores al acceder directamente a los atributos desde fuera de la clase.

- Ejemplo 2: Ejemplifica con una clase que tiene un atributo privado y una propiedad de atributo

```python

class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        if edad < 0:
            raise ValueError('La edad no puede ser negativa')
        self._edad = edad

    nombre = property(get_nombre, set_nombre)
    edad = property(get_edad, set_edad)

juan = Persona('Juan', 30)
print(juan.nombre)  # Salida: 'Juan'
juan.nombre = 'Pedro'
print(juan.nombre)  # Salida: 'Pedro'
print(juan.edad)    # Salida: 30
juan.edad = 40
print(juan.edad)    # Salida: 40
juan.edad = -10     # Error: ValueError: La edad no puede ser negativa
```

En este ejemplo, la clase `Persona` define dos atributos privados `_nombre` y `_edad` y los métodos `get_nombre`, `set_nombre`, `get_edad` y `set_edad` para personalizar cómo se accede y modifica los atributos. Las propiedades de atributo `nombre` y `edad` se crean utilizando la función `property()` y se asocian con los métodos correspondientes. Esto permite personalizar el comportamiento de los atributos `nombre` y `edad` y validar los valores asignados a ellos al modificarlos.

#### Manejo de atributos con decoradores

En Python, los decoradores se utilizan para modificar o extender el comportamiento de una función o método. Los decoradores se aplican utilizando la sintaxis `@decorador` antes de la definición de la función o método, lo que permite personalizar su comportamiento sin modificar su código interno. En el caso de las propiedades de atributo, se pueden utilizar decoradores para definir los métodos `getter`, `setter` y `deleter` de una propiedad de atributo de forma más concisa y legible. Aquí tienes un ejemplo de pseudocódigo y código para ilustrar cómo se puede lograr esto:

Código en Python:

```python

class MiClase:
    def __init__(self, valor):
        self._atributo = valor

    @property
    def atributo(self):
        return self._atributo

    @atributo.setter
    def atributo(self, valor):
        self._atributo = valor

    @atributo.deleter
    def atributo(self):
        del self._atributo


objeto = MiClase(42)
print(objeto.atributo)  # Salida: 42
objeto.atributo = 100
print(objeto.atributo)  # Salida: 100
del objeto.atributo
print(objeto.atributo)  # Error: AttributeError: 'MiClase' object has no attribute '_atributo'
```

### Lección 2: Herencia de atributos

La herencia en Python se refiere a la capacidad de una clase de heredar atributos y métodos de otra clase, lo que permite reutilizar y extender la funcionalidad de una clase existente. Cuando una clase hereda de otra clase, la clase hija adquiere todos los atributos y métodos de la clase padre y puede agregar nuevos atributos y métodos o sobrescribir los existentes. La herencia en Python se implementa utilizando la notación de paréntesis en la definición de la clase, donde se especifica la clase padre de la que se hereda. Aquí tienes un ejemplo de pseudocódigo y código para ilustrar cómo se puede lograr esto:

Pseudocódigo:

```ps
Clase ClasePadre:
    atributo_padre = 'Padre'

Clase ClaseHija(ClasePadre):
    atributo_hija = 'Hija'
```

Código en Python:

```python

class ClasePadre:
    atributo_padre = 'Padre'

class ClaseHija(ClasePadre):

    def __init__(self):
        self.atributo_hija = 'Hija'
    
objeto = ClaseHija()
print(objeto.atributo_padre)  # Salida: 'Padre'
print(objeto.atributo_hija)   # Salida: 'Hija'
```

### Leccion 3: Descriptor de atributos

Los descriptores de atributos en Python se utilizan para personalizar cómo se accede, modifica y elimina un atributo de una clase. Los descriptores son objetos que definen los métodos `__get__`, `__set__` y `__delete__`, que se llaman automáticamente cuando se accede, modifica o elimina un atributo de la clase. Los descriptores se pueden utilizar para validar los valores de los atributos, realizar cálculos adicionales al acceder o modificar un atributo, o realizar acciones específicas al eliminar un atributo. Aquí tienes un ejemplo de pseudocódigo y código para ilustrar cómo se puede lograr esto:

Código en Python:

```python
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

    def __init__(self, valor):
        self._atributo = valor

objeto = MiClase(42)
print(objeto.atributo)  # Salida: 'Accediendo al atributo' 42
objeto.atributo = 100
print(objeto.atributo)  # Salida: 'Modificando el atributo' 'Accediendo al atributo' 100
del objeto.atributo
print(objeto.atributo)  # Salida: 'Eliminando el atributo' 'Accediendo al atributo' AttributeError: 'MiClase' object has no attribute '_atributo'
```

En este ejemplo, la clase `Descriptor` define los métodos `__get__`, `__set__` y `__delete__` para personalizar cómo se accede, modifica y elimina el atributo `_atributo`. La clase `MiClase` define un atributo `atributo` que utiliza el descriptor `Descriptor` para personalizar su comportamiento. Cuando se accede, modifica o elimina el atributo `atributo`, se llaman los métodos correspondientes del descriptor, lo que permite personalizar el comportamiento del atributo y realizar acciones adicionales al acceder, modificar o eliminar el atributo.

**explaya: porque defines el método `__get__` de esa forma en el descriptor?**

El método `__get__` en el descriptor se define de esa forma para personalizar cómo se accede al atributo de la clase. El método `__get__` recibe tres argumentos: `self`, `instancia` y `clase`. El argumento `instancia` es la instancia de la clase en la que se está accediendo al atributo, y el argumento `clase` es la clase de la instancia. Al llamar al método `__get__` en el descriptor, se puede personalizar cómo se accede al atributo de la clase y realizar acciones adicionales al acceder al atributo. En este caso, el método `__get__` imprime un mensaje indicando que se está accediendo al atributo y devuelve el valor del atributo `_atributo` de la instancia. Esto permite personalizar el comportamiento del atributo y realizar acciones adicionales al acceder al atributo de la clase.

- Ejericio 2: Ejemplifica con una clase que tiene un atributo de correo y un descriptor que modifica el correo para que termine en '.net'

```python

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
print(obj1.mail)  # Salida: 'juan@gmail.net'
obj1.atributo = 'Pedro' # Salida: 'Modificando el atributo'
print(obj1.atributo)  # Salida: 'Accediendo al atributo' Pedro
obj1.mail = 'pedro@gmail' # Salida: 'Modificando el correo'
print(obj1.mail)  # Salida: 'pedro@gmail.net'

```

En este ejemplo, la clase `AccederMail` define los métodos `__get__` y `__set__` para personalizar cómo se accede y modifica el atributo `_mail`. El método `__get__` devuelve el valor del atributo `_mail` seguido de '.net', y el método `__set__` valida que el correo contenga un '@' antes de modificarlo. La clase `MiClase` define un atributo `mail` que utiliza el descriptor `AccederMail` para personalizar su comportamiento. Cuando se accede o modifica el atributo `mail`, se llaman los métodos correspondientes del descriptor, lo que permite personalizar el comportamiento del atributo y realizar acciones adicionales al acceder o modificar el atributo.

### Lección 4: Métodos especiales

Los métodos especiales en Python son métodos predefinidos que se utilizan para personalizar el comportamiento de las clases y objetos en Python. Estos métodos se llaman automáticamente en ciertas situaciones, como al crear, comparar, acceder, modificar o eliminar objetos, y permiten personalizar cómo se comportan las clases y objetos en diferentes contextos. Al implementar métodos especiales en una clase, se puede personalizar cómo se crean, comparan, acceden, modifican o eliminan instancias de esa clase, lo que puede ser útil para adaptar el comportamiento de la clase a las necesidades específicas del programa. Aquí tienes una lista de algunos de los métodos especiales más comunes en Python y cómo se utilizan:

- `__init__(self, ...)`: Se llama automáticamente al crear una nueva instancia de la clase y se utiliza para inicializar los atributos de la instancia.
- `__str__(self)`: Se llama automáticamente al convertir una instancia de la clase a una cadena de texto con `str()` o `print()` y se utiliza para personalizar la representación de la instancia.
- `__eq__(self, otro)`: Se llama automáticamente al comparar dos instancias de la clase con el operador `==` y se utiliza para personalizar cómo se comparan las instancias.
- `__ne__(self, otro)`: Se llama automáticamente al comparar dos instancias de la clase con el operador `!=` y se utiliza para personalizar cómo se comparan las instancias.
- `__lt__(self, otro)`: Se llama automáticamente al comparar dos instancias de la clase con el operador `<` y se utiliza para personalizar cómo se comparan las instancias.
- `__le__(self, otro)`: Se llama automáticamente al comparar dos instancias de la clase con el operador `<=` y se utiliza para personalizar cómo se comparan las instancias.
- `__gt__(self, otro)`: Se llama automáticamente al comparar dos instancias de la clase con el operador `>` y se utiliza para personalizar cómo se comparan las instancias.
- `__ge__(self, otro)`: Se llama automáticamente al comparar dos instancias de la clase con el operador `>=` y se utiliza para personalizar cómo se comparan las instancias.
- `__getattr__(self, nombre)`: Se llama automáticamente al intentar acceder a un atributo que no existe en la instancia y se utiliza para personalizar cómo se manejan los atributos inexistentes.
- `__setattr__(self, nombre, valor)`: Se llama automáticamente al intentar asignar un valor a un atributo de la instancia y se utiliza para personalizar cómo se asignan los valores a los atributos.
- `__delattr__(self, nombre)`: Se llama automáticamente al intentar eliminar un atributo de la instancia y se utiliza para personalizar cómo se eliminan los atributos.
- `__dir__(self)`: Se llama automáticamente al utilizar la función `dir()` en una instancia de la clase y se utiliza para personalizar la lista de atributos y métodos de la instancia.
- `__getitem__(self, clave)`: Se llama automáticamente al acceder a un elemento de la instancia mediante indexación y se utiliza para personalizar cómo se acceden los elementos de la instancia.
- `__setitem__(self, clave, valor)`: Se llama automáticamente al asignar un valor a un elemento de la instancia mediante indexación y se utiliza para personalizar cómo se asignan los valores a los elementos de la instancia.
- `__delitem__(self, clave)`: Se llama automáticamente al eliminar un elemento de la instancia mediante indexación y se utiliza para personalizar cómo se eliminan los elementos de la instancia.
- `__iter__(self)`: Se llama automáticamente al iterar sobre los elementos de la instancia y se utiliza para personalizar cómo se itera sobre los elementos de la instancia.
- `__next__(self)`: Se llama automáticamente al obtener el siguiente elemento de la instancia durante la iteración y se utiliza para personalizar cómo se obtienen los elementos sucesivos de la instancia.
- `__call__(self, ...)`: Se llama automáticamente al llamar a una instancia de la clase como si fuera una función y se utiliza para personalizar el comportamiento de la instancia como una función.
- `__len__(self)`: Se llama automáticamente al obtener la longitud de la instancia con la función `len()` y se utiliza para personalizar cómo se calcula la longitud de la instancia.
- `__contains__(self, valor)`: Se llama automáticamente al comprobar si un valor está contenido en la instancia con el operador `in` y se utiliza para personalizar cómo se comprueba la presencia de un valor en la instancia.
- `__add__(self, otro)`: Se llama automáticamente al sumar dos instancias de la clase con el operador `+` y se utiliza para personalizar cómo se suman las instancias.
- `__sub__(self, otro)`: Se llama automáticamente al restar dos instancias de la clase con el operador `-` y se utiliza para personalizar cómo se restan las instancias.
- `__mul__(self, otro)`: Se llama automáticamente al multiplicar dos instancias de la clase con el operador `*` y se utiliza para personalizar cómo se multiplican las instancias.
- `__truediv__(self, otro)`: Se llama automáticamente al dividir dos instancias de la clase con el operador `/` y se utiliza para personalizar cómo se dividen las instancias.
- `__floordiv__(self, otro)`: Se llama automáticamente al dividir dos instancias de la clase con el operador `//` y se utiliza para personalizar cómo se divide entera las instancias.
- `__mod__(self, otro)`: Se llama automáticamente al obtener el módulo de dos instancias de la clase con el operador `%` y se utiliza para personalizar cómo se obtiene el módulo de las instancias.
- `__pow__(self, otro)`: Se llama automáticamente al elevar una instancia de la clase a otra con el operador `**` y se utiliza para personalizar cómo se elevan las instancias.
- `__neg__(self)`: Se llama automáticamente al obtener el negativo de una instancia de la clase con el operador `-` y se utiliza para personalizar cómo se obtiene el negativo de la instancia.
- `__pos__(self)`: Se llama automáticamente al obtener el positivo de una instancia de la clase con el operador `+` y se utiliza para personalizar cómo se obtiene el positivo de la instancia.
- `__abs__(self)`: Se llama automáticamente al obtener el valor absoluto de una instancia de la clase con la función `abs()` y se utiliza para personalizar cómo se obtiene el valor absoluto de la instancia.
- `__round__(self, n)`: Se llama automáticamente al redondear una instancia de la clase con la función `round()` y se utiliza para personalizar cómo se redondea la instancia.
- `__int__(self)`: Se llama automáticamente al convertir una instancia de la clase a un entero con la función `int()` y se utiliza para personalizar cómo se convierte la instancia a un entero.
- `__float__(self)`: Se llama automáticamente al convertir una instancia de la clase a un flotante con la función `float()` y se utiliza para personalizar cómo se convierte la instancia a un flotante.
- `__str__(self)`: Se llama automáticamente al convertir una instancia de la clase a una cadena de texto con `str()` o `print()` y se utiliza para personalizar la representación de la instancia.
- `__repr__(self)`: Se llama automáticamente al obtener la representación "oficial" de una instancia de la clase con la función `repr()` y se utiliza para personalizar la representación de la instancia.
- `__format__(self, formato)`: Se llama automáticamente al formatear una instancia de la clase con la función `format()` y se utiliza para personalizar cómo se formatea la instancia.

#### Uso de `__getattr__`

El método `__getattr__` en Python se utiliza para personalizar cómo se manejan los atributos inexistentes en una instancia de una clase. Este método se llama automáticamente cuando se intenta acceder a un atributo que no existe en la instancia, y se puede utilizar para proporcionar un valor predeterminado, lanzar una excepción, o realizar acciones específicas al acceder a un atributo inexistente. Aquí tienes un ejemplo de pseudocódigo y código para ilustrar cómo se puede lograr esto:

Código en Python:

```python
class MiClase:
    def __init__(self, valor):
        self.atributo = valor

    def __getattr__(self, nombre):
        return f'Atributo {nombre} no encontrado'

objeto = MiClase(42)
print(objeto.atributo)  # Salida: 42
print(objeto.otro_atributo)  # Salida: 'Atributo otro_atributo no encontrado'
```

En este ejemplo, la clase `MiClase` define el método `__getattr__` para personalizar cómo se manejan los atributos inexistentes en la instancia. Cuando se intenta acceder a un atributo que no existe en la instancia, se llama al método `__getattr__` y se devuelve un mensaje indicando que el atributo no se encontró. Esto permite personalizar cómo se manejan los atributos inexistentes y proporcionar un comportamiento específico al acceder a un atributo que no existe en la instancia.

- Ejemplo 2:

```python

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

```

En este ejemplo, la clase `MiClase` define el método `__getattr__` para personalizar cómo se manejan los atributos inexistentes en la instancia. Cuando se intenta acceder a un atributo que no existe en la instancia, se llama al método `__getattr__` y se devuelve un mensaje específico para cada atributo. Esto permite personalizar cómo se manejan los atributos inexistentes y proporcionar un comportamiento específico al acceder a un atributo que no existe en la instancia.

#### Uso de `___setattr__`

El método `__setattr__` en Python se utiliza para personalizar cómo se asignan valores a los atributos de una instancia de una clase. Este método se llama automáticamente cuando se intenta asignar un valor a un atributo de la instancia, y se puede utilizar para validar los valores asignados, realizar cálculos adicionales al asignar un valor, o realizar acciones específicas al asignar un valor a un atributo. Aquí tienes un ejemplo de pseudocódigo y código para ilustrar cómo se puede lograr esto:

Código en Python:

```python
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
```

En este ejemplo, la clase `MiClase` define el método `__setattr__` para personalizar cómo se asignan valores a los atributos de la instancia. Cuando se intenta asignar un valor a un atributo de la instancia, se llama al método `__setattr__` y se asigna el valor al atributo correspondiente en el diccionario `__dict__` de la instancia. Esto permite personalizar cómo se asignan valores a los atributos y realizar acciones adicionales al asignar un valor a un atributo de la instancia.

**Nota:** Es importante tener en cuenta que al asignar un valor a un atributo dentro del método `__setattr__`, se debe utilizar el diccionario `__dict__` para evitar un bucle infinito al llamar al método `__setattr__` de nuevo. En tanto, el condicional `if...` se utiliza para mapear el atributo público `nombre` al atributo privado `_nombre` en la instancia (quitandole esa preocupación al usuario?  ... ).

#### Uso de `__delattr__`

El método `__delattr__` en Python se utiliza para personalizar cómo se eliminan atributos de una instancia de una clase. Este método se llama automáticamente cuando se intenta eliminar un atributo de la instancia, y se puede utilizar para realizar acciones específicas al eliminar un atributo, como liberar recursos, actualizar otros atributos, o lanzar una excepción. Aquí tienes un ejemplo de pseudocódigo y código para ilustrar cómo se puede lograr esto:  

Código en Python:

```python

class MiClase:

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

    def __delattr__(self, atributo):
        if atributo == 'nombre':
            atributo = '_nombre'
        del self.__dict__[atributo]

objeto = MiClase('Olivia Newton')
print(objeto.nombre) # Olivia Newton
del objeto.nombre
print(objeto.nombre) # AttributeError: El atributo nombre no existe
```

En este ejemplo, la clase `MiClase` define el método `__delattr__` para personalizar cómo se eliminan atributos de la instancia. Cuando se intenta eliminar un atributo de la instancia, se llama al método `__delattr__` y se elimina el atributo correspondiente del diccionario `__dict__` de la instancia. Esto permite personalizar cómo se eliminan atributos de la instancia y realizar acciones adicionales al eliminar un atributo.

## Unidad 3: Decoradores

Los decoradores en Python son funciones que se utilizan para modificar o extender el comportamiento de otras funciones o métodos. Los decoradores se aplican utilizando la sintaxis `@decorador` antes de la definición de la función o método, lo que permite personalizar su comportamiento sin modificar su código interno. Los decoradores se utilizan comúnmente para añadir funcionalidades adicionales a las funciones, como la validación de argumentos, la medición del tiempo de ejecución, la gestión de excepciones, la autenticación de usuarios, etc.

### Lección 1. Función como decorador

En Python, una función puede actuar como un decorador si toma otra función como argumento y devuelve una nueva función que modifica o extiende el comportamiento de la función original. Los decoradores se aplican utilizando la sintaxis `@decorador` antes de la definición de la función que se va a decorar, lo que permite personalizar su comportamiento sin modificar su código interno. Aquí tienes un ejemplo de pseudocódigo y código para ilustrar cómo se puede lograr esto:

Pseudocódigo:

```ps
Función decorador(función):
    Definir nueva_función():
        # Código adicional antes de llamar a la función original
        función()
        # Código adicional después de llamar a la función original
    Devolver nueva_función

@decorador
Función original():
    # Código de la función original

original()

```

Código en Python:

```python
# definir una funcion decoradora
def decorador(funcion):
    def nueva_funcion():
        # Código antes de llamar a la funciòn
        print('Llamando a la función')

        # llamamos a la función
        resultado = funcion()

        # Código después de llamar a la función
        print('Después de llamar a la función')

        # Devolver el resultado de la función original
        return resultado
    
    return nueva_funcion

# definir una funcion a decorar
def funcion_a_decorar():
    print('Dentro de la función a decorar')


# Decoramos la función
funcion_decorada = decorador(funcion_a_decorar)

# Llamamos a la función decorada
funcion_decorada()
```

En este ejemplo, la función `decorador` toma otra función `funcion` como argumento y devuelve una nueva función `nueva_funcion` que modifica o extiende el comportamiento de la función original. La función `nueva_funcion` imprime un mensaje antes y después de llamar a la función original, y luego devuelve el resultado de la función original. Al llamar a la función decorada `funcion_decorada`, se ejecuta el código adicional antes y después de llamar a la función original, lo que permite personalizar el comportamiento de la función sin modificar su código interno.

### Lección 2. Clase como decorador

En Python, una clase puede actuar como un decorador si implementa los métodos `__init__` y `__call__`, lo que permite personalizar cómo se aplica el decorador a una función o método. Los decoradores de clase se utilizan de la misma manera que los decoradores de función, pero permiten un mayor control y flexibilidad al personalizar el comportamiento del decorador. Aquí tienes un ejemplo de pseudocódigo y código para ilustrar cómo se puede lograr esto:

Pseudocódigo:

```ps
Clase Decorador:
    Definir __init__(self, función):
        # Inicializar el decorador con la función
        self.función = función

    Definir __call__(self):
        # Código adicional antes de llamar a la función original
        self.función()
        # Código adicional después de llamar a la función original

@Decorador
Función original():
    # Código de la función original
```

Código Python

```python

class Decorador:

    def __init_-_(self, funcion):
        # Inicializar el decorador con la función
        self.funcion = funcion

    def __call__(self. *args, **kwargs):
        # Código adicional antes de llamar a la función original
        print('Llamando a la función')

        # Llamamos a la función original
        resultado = self.funcion(*args, **kwargs)

        # Código adicional después de llamar a la función original
        print('Después de llamar a la función')

        # Devolver el resultado de la función original
        return resultado

@Decorador
def funcion_a_decorar():
    print('Dentro de la función a decorar')

# Llamamos a la función decorada
funcion_a_decorar()

# Salida:
# Llamando a la función
# Dentro de la función a decorar
# Después de llamar a la función

```

En este ejemplo ....

### Lección 3. Decoradores de clase

Los decoradores de clase son una forma de administrar clases o de terminar cómo se crean las instancias de una clase. Los decoradores de clase se aplican utilizando la sintaxis `@decorador` antes de la definición de la clase que se va a decorar, lo que permite personalizar su comportamiento sin modificar su código interno. Los decoradores de clase se utilizan comúnmente para añadir funcionalidades adicionales a las clases, como la validación de atributos, la gestión de recursos, la autenticación de usuarios, etc. Aquí tienes un ejemplo de pseudocódigo y código para ilustrar cómo se puede lograr esto:

Pseudocódigo:

```ps
Clase Decorador:
    Definir __init__(self, clase):
        # Inicializar el decorador con la clase
        self.clase = clase

    Definir __call__(self):
        # Código adicional antes de crear la instancia de la clase
        instancia = self.clase()
        # Código adicional después de crear la instancia de la clase
        Devolver instancia

@Decorador
Clase original:
    # Código de la clase original

instancia = Clase original()
```

Codigo en Python:

```python

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

```

En este ejemplo, la clase `Decorador` toma otra clase `clase` como argumento y devuelve una nueva clase `Envol` que modifica o extiende el comportamiento de la clase original. La clase `Envol` inicializa una instancia de la clase original en su método `__init__` y personaliza cómo se accede y modifica los atributos de la instancia en los métodos `__getattr__` y `__setattr__`. Al decorar la clase `Auto` con el decorador `decorador`, se crea una nueva clase `Envol` que personaliza cómo se accede y modifica los atributos de las instancias de la clase `Auto`.

### Lección 4. Apilamiento de decoradores

En Python, es posible apilar varios decoradores en una función o método para aplicar múltiples decoradores a la misma función. Los decoradores se aplican en orden de arriba a abajo, lo que significa que el decorador más cercano a la función se aplica primero, seguido de los decoradores en orden descendente. Esto permite personalizar el comportamiento de una función con múltiples decoradores y añadir funcionalidades adicionales de forma modular y reutilizable. Aquí tienes un ejemplo de pseudocódigo y código para ilustrar cómo se puede lograr esto:

Pseudocódigo:

```ps
@decorador1

@decorador2

def función():
    # Código de la función

```

Código en Python:

```python

def decorador1(funcion):
    def nueva_funcion():
        print('Decorador 1')
        funcion()
    return nueva_funcion

def decorador2(funcion):
    def nueva_funcion():
        print('Decorador 2')
        funcion()
    return nueva_funcion

@decorador1
@decorador2
def funcion():
    print('Función original')

funcion()
    
```

En este ejemplo, la función `funcion` se decora con los decoradores `decorador1` y `decorador2` utilizando la sintaxis `@decorador1` y `@decorador2` antes de la definición de la función. Los decoradores `decorador1` y `decorador2` se aplican en orden de arriba a abajo, lo que significa que el decorador más cercano a la función se aplica primero, seguido de los decoradores en orden descendente. Al llamar a la función `funcion`, se ejecuta el código adicional de los decoradores `decorador1` y `decorador2` antes de llamar a la función original, lo que permite personalizar el comportamiento de la función con múltiples decoradores.

- Ejemplo 2

```python
def cambio_estado(fun):
    def wrapper(*args, **kwargs):
        if args[0]:
            print("El motor se ha encendido")
        else:
            print("Se apagó el motor")
        return fun(*args, **kwargs)
    return wrapper

def aviso_cambio_estado(fun):
    def wrapper(*args, **kwargs):
        print("Se ejecuto %s" % fun.__name__)
        print("Enviando whatsapp")
        return fun(*args, **kwargs)
    return wrapper

@cambio_estado
@aviso_cambio_estado
def estado_motor(estado):
    if estado == True or estado == False:
        print(estado)
    else:
        print("Error: El estado debe ser True o False")

estado_motor(True)

estado_motor(False)
```

En este ejemplo, la función `estado_motor` se decora con los decoradores `cambio_estado` y `aviso_cambio_estado` utilizando la sintaxis `@cambio_estado` y `@aviso_cambio_estado` antes de la definición de la función. Los decoradores `cambio_estado` y `aviso_cambio_estado` se aplican en orden de arriba a abajo, lo que significa que el decorador más cercano a la función se aplica primero, seguido de los decoradores en orden descendente. Al llamar a la función `estado_motor`, se ejecuta el código adicional de los decoradores `cambio_estado` y `aviso_cambio_estado` antes de llamar a la función original, lo que permite personalizar el comportamiento de la función con múltiples decoradores.

### Lección 5. Decoradores con argumentos

En Python, es posible crear decoradores que acepten argumentos para personalizar su comportamiento y aplicar funcionalidades adicionales a las funciones o métodos. Los decoradores con argumentos se utilizan para configurar el comportamiento del decorador y permiten personalizar cómo se aplica el decorador a una función o método. Aquí tienes un ejemplo de pseudocódigo y código para ilustrar cómo se puede lograr esto:

Pseudocódigo:

```ps
def decorador_con_argumentos(argumento):
    Definir decorador(función):
        Definir nueva_función(*args, **kwargs):
            # Código adicional antes de llamar a la función original
            print('Argumento:', argumento)
            función(*args, **kwargs)
            # Código adicional después de llamar a la función original
        Devolver nueva_función
    Devolver decorador

@decorador_con_argumentos('Hola')
def función():
    # Código de la función

función()
```

Código en Python:

```python
def ambiente(debug):
    def decorador(func):
        def envoltura(*args, **kwargs):
            if debug:
                print("Se ejecutara la funcion en desarrollo")
            else:
                print("Se ejecutara la funcion en produccion")
            for id, argu in enumerate(args):
                print(f"Argumento {id}: {argu}")
            return func(*args, **kwargs)
        return envoltura
    return decorador

@ambiente(True)
def registro_usuario(nombre, apellido):
    print(f"Se registro {nombre}")

registro_usuario("Carlo", "Kuntz")
```
<!--
## Unidad 4: Metaclases

Con las metaclases se busca extender las funcionalidades de una clase, permitiendo modificar la forma en que se crean las instancias de una clase. Las metaclases son clases que definen cómo se crean las clases, y permiten personalizar el comportamiento de las clases y sus instancias. Las metaclases se utilizan para añadir funcionalidades adicionales a las clases, como la validación de atributos, la gestión de recursos, la autenticación de usuarios, etc. Aquí tienes un ejemplo de pseudocódigo y código para ilustrar cómo se puede lograr esto:

Pseudocódigo:

```ps
Clase Metaclase(type):
    Definir __new__(cls, nombre, bases, diccionario):
        # Código para personalizar la creación de la clase
        return super().__new__(cls, nombre, bases, diccionario)

Clase Clase(metaclass=Metaclase):
    # Código de la clase

Instancia = Clase()
```

Código en Python:

```python
class Metaclase(type):
    def __new__(cls, nombre, bases, diccionario):
        print('Creando la clase:', nombre)
        return super().__new__(cls, nombre, bases, diccionario)

class Clase(metaclass=Metaclase):
    def __init__(self):
        print('Creando una instancia de la clase')
        
instancia = Clase()
```

En este ejemplo, la clase `Metaclase` define el método `__new__` para personalizar cómo se crea la clase, y la clase `Clase` utiliza la metaclase `Metaclase` para personalizar su comportamiento. Al crear una instancia de la clase `Clase`, se llama al método `__new__` de la metaclase `Metaclase` para personalizar la creación de la clase y la instancia, lo que permite extender las funcionalidades de la clase y personalizar su comportamiento.
-->

## Unidad 4. Patrones de Desarrollo

Nos vamos a centrar en el patron Observador porque es el que solicita el Docente Barreto. Quedarán pendientes los otros patrones de diseño: singleton, factory, builder, otros. Se debe señalar que la bibliografia enuncia que cada patron se diseña para resolver un problema especifico, por lo que se debe tener en cuenta el problema a resolver para aplicar el patron de diseño adecuado.

### Lección 1. Patrón Observador

El patrón Observador es un patrón de diseño de comportamiento que define una relación de uno a muchos entre un sujeto y varios observadores. El sujeto es el objeto que tiene un estado que puede cambiar, y los observadores son los objetos que desean ser notificados cuando cambia el estado del sujeto. Cuando el estado del sujeto cambia, notifica a todos los observadores registrados, permitiéndoles actualizar su estado o realizar acciones adicionales en respuesta al cambio. El patrón Observador se utiliza para implementar la comunicación entre objetos de forma desacoplada y flexible, permitiendo que los objetos se comuniquen sin conocerse directamente.

#### Implementación del patrón Observador en Python

En Python, el patrón Observador se puede implementar utilizando clases y métodos para definir el sujeto y los observadores, y establecer una relación de uno a muchos entre ellos. Aquí tienes un ejemplo de pseudocódigo y código para ilustrar cómo se puede implementar el patrón Observador en Python:

Pseudocódigo:

```ps
Clase Sujeto:
    Definir __init__(self):
        self.observadores = []

    Definir registrar_observador(self, observador):
        self.observadores.append(observador)

    Definir eliminar_observador(self, observador):
        self.observadores.remove(observador)

    Definir notificar_observadores(self):
        Para observador en self.observadores:
            observador.actualizar()

Clase Observador:
    Definir actualizar(self):
        # Código para actualizar el estado del observador

sujeto = Sujeto()
observador1 = Observador()
observador2 = Observador()

sujeto.registrar_observador(observador1)
sujeto.registrar_observador(observador2)

sujeto.notificar_observadores()
```

Código en Python:

```python
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
```

En este ejemplo, se define una clase abstracta `Sujeto` que representa el sujeto que notifica a los observadores, y una clase abstracta `Observador` que representa los observadores que reciben las notificaciones del sujeto. Se definen las clases concretas `ConcretoSujeto` y `ConcretoObservador` que implementan los métodos abstractos de las clases abstractas y personalizan su comportamiento. Se crea una instancia del sujeto `ConcretoSujeto` y un observador `ConcretoObservador`, se agrega el observador al sujeto, se cambia el estado del sujeto y se notifica a los observadores. Al imprimir el estado del observador, se muestra el estado actualizado en respuesta al cambio del sujeto.

## Unidad 5: Socket

Los sockets en Python son una forma de comunicación entre procesos que permite enviar y recibir datos a través de una red o entre procesos en la misma máquina. Los sockets se utilizan para establecer una conexión entre un cliente y un servidor, y permiten la transferencia de datos en tiempo real. Los sockets en Python se implementan utilizando la biblioteca `socket`, que proporciona una interfaz para crear y gestionar conexiones de red.

### Lección 1. Servidor de sockets

El servidor de sockets en Python se implementa utilizando la biblioteca `socket` para crear un socket de servidor y escuchar conexiones entrantes de los clientes. El servidor de sockets se ejecuta en un bucle infinito para aceptar conexiones de los clientes y manejar las solicitudes de los clientes. Aquí tienes un ejemplo de pseudocódigo y código para ilustrar cómo se puede implementar un servidor de sockets en Python:

Pseudocódigo:

```ps
Importar la biblioteca socket

Crear un socket de servidor

Enlazar el socket a una dirección y puerto

Escuchar conexiones entrantes

En un bucle infinito:
    Aceptar una conexión entrante
    Recibir datos del cliente
    Procesar los datos recibidos
    Enviar una respuesta al cliente
    Cerrar la conexión

Cerrar el socket de servidor

```

Código en Python:

```python
import socket

# Crear un socket de servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazar el socket a una dirección y puerto
servidor.bind(('localhost', 12345))

# Escuchar conexiones entrantes
servidor.listen()

# En un bucle infinito:
while True:
    # Aceptar una conexión entrante
    cliente, direccion = servidor.accept()
    print(f'Conexión entrante de {direccion}')

    # Recibir datos del cliente
    datos = cliente.recv(1024)
    print(f'Datos recibidos: {datos.decode()}')

    # Procesar los datos recibidos
    respuesta = 'Mensaje recibido'
    cliente.send(respuesta.encode())

    # Cerrar la conexión
    cliente.close()

# Cerrar el socket de servidor
servidor.close()
```

En este ejemplo, se crea un socket de servidor utilizando la biblioteca `socket` y se enlaza a la dirección `localhost` y el puerto `12345`. El servidor de sockets escucha conexiones entrantes de los clientes y acepta las conexiones en un bucle infinito. Cuando se recibe un mensaje del cliente, se procesa y se envía una respuesta al cliente. Finalmente, se cierra la conexión con el cliente y se continúa escuchando conexiones entrantes. El servidor de sockets se ejecuta en un bucle infinito hasta que se cierra manualmente.

### Lección 2. Cliente de sockets

El cliente de sockets en Python se implementa utilizando la biblioteca `socket` para crear un socket de cliente y conectarse a un servidor remoto. El cliente de sockets se conecta al servidor remoto y envía datos al servidor para solicitar información o realizar una acción. Aquí tienes un ejemplo de pseudocódigo y código para ilustrar cómo se puede implementar un cliente de sockets en Python:

Pseudocódigo:

```ps
Importar la biblioteca socket

Crear un socket de cliente

Conectar el socket a una dirección y puerto

Enviar datos al servidor

Recibir una respuesta del servidor

Cerrar la conexión

```

Código en Python:

```python
import socket

# Crear un socket de cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar el socket a una dirección y puerto
cliente.connect(('localhost', 12345))

# Enviar datos al servidor en utf-8
mensaje = 'Hola, servidor'
cliente.send(mensaje.encode())

# Recibir una respuesta del servidor
respuesta = cliente.recv(1024)
print(f'Respuesta del servidor: {respuesta.decode()}')

# Cerrar la conexión
cliente.close()
```
### Ejemplo 1. Echo Server

Ejemplo completo de un servidor de sockets que recibe un mensaje del cliente y lo envía de vuelta al cliente. El servidor de sockets escucha conexiones entrantes de los clientes y acepta las conexiones en un bucle infinito. Cuando se recibe un mensaje del cliente, se envía de vuelta al cliente. El servidor de sockets se ejecuta en un bucle infinito hasta que se cierra manualmente.

Código en Python:
1. Servidor:

```python
import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind(('localhost', 12345))

servidor.listen()

while True:
    cliente, direccion = servidor.accept()
    print(f'Conexión entrante de {direccion}')

    datos = cliente.recv(1024)
    print(f'Datos recibidos: {datos.decode()}')

    respuesta = datos
    cliente.send(respuesta)

    cliente.close()

servidor.close()
```

2. Cliente:

```python
import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('localhost', 12345))
mensaje = 'Hola, servidor'
cliente.send(mensaje.encode())
respuesta = cliente.recv(1024)
print(f'Respuesta del servidor: {respuesta.decode()}')
cliente.close()
```



<!--Estudiar pruebas unitarias!!! -->