# Definición de una clase abstracta para poder visitar los diferentes objetos a serializar en XML.
class Visitable:
    def acepta(self, visitante):
        nombre_metodo = 'visita' + self.__class__.__name__
        metodo = getattr(visitante, nombre_metodo, getattr(visitante, 'default', None))
        if metodo:
            return metodo(self)
        else:
            raise NotImplementedError(f"No se ha implementado el método '{nombre_metodo}' en el visitante.")

# Propietario del vehículo, visitable y que contiene solo el nombre.
class Propietario(Visitable):
    def __init__(self, nombre):
        self.nombre = nombre

# Un equipamiento del vehículo, visitable y que solo contiene el tipo de equipamiento.
class Equipamiento(Visitable): 
    def __init__(self, tipo): 
        self.tipo = tipo

# Coche, visitable y conteniendo su nombre, su propietario y una lista de equipamientos.
class Coche(Visitable):
    def __init__(self, nombre):
        self.nombre = nombre
        self.propietario = Propietario('Emmett Brown')
        self.equipamientos = [Equipamiento('Convector temporal'), 
                              Equipamiento('Generador de fisión')]

class VisitanteXML:
    # Método de visita de un Coche.
    def visitaCoche(self, coche):
        # Se escribe la etiqueta XML de apertura así como el atributo 'nombre'.
        print("<Coche nombre='{}'>".format(coche.nombre))
        # Se visita el propietario.
        coche.propietario.acepta(self)
        # Se escribe la etiqueta XML de apertura de los equipamientos.
        print("<Equipamientos>")
        # Se recorren los equipamientos del coche...
        for equipamiento in coche.equipamientos:
            # ...y los visita.
            equipamiento.acepta(self)
        # Se cierra la etiqueta de equipamientos y del coche.
        print("</Equipamientos>")
        print("</Coche>")

    # Método de visita de un propietario.
    def visitaPropietario(self, propietario):
        # Escribimos la etiqueta XML correspondiente, con el nombre del propietario como contenido textual.
        print("<Propietario>{}</Propietario>".format(propietario.nombre))

    # Método de visita de un equipamiento.
    def visitaEquipamiento(self, equipamiento):
        # Escribimos la etiqueta XML correspondiente, con el tipo de equipamiento como atributo.
        print("<Equipamiento tipo='{}' />".format(equipamiento.tipo))

# Creación del visitante.
visitante = VisitanteXML()
# Creación del Coche, objeto a visitar.
delorean = Coche('delorean')
# Inicio de la visita.
delorean.acepta(visitante)
