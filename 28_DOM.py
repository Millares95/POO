 #* Cambiar este import en parseString en función de las necesidades.
from xml.dom.minidom import parse 
#* Analisis del archivo dado y asignacion del resultado en una variable 
mi_XML = parse('XML.xml')

#* Recuperacion en una lista de los elementos XML cuya etiqueta se llama "Equipamiento"
lista_de_los_equipamientos = mi_XML.getElementsByTagName('Equipamiento')

#*Recorrido de esta lista
for equipamiento in lista_de_los_equipamientos:
    #* Mostar el atributo 'tipo' del equipamiento en cuestion 
    print(equipamiento .getAttribute('tipo'))
