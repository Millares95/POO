#La clase base
class Forma :
    #* el metodo polimorfico , que sera especializado 
    #* para cada clase  derivada 
    def perimetro(self):
        # Mensaje de error
        raise NotImplementedError("imposible calcular el perimetro de unadomra genetica ")
    