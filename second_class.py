# class Circulo:
#     # Declaracion de un atributo de clase 'radio'
#     #al que se le asigna el valor 2 
#     radio = 2 
# print(Circulo.radio)

class Circulo:
    # El cuerpo de la clase se deja vacio 
    pass 
Circulo.radio = 2
# print(Circulo.radio)

c = Circulo()
# print(c.radio)
# c = Circulo()
# c.radio = 5 
# print(c.radio)
# del(c)
# print(c.radio)

c.radio = 4
print(c.radio)
print(Circulo.radio)
Circulo.radio = 6 
print(Circulo.radio)
print(c.radio)