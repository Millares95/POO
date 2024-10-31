import json

json_string = json.dumps([1,"Dos",None,True,{11:"One"}]) # Convertimos la lista en una cadena JSON
print(json_string)  

mostrar = json.loads(json_string) # Lectura de un JSON en objeto Python 
print(mostrar)

# Abre el archivo JSON en modo de lectura
with open('JSON.json', 'r') as archivo:
    datos = json.load(archivo)  # Carga el contenido del archivo JSON en un diccionario

# Muestra el contenido cargado
print(datos)

class Pais: pass 
pais = Pais() 
pais.nombre = "España"
pais.capital = "Madrid"

#* Todo en code JSON deve heredar de JSONENcoder
class PaisEncoder(json.JSONEncoder):
    #No es el metodo encode el que esta sobracargado, sino este ,cuyo objetivo es devolver un tipo basico serializable(aqui un diccionario)
    def  default(self, objeto):
        #es una buena practica que un encoder solo sea responsable del procesado de un unico tipo de objeto 
        if isinstance(objeto,Pais):
            return objeto.__dict__ #¿Qué es __dict__?En Python, cada objeto tiene un atributo especial llamado __dict__, que es un diccionario que almacena todos los atributos y sus valores de ese objeto.
                                    #Por ejemplo, si tienes un objeto de la clase Pais, su __dict__ contendrá todos los atributos que se le han asignado, en este caso nombre y capital.
        else:
            # Dejamos que la clase base se encargue de desencadenarrel error adecuado 
            return json.JSONEncoder.default(self, objeto)
        
print(PaisEncoder().encode(pais))       
