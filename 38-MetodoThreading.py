# import time

# #Clase que representa a un coche
# class Coche:
#     #Metodo permite hacer que u n coche avance
#     def rodar (self):
#         print("el Coche rueda")
#         #10 veces de golpe 
#         for _ in range(10):
#             # ...simbolizamos el coche que rueda mostrando  un punto...
#             print('.')
#             # ... y esperamos un segundo para dar tiempo  al coche para girar.
#             time.sleep(1)
    
# coche = Coche()
# while True: coche.rodar() # Tenemos que esperar a que termine rodar()  antes de hacer la llamada a girar().
# coche.girar()

#*Aplicatin to Trheadig

import threading
import time
# Primera clase de accion para hacer que el coche avance 
class Rodar(threading.Thread):
    def __init__(self):
        super().__init__()
    #Metodo sobrecargado en el que serealiza realmente la accion 
    def run(self):
        for _ in range(5):
            print(".")
            time.sleep(1)
    #Segunda Clase de accion para hacer girar el coche
class Girar(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        for  _ in range(3):
            print("->")
            time.sleep(1)

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

coche = Coche()
coche.arrancar()
