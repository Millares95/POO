"""Enunciado: escriba una clase Logger, cuyo objetivo sea escribir un mensaje dado como parámetro en un archivo cada vez que
se llame al método log(mensaje). La primera línea del archivo debe ser "--Start log--", seguida de los mensajes recibidos
por el método log en la parte superior de un mensaje por línea, y la última línea del archivo, escrita cuando se destruye la instancia de Logger, 
debe ser "--End log: x log (s) -" donde x es el número de llamadas al método log. Esta clase Logger se utilizará en un método llamada()
 de una clase Test."""

class Logger :
    def __init__(self):
        #Aperturna de una archivo en modo escritura 
        self.log_file = open('log.txt', "w")
        #Iniciacion del contador de log 
        self.log_count = 0
        #Escritura de la primera línea 
        self.log_file.write("--Start log --\n")

    def __del__(self):
        #Destruccion de la instancia 
        #Se escribe la ultima linea del archivo 
        self.log_file.write("--End Log :{}log(s)--\n".format(self.log_count))
        #Cierre correcto del archivo 
        self.log_file.close()
        
    def log(self,mensaje):
        #Escritura del mensaje que se pasa como argumento 
        self.log_file.write("{}\n".format(mensaje))
        #Incremento del contador de logs
        self.log_count += 1

class Test:
    def __init__(self):
        self.logger = Logger()

    def llamada (self,mensaje):
        self.logger.log(mensaje)   

test = Test()
for i  in range(1,6):
    if i ==1:
       print( test.llamada("Primera llamada"))
    else:
        print(test.llamada('{}ª llamada'.format(str)))
