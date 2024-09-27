"""Ejercicio 1: Definición y Uso de Clases
Crea una clase Perro con los siguientes atributos: nombre, edad y raza. Añade un método llamado ladrar que imprima el mensaje "Guau!"."""

# class  Perro:
#     def __init__(self,nombre,edad,raza) -> None:
#         self.nombre = nombre
#         self.edad = edad
#         self.raza = raza 
#     def ladrar(self):
#         print("Guau")

# perro1 = Perro("Budy",10,"pequine")
# perro1.ladrar()

"""Ejercicio 2: Métodos con Parámetros 
Crea una clase Coche con atributos como marca, modelo, y velocidad. Añade un método acelerar que incremente la velocidad y otro método frenar que la disminuya."""

# class Coche:
#     def __init__(self,marca,modelo,velocidad) -> None:
#         self.marca = marca
#         self.modelo = modelo
#         self.velocidad = velocidad
    
#     def acelerar(self, incremento):
#         print("aumentar la velocidad")
#         self.velocidad +=  incremento
#         print(self.velocidad)

#     def frena(self,decremento):
#         print("disminuye velocidad")
#         self.velocidad  -= decremento
#         print(self.velocidad)

# carro1 =Coche("Lada",29,100)
# acelerar = carro1.acelerar(50)
# frena = carro1.frena(10)

"""Ejercicio 3: Métodos de Clase vs Métodos de Instancia
Crea una clase CuentaBancaria con atributos titular y saldo. Añade un método de instancia depositar que sume dinero al saldo,
y un método de clase tasa_interes que devuelva una tasa de interés estándar para todas las cuentas."""

# class CuentaBancaria:
#     tasa_fija = 4/100

#     def __init__(self,titular,saldo) -> None:
#         self.titular = titular
#         self.saldo = saldo

#     def depositar(self,dinero):
#         self.saldo = self.saldo + dinero
#         print(f"el aumento del dinero fue de {self.saldo}")

#     @classmethod
#     def tasa_interes(cls,saldo):
#         tasa =saldo * cls.tasa_fija
#         print(f'el descuento es de {tasa}')

# c = CuentaBancaria
# cuenta1 = c("Lazaro",4650)
# cuenta1.depositar(1200)
# c.tasa_interes(cuenta1.saldo)

"""Ejercicio 1: Destructores
Crea una clase Libro que tenga los atributos titulo, autor y paginas. Añade un método __del__() 
que imprima un mensaje cuando un objeto de la clase se destruya, por ejemplo, "Libro eliminado". Luego, crea y elimina un objeto de esta clase."""

# class Libro:

#     def __init__(self,titulo,autor,pagina) -> None:
#         self.titulo = titulo
#         self.autor = autor
#         self.pagina = pagina
    
#     def __del__ (self):
#         print("Libro Eliminado")

# M = Libro
# libro1 = M("Quijote","cervantes",213)
# print(libro1.autor)

"""Ejercicio 3: Diferencias entre Métodos de Clase e Instancia
Crea una clase Rectangulo con atributos largo y ancho. Añade un método de instancia area() que devuelva el área del rectángulo. Luego, 
añade un método de clase crear_cuadrado(cls, lado) que devuelva un objeto de tipo Rectangulo con largo y ancho iguales."""

# class Rectangulo :
#     def __init__(self, largo , ancho) -> None:
#         self.largo = largo
#         self.ancho = ancho
#         print(f'los lados son {self.largo} y {self.ancho}')

#     def area(self):
#         A = self.largo * self.ancho
#         print(f'El area del rectangulo es {A}')
#     @classmethod
#     def crear_cuadrado(cls,lado):
#         return cls(lado,lado) #TODO en este caso el cls se puede sustituir por el nombre de la clase (RECTANGULO)
    
# poligono1 = Rectangulo(4,6)
# poligono1.area()

# cuadrado = Rectangulo.crear_cuadrado(4)
# cuadrado.area()



"""Ejercicio 4: Métodos con Valores por Defecto
Crea una clase Empleado con los atributos nombre y salario. Añade un método mostrar_datos que imprima los datos del empleado.
 Si no se proporciona un salario, debe usar un valor por defecto de 1000."""

# class Empleado:
#     def __init__(self,nombre,salario = 1000) -> None:
#         self.nombre = nombre
#         self.salario = salario
#     def mostrar_datos(self):
#         print(f"El nombre del usuario es {self.nombre} el salario es de {self.salario}")

# empleado1 = Empleado("carlos",34500)
# empleado1.mostrar_datos()

"""Ejercicio 5: Comparación entre Objetos
Crea una clase Punto que represente un punto en un plano cartesiano, con los atributos x y y. Añade un método comparar que compare si dos puntos son iguales (tienen la misma x y y)"""

# class Punto:
#     def __init__(self,x=0,y=0) -> None:
#         self.x = x 
#         self.y = y
#     @classmethod
#     def comparar(cls,pto1,pto2):
#         if pto1.x == pto2.x and pto1.y == pto2.y:
#             print('True')
#         else:
#             print("false")
    
# punto1 = Punto(9,5)
# punto2 = Punto(9,5)
# comparar = Punto.comparar(punto1,punto2)


"""Ejercicio 6: Métodos Estáticos
Crea una clase Calculadora con un método estático sumar(a, b) que reciba dos números y devuelva la suma. Añade un método de instancia multiplicar(a, b)
que devuelva el producto de dos números. Luego, crea una instancia de Calculadora y utiliza ambos métodos."""

# class Calculadora: 
#     @staticmethod
#     def suma (a,b):
#         return a+b
# resultado = Calculadora.suma(5, 6)
# print(resultado)

"""Ejercicio 9: Clases y Métodos de Clase
Crea una clase Coche con atributos marca, modelo y un atributo de clase total_coches. Cada vez que se cree una nueva instancia de Coche,
el atributo total_coches debe incrementarse en 1. Añade un método de clase mostrar_total() que imprima cuántos coches han sido creados."""

# class Coche:
#     total_coches = 0 
#     def __init__(self, marca , modelo) -> None:
#         self.marca = marca
#         self.modelo = modelo
#         Coche.total_coches += 1

#     @classmethod
#     def mostrar_total(cls):
#         print(f'Total de coches {cls.total_coches}')



"""Ejercicio 10: Uso de Self
Crea una clase Circulo con el atributo radio. Añade un método area() que calcule y devuelva el área del círculo usando self.radio.
Luego, añade un método de clase mostrar_formula_area() que imprima la fórmula del área de un círculo."""
# import math
# class Circulo:
#     def area(self, radio ):
#         self.radio = radio
#         area = (self.radio)**2 * math.pi 
#         print(f"El calculo del area es {area}")

# circulo = Circulo()# TODO es necesario crear una instancia del metodo en este caso para poder llamarlo 
                     # TODO  porque se esta trabajando con un metodo de instancia y por tanto se hace necesario instanciar el objeto primero
# circulo.area(3)

# class Circulo1:
#     @staticmethod
#     def area(radio):
#         area = radio**2 * math.pi
#         print(f'El area aplicando el metodo estatico es {area}')
# Circulo1.area(3)