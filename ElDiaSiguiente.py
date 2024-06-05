'''Enunciado: modelar lo siguiente.Una empresa es propietaria de varios edificios
y emplea a varios empleados. Un edificio está necesariamente ubicado en una
ciudad y una ciudad está formada por varios edificios. Empresa, empleado, 
ciudad y edificio tienen cada uno un nombre. Estas ciudades incluyen New York, 
donde se encuentran los edificios A y B, y Los Ángeles, donde está el edificio C.
Estos tres edificios son propiedad de YooHoo! que emplea a los Sres. Martin,
Salim y la Sra. Xing. Una vez definidas estas entidades, imagine que su
programa es una película estadounidense de catástrofes, en la que se 
destruye New York. Implemente este evento para que todas las entidades 
del juego tengan en cuenta las consecuencias de este cataclismo.'''

class Ciudad :
    def __init__(self , nombre):
        self.nombre = nombre
        self.edificios = []

    def __del__(self):
        print("Destrucci'on de {}".format(self.nombre))

class Edificio:
    def __init__(self, nombre):
        self.nombre = nombre 
    
    def __del__(self):
        print("Destruccion de {}".format(self.nombre))
    
class Empresa:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.edificios = []
        self.empleados = []

    def __del__(self):
        print("Declaracion de bancarrota de {}".format(self.nombre))
    
    def contrata(self, empleado):
        self.empleados.append(empleado)

    def numeroDeEdificios(self):
        print("{} tiene {} edificio(s)".format(self.nombre,len(self.edificios)))

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def __del__(self):
        print("Fallecimiento del {}".format(self.nombre))

# Instanciación de la ciudad de New York.
ny = Ciudad("New York")
# Asignación de una lista de nuevas instancias de Edificio 
# a la ciudad.
ny.edificios = [Edificio("A"), Edificio("B")]
# Idem para Los Ángeles.
lax = Ciudad("Los Ángeles")
lax.edificios = [Edificio("C")]
# Instanciación de la empresa.
empresa = Empresa("YooHoo!")
# Asignación de una lista de instancias de Edificio ya existentes # en la empresa.
empresa.edificios = [ny.edificios[0], ny.edificios[1], lax.edificios[0]]
# Instanciación de nuevos empleados.
martin = Empleado("Martin")
salim = Empleado("Salim")
xing = Empleado("Xing")
[empresa.contrata(empleado) for empleado in [martin, salim, xing]]
## Si destruimos la instancia Ciudad, los edificios A y B
# no se destruyen porque se hace referencia a ellos en la lista 
# empresa.edificios. Por tanto, se deben eliminar de esta lista 
# para que los edificios queden bien destruidos con la ciudad. 
# Esta función realiza esta tarea.

def destruirEdificiosEmpresa(ciudad):
    #Para todos los edificios de la ciudad destruida 
    for edificio in ciudad.edificios:
        # ...si el edificio forma parte de los edificios
        # de la empresa...
        if edificio in empresa.edificios:
            # ...se retira este edificio del patrimonio de la empresa.
             empresa.edificios.remove(edificio)   

empresa.numeroDeEdificios()

# Eliminación de la única referencia a la instancia de New York 
