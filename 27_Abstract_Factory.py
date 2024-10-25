# class ModeloDeJuego:
#     #Método de creación de un DiarioDeAbordo
#     def crear_diario(self):
#         pass 
#     #Metodo de creacion de una representacion 
#     def crear_representacion(self):
#         pass 

# class ModoDebug(ModeloDeJuego):
#     #Metodo de de creacion de un DiarioDeAbordo dedicado al modo debug
#     def crear_diario(self):
#         return DiarioDebug()
#     #Método de creación de una representación dedicada al modo debug
#     def crear_representacion(self):
#         return RepresentacionDebug()


# class ModoRelease (ModoDeJuego):
#     #Metodo de creacion de un DiarioDeAbordo dedicado al modo Release
#     def crear_diario(self):
#         return DiarioRelease()
#     #Metodo de creacion de una Representacion dedicada al modo Release
#     def crear_representacion(self):
#         return RepresentacionRelease()

#* Cuando se inicializa el juego, lo único que tiene que hacer es crear el ModoDeJuego deseado y pasarlo al resto del código: 
#* la creación de las instancias deseadas de DiarioDeAbordo y Representacion se ocultará detrás de la abstracción que es ModoDeJuego. 
#* Así, los diferentes módulos del juego no tendrán que saber en qué modo se encuentra el juego: confiarán en la instancia de ModoDeJuego 
#* que creará los objetos adecuados para ellos.

"""Enunciado: Implementar un programa que factura productos por valor de 100, con la tasa de IVA correcta, según sean productos de alimentación o servicios.
Comportamiento esperado:"""
from enum import Enum

class Naturaleza(Enum):
    ALIMENTARIA = 1
    SERVICIO = 2

class Producto:
    def __init__(self, naturaleza):
        self.naturaleza = naturaleza
        self.precio_bruto = 100
from abc import ABCMeta, abstractmethod

class FacturaProducto(metaclass = ABCMeta):
    def __init__(self, precio_bruto):
        self.precio_bruto = precio_bruto

    @abstractmethod
    def facturar(self):
        pass

class FacturaAlimentaria(FacturaProducto):
    def facturar(self):
        return self.precio_bruto * (1 + 0.055)
    
class FacturaServicio(FacturaProducto): 
    def facturar(self): 
        return self.precio_bruto * 1.2
    
class FactoryFactura:
    def crear(producto):
        precio_bruto = producto.precio_bruto
        seleccion_facturas = { 
 Naturaleza.ALIMENTARIA: FacturaAlimentaria(precio_bruto),
            Naturaleza.SERVICIO: FacturaServicio(precio_bruto)}
        return seleccion_facturas.get(producto.naturaleza, "Naturaleza desconocida")
    
producto = Producto(Naturaleza.ALIMENTARIA) #IVA 5.5%
precio_neto = FactoryFactura.crear(producto).facturar()
print(precio_neto)#10.5

producto = Producto(Naturaleza.SERVICIO) #IVA 20%
precio_neto = FactoryFactura.crear(producto).facturar()
print(precio_neto) #120