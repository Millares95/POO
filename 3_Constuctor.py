class MyClass:
    # Declaración del constructor de MyClass 
    # como un metodo clasico 
    def __init__(self):
        self.alpha = 1
        print("constructor about MyClass")
        pass

instancia = MyClass()
i = MyClass()
print(i.alpha)

class Circulo :
    def __init__(self,radio) -> None:
        self.radio =radio

    def diametro(self):
        return self.radio * 2
# Creacion de un círculo cuyo # * constructor  recibe como argumento
#* (ademas de self ) la longuitud de su radio

c = Circulo(3)
print(c.diametro())