class Automovil:
    def __init__(self):
        # Declaración de una lista que puede 
        # contener las ruedas del automóvil.
        self.rueda = []

    def agregarRueda (self, rueda):
        #* Si la rueda contiene menos de cinco elementos 
        if len (self.rueda) < 5 :
        #*... anadimos la reuad dad como argumento 
            self.rueda.append(rueda)
            #* Aprovechamos para acutalizar la realacion 
            #* entre la reuad y le automovil 
            rueda.automovil = self
        else:
            print("El automovil tiene ya 5 ruedas")
class Rueda :
    def __init__(self) -> None:
        # Declaración de un atributo que contiene una referencia 
        # al automóvil con el que está relacionada la rueda.
        self.automovil = None

#* Creación de una lista con cuatro instancias de Rueda.
ruedas = [Rueda() for i in range(4)]
#* Creación de una instancia de Automovil.
automovil = Automovil()

#*Asignación de la lista de ruedas al Automóvil
automovil.ruedas = ruedas 

#* Para cada rueda de la lista...
for rueda in ruedas :
    #* ... se le asocia el automovil 
    rueda.automovil = automovil

# print("Instancia de automovil : {}".format(automovil))
# print("Las cuatro ruedas del automovil son : {}".format(automovil))
# print("Las 4 ruedas del automovil son {} son {}".format(automovil,automovil.ruedas))
# print("El automovil de la rueda {} es {}".format(ruedas[0],ruedas[0].automovil))

print(automovil.ruedas)
del automovil
print(ruedas)