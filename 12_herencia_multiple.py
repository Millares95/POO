class Druida(object):
    def pv_base(self):
        return 5
    
    def pv(self):
        return self.pv_base() * 2 # Coef para Druida

class Ladron(object):
    def pv_base(self):
        return 15
    
    def pv(self):
        return self.pv_base() * 3 #Coef para Ladron

class Heroe(Druida, Ladron):
    def pv(self):
        return (super(Heroe, self).pv_base() * 2 + super(Druida,self).pv_base() * 3) / 2  # aqui por el mro estoy llamando realmente  a Druida y Ladron que podria sustituir super(Druida,self).pv_base() * 3) por #* Ladron.pv_base(self) * 3)
h = Heroe()
print(h.pv())
print(Heroe.__mro__)