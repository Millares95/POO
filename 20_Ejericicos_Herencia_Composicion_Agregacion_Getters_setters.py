# """ 5. Herencia Múltiple con Métodos Personalizados
# Ejercicio 5: Crea una clase Animal, y dos clases que hereden de ella (Perro y Gato),
#  luego una clase que herede de ambas (PerroGato) y personaliza los métodos."""

# class  Animal:
#     def __init__(self, nombre) ->  None:
#         self.nombre  = nombre
    
# class Perro(Animal):
#     def  __init__(self, nombre, raza) -> None:
#         super().__init__(nombre)
#         self.raza  = raza

# class Gato(Animal):
#     def __init__(self, nombre,forma) -> None:
#         super().__init__(nombre)
#         self.forma = forma

# class  PerroGato(Perro,Gato):
#     def __init__(self, nombre, raza, forma) -> None:
#     # Llamamos al inicializador de la clase base de Perro
#         Perro.__init__(self, nombre, raza)
#     # Llamamos al inicializador de la clase base de Gato
#         Gato.__init__(self, nombre, forma)


# """Ejercicio 6: Modifica el ejercicio de Murciélago para que tenga un getter y setter para modificar una característica única (como tipo_de_ala)."""

# class Ave:
#     def volar(self):
#         return "Puede volar"
    
# class Mamifero:
#     def  __init__(self,__tipo_de_ala) -> None:
#         self.__tipo_de_ala = __tipo_de_ala
    
#     def get_tipo_de_ala(self):
#         return self.__tipo_de_ala
    
#     def set_tipo_de_ala(self,nuevo_tipo_de_ala):
#         self.__tipo_de_ala = nuevo_tipo_de_ala

#     def amamantar(self):
#         return "Amamanta a sus crías"

# class Murcielago(Ave, Mamifero):
#     def __init__(self, tipo_de_ala) -> None:
#         Mamifero.__init__(self, tipo_de_ala)
#     pass

# # Instancia y prueba
# murcielago = Murcielago()
# print(murcielago.volar())  # Salida: Puede volar
# print(murcielago.amamantar())



# # *Ejercicio 7: Crea una clase Libro y una clase Biblioteca que use agregación para almacenar libros. Agrega getters y setters para los libros.
# class Libro:
#     def __init__(self, titulo, autor, año_publicacion) -> None:
#         self.titulo = titulo
#         self.__autor = autor
#         self.año = año_publicacion
    
#     def  get_autor(self):
#         return self.__autor 
    
#     def set_autor(self, new_autor):
#         self .__autor = new_autor

# class Biblioteca:
#     def __init__(self) -> None:
#         self.libros =[]
    
#     def agregar_libros(self, titulo, autor, año_publicacion):
#         nuevo_libro = Libro(titulo, autor, año_publicacion)
#         self.libros.append(nuevo_libro)



# Ejercicio 8: Implementa una clase Rectángulo con métodos para obtener y establecer la longitud y el ancho.

# Ejercicio 9: Crea una clase Automóvil que use composición para tener un motor, agregando getters y setters para gestionar el motor.

# Ejercicio 10: Crea una clase Profesor que herede de las clases Persona y Empleado, con atributos como nombre, salario, y usa métodos personalizados.


    
class Persona:
    def __init__(self, nombre, tamaño, color_de_ojos,  color_de_pelo) -> None:
        self.nombre = nombre
        self.tamaño = tamaño
        self.color_de_ojos = color_de_ojos
        self.color_de_pelo = color_de_pelo


class Empleado:
    def __init__(self, salario, años_de_trabajo) -> None:
        self.salario = salario
        self.años_de_trabajo = años_de_trabajo


class Profesor(Persona, Empleado):
    def __init__(self, nombre, salario, materia, tamaño, color_de_ojos,  color_de_pelo, años_de_trabajo)-> None:
        super(Profesor,self).__init__( nombre, tamaño, color_de_ojos,  color_de_pelo)
        super(Persona,self).__init__( salario,  años_de_trabajo)
        self.materia = materia
    def  __str__(self) -> str:
        return f'Nombre: {self.nombre}, Salario: {self.salario}, Materia:{self.materia}'

p = Persona("Juan", 123, "verde" , "negro")
profe1 = Profesor('nombre', 1, 'materia', 3, 'color_de_ojos',  'color_de_pelo', 34 )
print(profe1)
