class Pared:
    def __init__(self, orientacion) -> None:
        self,orientacion = orientacion
        # Una pared no tiene nunca una ventana por defecto
        self.ventana = []

class Ventana:
    def __init__(self, pared, superficie) -> None:
        self.pared = pared
        self.superficie = superficie
        # Se "añade" la ventana a la pared dada como argumento
        self.pared.ventana.append(self)
class Casa:
    def __init__(self, paredes) -> None:
        self.paredes = paredes 
    
    def superficie_acristalada(self):
        superficie = 0
        for pared in self.paredes:
            for ventana in pared.ventanas:
                superficie += ventana.superficie
        return superficie
#----------------------------------------------------------------------------
class ParedCortina(Pared, Ventana):
    def __init__(self, orientacion,superficie) -> None:
        # Llamada al constructor de pared para tener una instancia 
        # sobre la que "añadir" el componente "ventana"
        Pared.__init__(self, orientacion)
        # Llamada al constructor de Ventana, con 'self' como primer
        # argumento 'pared' (porque una ParedCortina es una Pared)
        Ventana.__init__(self, self, superficie)
#-------------------------------------------------------------------------------------------------------