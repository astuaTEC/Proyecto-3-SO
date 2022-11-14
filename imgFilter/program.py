import cv2
from threading import *
import time

class Objeto:
    def __init__(self, name, image):
        self.name = name
        self.image = image

lista = []
contador = 0

def filtro():
    global contador
    for i in range(1000):
        obj = lista[contador]
        image = obj.image
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        contador += 1

if __name__ == "__main__":
    threads = []
    inicio = time.time()
    for i in range(10000):
        lista.append( Objeto("img", cv2.imread("img.jpg")) )
    for i in range(10):
        hilo = Thread(target=filtro)
        hilo.start()
        threads.append(hilo)

    for thread in threads:
        thread.join()

    fin = time.time()
    tiempo = str( (fin - inicio) )
    print("Time taken:", tiempo, "s")
    print("Termino...", contador)