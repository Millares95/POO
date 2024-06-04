 #! Definicion de la clase de base 
class Forma:
    #* Constructor de la clase de base 
    def __init__(self) -> None:
        print("Init Forma")
        #* Inicializacion de los atributos de instancia 
        self.x = 0
        self.y = 0

#! Definicion de la clase derivada
class Circulo (Forma):
    #* Constructor de la case derivada, que no llama 
    #* al constructor de la case de base 
    def __init__(self) -> None:
        #* LLamada explicita al constructor de la clase de base.
        # Forma.__init__(self)
        super().__init__()
        print("init circulo",self)   

c = Circulo()
print(c.x ,c.y)
f = Forma()

print(type(c))
print(type(f))
print(isinstance(c, Circulo)) #c es una instancia de circulo 

# -----------------------------------------------------------------------------------
