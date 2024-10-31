import xml.sax
"""Especialización de la clase ContentHandler encargada llamar a algunos métodos basados en el elemento XML analizado actualmente."""

class MiHandlerSAX(xml.sax.ContentHandler):
    # Metodo llamado al abrir una etiqueta XML, los parametros son el nombre de la etiqueta y la lista de sus atributos 
    def startElement(self, name, attrs):
        #Se muestra el nombre
        print(f"Elemento" ,name)
        #Para cada atributo 
        for (clave, valor) in attrs.items():
            #.... se muestra su nombre y su valor 
            print('Atributo:', clave, "=", valor )
# Metodo llamado cunado el analizado esta en un elemnto de texto comprendiendo entre una etiqueta de apertura y su contraparte de cierre.
# El parametro es el texto en cuestion
    def  endElement(self, content):
        #strip() permite elimimar los caracteres en blanco al principio y al final de una cadena.
        #  Si, una vez que se eliminan estos , espacios en blanco la cadena no esta vacia...
        if content.strip():
            #... la mostramos.
            print("texto:",content)
# Instanciación de la clase ContentHandler personalizada en función de las necesidades.
mi_handler = MiHandlerSAX()
# Análisis del archivo XML.
xml.sax.parse('XML.xml', mi_handler)
