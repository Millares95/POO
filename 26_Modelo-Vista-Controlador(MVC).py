"""Enunciado: siguiendo la filosofía MVC, escriba un programa que lea dos líneas en la entrada estándar, las convierta a mayúsculas y las
   escriba en un archivo. Tenga en cuenta que para beneficiarse plenamente de las ventajas del design pattern MVC, los atributos, en 
   particular los del modelo, se deben encapsular."""

import sys
#* la vista se encarga de recuperar la accion del usuario que consiste ne escribir una linea de texto en la entrada estandar 
class Vista:
    def entrada (self):
        return sys.stdin.readline()
    
#* El controlador hace el enlace entre la vista y el modelo, y también el procesamiento de datos.
class Controlador:
    #* EL controlador pide a la vista que recupere una cadena en la entrada estandar , y luego soliciar al modelo que la almacene.
    def almacenarEntrada(self):
        cadena = vista.entrada()
        modelo.agregar(cadena.upper())

        #* El controlador recupera las cadenas del modelo y las escribe en un archivo 
    def guardarCadenas(self):
        cadenas = modelo.recuperarCadenas()
        with open('text.txt', 'w') as f:
            for cadena in cadenas:
                f.write(cadena)
#* El modelo se encarga de la gestion de los datos 
class Modelo:
    def __init__(self):
        self.cadenas = []
    #* Anade una cadena a la lista 
    def agregar(self, cadena):
        self.cadenas.append(cadena)
    #*Devuevle la lista de cadenas 
    def recuperarCadenas(self):
        return self.cadenas
#* Los actores MVC son globales en este ejemplo
vista = Vista()
controlador = Controlador()
modelo = Modelo()

for _ in range(2):
    controlador.almacenarEntrada()
#Despues la guardamos en un archivo
controlador.guardarCadenas()
"""Enunciado: ahora, las líneas ya no deberían leerse en la entrada estándar, sino en un archivo que se pasa como argumento 
en el constructor de la vista; el modelo, mientras tanto, ya no debería almacenarlas en una lista, sino delegar este almacenamiento
a una clase anidada ListaCadena, que usará una lista."""

class Vista:
    def __init__(self, nombre_archivo):
        self.archivo = open(nombre_archivo, 'r')

    def __del__(self):
        self.archivo.close()

    def entrada(self):
        return self.archivo.readline()
#Controloador inalterado

class Modelo:
    class ListaCadenas:
        def __init__(self):
            self.cadenas = []

        def guardar(self, cadena):
            self.cadenas.append(cadena)
    
        def cargar(self):
            return self.cadenas
    
    def __init__(self):
        self.lista = Modelo.ListaCadena()

    def agregar(self, cadena): 
        self.lista.guardar(cadena)

    def recuperarCadenas(self): 
        return self.lista.cargar()
    
vista = Vista('26_Modelo-Vista-Controlador(MVC).py')