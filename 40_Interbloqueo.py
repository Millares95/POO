import threading
import time

class ThreadA(threading.Thread):
    def run (self):
        print("A - Thread A lanzado")
        print("A - A la espera del bloqueo 1")
        bloqueo1.acquire()
        print("A - Bloqueo 1 adquirido")
        time.sleep(.5)
        print("A - A la espera del bloqueo 2")
        bloqueo2.acquire()
        print("A - Thread A")
        bloqueo2.release()
        bloqueo1.release() 

class ThreadB(threading.Thread):
    def run(self):
        print("B - Thread B lanzado")
        print("B - A la espera del bloqueo 2")
        bloqueo2.acquire()
        print("B - Bloqueo 2 adquirido")
        time.sleep(.5)
        print("B - A la espera del bloqueo 1 ")
        bloqueo1.acquire()
        print("B - Thread B")
        bloqueo1.release()
        bloqueo2.release()

bloqueo1 = threading.Lock()
bloqueo2 = threading.Lock()

threada = ThreadA()
threadb = ThreadB()

threada.start()
threadb.start()