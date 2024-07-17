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