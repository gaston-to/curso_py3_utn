def contar_ejecuciones(funcion):
    def wrapper(*args, **kwargs):
        # Se crea un atributo en la función wrapper
        # para contar las veces que se ejecuta la función
        wrapper.ejecuciones += 1
        print(f'Función {funcion.__name__} ha sido ejecutada {wrapper.ejecuciones} veces')
        return funcion(*args, **kwargs)
    wrapper.ejecuciones = 0
    return wrapper

@contar_ejecuciones
def sumar(a, b):
    c = a + b
    return c

sumar(1, 2)
sumar(3, 4)