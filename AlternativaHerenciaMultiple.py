'''Enunciado: comenzando con el mismo código que el ejercicio
sobre herencia múltiple, cree una clase que agrupe el comportamiento 
común entre las clases Ventana y ParedCortina.'''

class Pared:
    def __init__(self, orientacion) -> None:
        self,orientacion = orientacion
        # Una pared no tiene nunca una ventana por defecto
        self.ventana = []

    def ventanas(self):
        return self.__ventanas
    
    def superficie_acristalada(self):
        superficie = 0 
        for ventana in self.ventanas(): 
            superficie += ventana.superficie() 
        return superficie

class Ventana:
    def __init__(self, pared, superficie, proteccion ) -> None:
        # *'Ventana' delega la gestión de la superficie acristalada 
        #* a 'Cristal', que es privada
        self.__cristal = Cristal(superficie)
        self.pared = pared
        # Se "añade" la ventana a la pared dada como argumento
        self.pared.ventana.append(self)
    def superficie(self):
        return self.__cristal.superficie()
    
class Casa:
    def __init__(self, paredes) -> None:
        self.paredes = paredes 

    def paredes(self):
        return self.__paredes 
    
    def superficie_acristalada(self):
        superficie = 0
        for pared in self.paredes():
            superficie += pared.superficie_acristalada()
        return superficie

class ParedCortina(Pared, Ventana):
    def __init__(self, orientacion,superficie) -> None:
        # Llamada al constructor de pared para tener una instancia 
        # sobre la que "añadir" el componente "ventana"
        Pared.__init__(self, orientacion)
        # No más uso polémico de 'self' 
        # como su propia pared. 
        self.__cristal = Cristal(superficie)
        Ventana.__init__(self, self, superficie)

class Cristal:
    def __init__(self, superficie) -> None:
        self.__superficie = superficie

    def superficie (self):
        return self.__superficie