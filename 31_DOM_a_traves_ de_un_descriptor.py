from xml.dom.minidom import parse
import sys 
ruta_del_archivo = 'XML.xml'
# Analisi del archivo XML
mi_XML = parse(ruta_del_archivo)

#Recuperacion del nodo 'Propietario'
propietario = mi_XML.getElementsByTagName('Propietario')

#Modificacion del texto del primer (y unico ) hijo
propietario[0].firstChild.data = 'Doc Emmett Brown'

try:
    #Apertura del archivo en modo escritura 
    archivo_XML = open(ruta_del_archivo, 'w') #'w' para poder escribir
#Escritura del nuevo contenido XML
    mi_XML.writexml(archivo_XML)
    #Cierre del archivo 
    archivo_XML.close()
except:
    print("Error:", sys.exc_info()[0])  

