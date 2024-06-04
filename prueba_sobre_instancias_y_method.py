class Circulo:
    def perimetro (self):

        return 2 * 3.14 * self.radio
    
c = Circulo()
c.radio = 2
p = c.perimetro
print(p())

f=Circulo.perimetro
print(f(c))
print(callable(f))

methods_circle =[ Circulo.perimetro]

for m in methods_circle:
    print(m(c))
print(Circulo.perimetro(c))