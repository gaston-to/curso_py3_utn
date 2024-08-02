import threading
import time

def en_espera(nombre, tiempo):
    print(f"El hilo toma el nombre de {nombre} y se ejecuta\
 {tiempo} segundos despues")
    time.sleep(tiempo)
    print(f"El hilo {nombre} finaliza su ejecución")

hilo = threading.Thread(target=en_espera, args=("gaston", 5))
hilo.start()

for i in range(5):
    print("Esto ocurre en paralelo")
    time.sleep(1)
