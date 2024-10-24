class Visitante:
    #El segundo parametro corresponde al visitante
    #vistando la clase
    def acepta(self, visitor):
        #se recupera el nombre de la clase actual
        class_name = self.__class__.__name__

        # el metodo getattr() recuperará, en la instancia del visitante,el metodo cuyo nombre es 'visita'
        #despues el nombre de la clase . Si tal miembro no existe,se selecciona el metodo default()
        method = getattr(visitor, 'visit' + class_name,visitor.default)
        #llamamos a este metodo con la instanica del visitable como parametro
        return method(self)
    
class Entidad(Visitante):
    pass
class Imagen(Entidad):
    def __init__(Entidad):
        def __init__(self, src, alt):
            #la URL origen de la imagen
            self.src =src 
            #El texto alternativo de la imagen
            self.alt = alt
class Enlace(Entidad):
    def __init__ (self, href, text):
        #El enlace hipertexto
        self.href = href
        #El texto que aparece en el enlace
        self.text = text
# La clase siguiente representa un ejemplo de visitante, transforma cad entida den uan caden de caracteres que se corresponden con su representacion en HTML
#La clase abstracta VisitanteEntidad no es un requisito de diseño y solo se describe aquí para mayor claridad.

class VisitanteEntidad: 
    def visitaImagen(self, imagen): 
        pass 

    def visitaEnlace(self, enlace): 
        pass


class RepresentacionHtml(VisitanteEntidad):
    def visitaImagen(self, imagen):
        return f'<img src="{imagen.src}" alt="{imagen.alt}">'

class AnalizadorDeEnlace(VisitanteEntidad):
    def __init__(self):
        #Se define un conjunto vacion que recuperara 
        #los enlaces de lapagina HTML
        self.enlaces = set()

        def visitaEnlace(self, enlace):
            #Agregamos el enlace que estamos visitando a nuestro conjunto de enlaces
            self.enalces.add(enlace.href)

entidades = CrearEntidades() 
representacion = RepresentacionHtml() 
analizador = AnalizadorDeEnlace()
for entidad in entidades: 
    print(entidad.acepta(representacion)) 
    entidad.accept(analizador) 
print(analizador.enlaces)