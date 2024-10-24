
# class MetaSingleton(type):
#     __instancia = None
#             #cls es la clase de instancia 
#     def __call__ (cls):
#             #  si el atributo de la clase a intanciar es nulo 
#         if cls.__instancia is None:
#             #Esto significa que la instancia de Singleton (cls)
#             # aun no ha sido creada . Entonces la creamos .Utilizamos super() para respetar la jerarquia de clases 
#            cls.__instancia = super(MetaSingleton,cls).__class__()
#             #aqui necesariamente se cre la instancia de cls 
#             #por tanto, podemos devolverla 
#         return cls.__instancia



# class Singleton(metaclass=MetaSingleton):
#     pass

# Singleton1 = Singleton()
# Singleton2 = Singleton()
# print(Singleton1)
# print(Singleton2)
# *------------------------------------------- USANDO DECORADOR---------------------------------------------

# Definicion del decorador 
class Singleton:
    #Fabricante del decorador
    #Toma la clase decorada como parametro
    def __init__(self, decorated):
        #Conservamos una referencia sobre la clase decorada
        #para que pueda instanciarla mas tarde
        self._decorated = decorated 
    def Instance(self):
        #Intentamos acceder a la instancia de Singleton 
        try:
            return self._instancia
        except AttributeError:
            #Las excepcion se desencadena si el atributo no está 
            # definido. Esto significa que la instancia se Singleton 
            # no se ha creado.Por lo tanto,se debe crearse aqui.
            self._instancia = self._decorated() 
            #Se devuelve la instancia única 
            return self._instancia
    def __call__(self):
        # la sobrecarga de __call__ permite prohibir
        #la instanciacion  "salvaje"
        raise TypeError( "Para recuperar la instancia de Singleton, \ utilizar 'Instance'()'." )
        
#Decorador
@Singleton
#Definici'on de la clase Impresora
class  Impresora:
    pass

# i1 = Impresora()
i1 = Impresora.Instance()
i2 = Impresora.Instance()

print(i1 is i2)