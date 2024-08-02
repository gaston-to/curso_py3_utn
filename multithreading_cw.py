import threading
 
def funcion():
    for i in range(5):
        print(f'Hola, soy un hilo {i}')

hilo = threading.Thread(target=funcion)
hilo.start()
print('Hola, soy el hilo principal')
hilo.join()