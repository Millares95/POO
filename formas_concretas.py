from 9_forma import Forma
#* Una clase derivada
class Cuadrado (Forma):
    def __init__(self,lado) -> None:
        self.lado = lado

    #* Sobrecarga del metodo de base
    def perimetro(self):
        return 4  * self.lado
    
    #* Otra clase derivada
class Circulo(Forma):
    def __init__(self,radio) -> None:
        self.radio = radio

    #* Una nueva sobrecarga del metodo base
    def perimetro(self):
        return 2 * 3.14 * self.radio
        
#* Creacion de una lista de formas concretas 
formas = [Circulo(3), Cuadrado(2), Cuadrado(5)]
