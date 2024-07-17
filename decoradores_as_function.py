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
