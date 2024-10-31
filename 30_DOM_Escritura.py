from xml.dom.minidom import parse 
# Analysis to XML file
mi_XML = parse('XML.xml')
# Recuperacion del nodo "Propietario"
propietario = mi_XML.getElementsByTagName('Propietario')
# Modificacion del texto del primer (y unico) hijo.
propietario[0].firstChild.data = "Doc Emmett Brown"
#Visualizacion del numero contenido XML "limpio" (con indentaciones y retornos de lineas)
print(mi_XML.toprettyxml())
