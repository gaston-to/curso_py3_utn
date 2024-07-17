class Decorador:
    def __init__(self, funcion):
        self.funcion = funcion

    def __call__(self, *args, **kwargs):
        print('Llamando a la función')
        resultado = self.funcion(*args, **kwargs)
        print('Después de llamar a la función')
        return resultado
    
@Decorador
def funcion_a_decorar():
    print('Dentro de la función a decorar')

funcion_a_decorar()
# Salida:
# Llamando a la función
# Dentro de la función a decorar
# Después de llamar a la función
