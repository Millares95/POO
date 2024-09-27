# class Test:
##Sobrecarga del destructor de la clase test 
#     def __del__(self):
#         print("Destrucción ")

# #Primera referecnai a la instancia Test()
# test1 = Test()
# #Segunda referencia a la intancia Test()
# test2 = Test()
# # Se elimina una referencia a la instancia de Test()
# test2 = test1 
# # se elimina una referencia a la instancia de Test()
# del test1
# # La instancia no se destruye porque todavia hay una referencia 
# print("No hay destruccion")
# del test2

#---------------------------------------------------
class MiClase:

    def __init__(self):
        print("Constructor de MiClase")
        #Apertura de un archivo modo escritura
        #y  signacion de este archivo a un atributo 
        self.archivo = open('archivo.txt','w')

    def __del__(self):
            print("Destruccion de MiClase ")
            # Cierre del archivo abierto en el constructor
            self.archivo.close()

    def escribir (self):
        #Escribir en el archivo
        self.archivo.write("esto es una prueba ")

instancia = MiClase()
instancia.escribir()
