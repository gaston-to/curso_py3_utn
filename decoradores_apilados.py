"""
Ejemplo de decoradores apilados
"""
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