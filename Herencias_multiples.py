 #* Una primera clase base 
class Druida:
    def __init__(self) -> None:
        #* Llamar al constructor de la clase siguiente
        #* en la lista __mro__(Ladron en este ejemplo).
        super().__init__()
        self.magia = 4

#* Una segunda clase base 
class Ladron:
    def __init__(self) -> None:
        #* Llamada al constructir de la clase siguiente
        #* en la lista __mro__(ojbect en este ejemplo).
        super().__init__()
        self.habilidad = 7
    
#* Una clase derivada doble
class Heroes(Druida, Ladron):
    pass

h = Heroes()
# print(isinstance(h,Ladron)) # h es una instancia de ladron 
# print(isinstance(h,Druida)) # h es una instancia de Druida

print(h.magia)
print(h.habilidad)

#* __mro__ es un atributo de clase al que no se puede 
#* acceder a traves de una instancia. Lo que es "logico"
#* el algoritmo MRO trabajoa sobre los ancestros de una clase ,
#* no de una instancia 
print(Heroes.__mro__)
