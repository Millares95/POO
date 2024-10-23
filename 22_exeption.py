'''Enunciado: escriba un programa que simule la conexión de un usuario a un sitio web para el que ya se ha registrado,
solo con su dirección de correo electrónico (la gestión de una contraseña está fuera del alcance de esta sección)
. Este programa debe ofrecer la posibilidad al usuario de introducir una dirección de correo electrónico, y mostrará 
diferentes mensajes de error en función de la cadena introducida. El programa debe continuar si el correo electrónico 
indicado tiene un formato incorrecto y finalizar si no se reconoce el correo electrónico, ya que se podría tratar de 
un ciberataque. Importante: el método que analiza la cadena de caracteres no debe devolver ningún valor.'''
import re  

class EntradaIncorrecta(Exception): pass
class EmailMalFomrateado(BaseException): pass 
class CiberAtaque(BaseException): pass 

def validacion_email(cadena):
    if cadena is None or cadena == "":
        raise EntradaIncorrecta 
    if re.search(". * @. * \ .. *", cadena) is None:
        raise EmailMalFomrateado
    if cadena != "vicente@eni.es":
        raise CiberAtaque

while True:
    try:
        cadena = input('-->')
        validacion_email(cadena)
# * Si llegamos a esta linea significa que no se produjo la excepción por lo tanto , el correo es correcto y el bucle se puede interrumpir 
        break
    except EntradaIncorrecta:
        print (f'{cadena}es una entrada incorrecta.Indique una direccion de correo electronico ')
    except EmailMalFomrateado:
        print("Una direccion de correo electrónico debe tener el formato xxx@xxx.xx")
    except CiberAtaque:
        print("Ciberataque detectado. El programa se cerrará")
        exit(1)
    print("Bienvenido Vivente")