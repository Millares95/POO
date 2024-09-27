"""Enunciado: crear una clase Palindromo que contenga un método de clase esPalindromo(), 
que devuelve un valor booleano que indica si una cadena de caracteres pasada como argumento 
es un palíndromo. Un palíndromo es una cadena que se puede leer de izquierda a derecha o de 
derecha a izquierda. Se tienen en cuenta los caracteres no alfanuméricos."""

# class Palindromo :
#     #* Metodo de clase que verifica si una cadena s 
#     #*es un palindormo
#     def esPalindromo (s):
#         #* Una cadena de un unico caracter o una cadena vacia 
#         #* son Palindromo
#         if len(s) <= 1:
#             return True
#         #* si el primer y utlimo caracter son iguales
#         #*y si la subcadena restante es ella misma 
#         #* un palindormo , entonces todas las cadenas es 
#         #* un palindromo

#         #* el uso del indice -1 permite recuperar
#         #* el ultimo caracter de una cadena
#          #* el uso del caracter ':' permite extraer una 
#          #*subcadena que especifica las indices de inicio y fin 
#         return s[0] == s[-1] and Palindromo.esPalindromo(s[1:-1])

# print(Palindromo.esPalindromo('radar'))
# P = Palindromo
# print(P.esPalindromo('casa'))

# todo Explicacion sobre que es un metodode clase y que es un metodo de instancia 
# class Persona:
#     # Método de clase
#     @classmethod
#     def saludar(cls):
#         print("Hola, soy un método de clase!")

#     # Método de instancia
#     def saludar(self):
#         print(f"Hola, mi nombre es {self.nombre}!")

# juan = Persona("Juan")
# juan.saludar()  # Imprime "Hola, mi nombre es Juan!"
# Persona.saludar()  # Imprime "Hola, soy un método de clase!"
#todo -----------------------------------------------------------------------------------------
"""b. Palíndromo - método de instancia Enunciado: en esta misma clase Palindromo,
añada un atributo que se inicializará en el constructor. Añada también un método test() 
que pruebe si el atributo de la instancia es un palíndromo. Además, al destruir la instancia,
muestre el atributo en mayúsculas."""
# class Palindromo :
        
#     def __init__(self,cadena) -> None:
#         self.cadena = cadena
#     #Metodo de clase que verifica si una cadena s 
#     #es un palindormo
#     def esPalindromo (s):
#         # Una cadena de un unico caracter o una cadena vacia 
#         # son Palindromo
#         if len(s) <= 1:
#             return True
#         # si el primer y utlimo caracter son iguales
#         #y si la subcadena restante es ella misma 
#         # un palindormo , entonces todas las cadenas es 
#         # un palindromo

#         # el uso del indice -1 permite recuperar
#         # el ultimo caracter de una cadena
#          # el uso del caracter ':' permite extraer una 
#          #subcadena que especifica las indices de inicio y fin 
#         return s[0] == s[-1] and Palindromo.esPalindromo(s[1:-1])
    
#     def __del__(self):
#         print(self.cadena.upper())
    
#     def test (self):
#         return Palindromo.esPalindromo(self.cadena)
    
# p = Palindromo('radar')
# print(p.test())

# p= Palindromo('sonar')

# print(p.test())