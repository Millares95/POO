from xml.dom.minidom import parse

# Análisis del archivo XML
mi_XML = parse('XML.xml')
# Recuperacion de la raiz del arbol, es decir, del primer nodo
raiz_del_XML = mi_XML.childNodes[0]
# A partir de este nodo, se puede leer el atributo 'nombre'..\
nombre_coche = raiz_del_XML.getAttribute('nombre')
# ... y se visualiza.
print(nombre_coche)

# Se recuperan los hijos del nodo raíz.
lista_de_los_hijos = raiz_del_XML.childNodes
# Recorremos estos hijos
for hijos in lista_de_los_hijos:
 # Nos aseguramos de que el nodo sea un elemento y no # algo más, como un comentario o contenido. 
    if hijos.ELEMENT_NODE != hijos.nodeType:
        continue
    # Si el nodo lleva el nombre 'Propietario'...
    if 'Propietario' == hijos.nodeName:
    # ... se recupera el primer hijo, es decir, el nodo # que representa el texto.
        nombre = hijos.firstChild
    # Comprobamos que el nodo existe y, si efectivamente es un # nodo de tipo TEXT_NODE, es decir, 
    # texto escrito # entre una etiqueta de apertura y una etiqueta de cierre ...
        if None != nombre and nombre.TEXT_NODE == nombre.nodeType:
          # ... se muestra el texto del nodo.
          print(nombre.data) # (1)
        # Si el nodo tiene el nombre 'Equipamientos'...
    elif "Equipamiento" == hijos.nodeName:
        # ... se recuperan los hijos de este nodo 
        lista_de_los_equipamientos = hijos.childNodes
        # Se recorren estos hijos.
        for equipamiento in lista_de_los_equipamientos:
            # Se asegura que se trata de un ELEMENT_NODE.
            if equipamiento.ELEMENT_NODE != equipamiento.nodeType:
                continue
            # Si el nodo tiene el nombre 'Equipamiento'...
            if 'Equipamiento' == equipamiento.nodeName: 
                # ... se recupera el atributo llamado 'tipo'... 
                tipo = equipamiento.getAttribute('tipo') 
                # ... y lo mostramos. 
                print(tipo) # (2)

