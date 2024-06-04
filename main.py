from formas_concretas import Circulo, Cuadrado
from formas_concretas import formas
#* Recorrer la lista de formas , sin preocuparse de que forma concretas son
for forma in formas:
    print(forma.perimetro())

#* Clase que no hereda de la clase base Forma
class Chucrut:
    #* Definicion de un metodo con el mismo prototipo
    #* que el sobrecargo en Forma
    def perimetro(self):
        return "Ningun informe"
    
#Declaracion de una lista de formas que tambien contiene 
#una instancia deesta nueva clase "Incongruente "

formas = [Circulo(3), Cuadrado(2), Cuadrado(5), Chucrut()]

#* Recorrido de la lista como si no hubiera pasado nada
for forma in formas :
    print(forma.perimetro())