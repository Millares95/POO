class Casa:
    def __del__(self):
        print("destruccion Casa")

    def __init__(self):
        # Declaración de una lista de instancias de Habitacion
         # con nombres diferentes.
        self.habitaciones = [Habitacion (name) for name in ['Cocina', 'Dormitorio', 'Salon' ]]

class Habitacion:
    def __del__(self):
        print('Destruccion {}'.format(self.name))
    
    def __init__(self) -> None:
        print('Destruccion {}'.format(self.name))
    
    def __init__(self, name):
        self.name = name 

casa = Casa()

# #* Variable que referencia a la instancia de la primera habitación 
# #* de la casa (en este caso, la cocina).
# cocina = casa.habitaciones[0]
# print(casa.habitaciones[0])
# del casa

# print(cocina)