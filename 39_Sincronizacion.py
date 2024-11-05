import threading
import time
# Primera clase de accion para hacer que el coche avance 
class Rodar(threading.Thread):
    def __init__(self):
        super().__init__()
    #Metodo sobrecargado en el que serealiza realmente la accion 
    def run(self):
        # El bloqueo es capturado por el thread. Todos los demás threads que quieran capturar este bloqueo # esperarán hasta que se libere.
        bloqueo.acquire()
        for _ in range(5):
            print('.', end='')
            time.sleep(2)
# Liberación del bloqueo. Entre los otros threads que # estaban esperando capturarlo, solo se seleccionará uno # por el sistema operativo para recuperarlo.
        bloqueo.release()
#Segunda Clase de accion para hacer girar el coche
class Girar(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        bloqueo.acquire()
        for  _ in range(3):
            print("->", end='')
            time.sleep(2)
        bloqueo.release()
class Coche():
    def __init__(self):
        #Instancia de la clase de accion para rodar
        self.rodar = Rodar()
        #Instancia de la clase de accion para girar
        self.girar = Girar()
#Durante el arranque, se quiere rodar y girar simultáneamente.
    def arrancar(self):
        # El método start() oculta la mecánica de lanzamiento del thread y su asociación con el proceso padre, 
        # y  una vez que el thread ha comenzado, llama a su método run() que realizará la tarea paralela.
        self.rodar.start()
        self.girar.start()
 # Declaración del bloqueo, recurso común entre los dos threads.
bloqueo = threading.Lock() # Este bloqueo se utiliza para sincronizar los threads.   
coche = Coche()
coche.arrancar()
