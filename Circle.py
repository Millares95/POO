class Circle :
    def perimeter (self):
        # Definicion del cuerpo del metodo,
        #em la ocurrencia con un valor de retorno 
        return 2*3.14 *self.radio

c = Circle()
c.radio = 2
print(c.perimeter())

