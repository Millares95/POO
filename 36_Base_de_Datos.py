class SuperHeroes:
    def __init__(self, nombre, color, accesorios):
        self.nombre = nombre
        self.color = color
        self.accesorios = accesorios
    
SuperHeroes("Tony Stark","rojo","armadura")
SuperHeroes("Steve Rogers",  "azul", "escudo")
SuperHeroes("Bruce Banner","verde", None)

import sqlite3 
import sys

# Declaramos la variable aquí para evitar un error de 'conexion # is not defined' en el bloque 'finally'
conexion = None
try:
    #Recuperacion de un objt que repersenta la conexion de datos rerpsneradas por el archivo ejemplo.db
    #Si el archivo no existe se crea 
    conexion = sqlite3.connect('ejemplo.db')
# el cursor en un objeto utilizado para recirrer el conjunto (en el sentido matemtico ) de los resultados obtenidos 
    cursor = conexion.cursor()
#Desde este cursor se ejecutan las consultas SQL. Aqui ,SQLITE_VERSION() es una funcion porpuesta por SQLITE par recuperar el numero de version de la base  de datos
    cursor.execute('SELECT SQLITE_VERSION()')
    #Obtenemos el primer ( y unico) registro del conjunto devuelto por la consulta 
    datos = cursor.fetchone()

# Se muestra esta grabacion en la salida estandar 
    print("SQLITE esta en version {}".format(datos))
except  sqlite3.Error as e:
    #Si SQLite alguna vez arroja uana excepcion, la detectamos aqui y la mostramos 
    print("Error{}:".format(e.arg[0]))
    #Es una buena practica devolver el ejecutable un codigo diferente de cero en cada error.
    sys.exit(1)

finally:
    #Como es necesario limpiar una vez finalizado el tratmiento,excepcion o no, cerramos la conexion a la base de datos 
    if conexion:
        conexion.close()