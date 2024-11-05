import sqlite3
#Clase cuyas instancias se almcenaran en la base de datos
class SuperHeroes:
    def __init__(self, nombre, color, accesorios):
        self.nombre = nombre
        self.color = color
        self.accesorios = accesorios
    
IronMan = SuperHeroes("Tony Stark","rojo","armadura")
capitanAmerica = SuperHeroes("Steve Rogers",  "azul", "escudo")
hulk = SuperHeroes("Bruce Banner","verde", None)
zorro = SuperHeroes("Don Diego de  la Vega", "negro", "espada")

#Objeto que representa la conexion a la base de datos 
conexion = sqlite3.connect('ejemplo.db')

#Uso de la palabra clave "with " que cerrara automaticamente la conexion  al final del bloque 
with conexion:
    #Recuperacion del cursos de la conexion a la base de datos 
    cursor = conexion.cursor()
    # Ejecución de un script SQL para crear una tabla.# Esta se llama SuperHeroes y contiene cuatro columnas:# un identificador entero que debe ser único entre todos
    # los registros de la tabla, y tres campos de texto  que contiene los valores de los atributos de las instancias.# El orden de declaración de los campos es importante.
    cursor.execute("""CREATE TABLE SuperHeroes(ID INT, 
                   Nombre TEXT, 
                   Color TEXT,
                   Accesorio TEXT)""")
    # Lista de las instancias, para hacer un bucle con ellas, para almacenarlas en la base.
    lista_heroes = [IronMan, capitanAmerica, hulk, zorro]
    # El primer identificador comienza por 0 (pero es solo una convención).
    id_heroes = 0
    # Para cada instancia...
    for heroes in lista_heroes:
       # ... ejecutamos un script SQL que insertará uno nuevo registro en la tabla SuperHeroes. Los valores del registro deben estar en el mismo orden que
       # las columnas declaradas durante la creación de la tabla.
       cursor.execute("INSERT INTO SuperHeroes VALUES(?,?,?,?)", (id_heroes, heroes.nombre, heroes.color, heroes.accesorios))
       # No olvide incrementar el contador de identificadores para mantener la unicidad.
       id_heroes += 1
       # Ejecutamos una consulta para recuperar todos los registros (simbolizados por el carácter asterisco) de la tabla SuperHeroes.
       cursor.execute ("SELECT * FROM SuperHeroes")
       # La solicitud se ejecuta y de hecho obtenemos la lista completa en una variable.
       lineas = cursor.fetchall()
       # Se recorre esta lista de registros...
       for linea in lineas:
           # ... y se muestran en la salida estándar.
           print(linea)
          #Se ejecuta una consulta para modificar el campo Accesorio del registro cuyo nombre es Zorro, para darle el valor 'capa'.
    cursor.execute ("UPDATE SuperHeroes SET Accesorio =? WHERE Nombre =?",("capa", zorro.nombre))
    # Las acciones de escritura no se realizan de forma inmediata en la base. De hecho, en caso de error, es aconsejableretroceder en la ejecución,
    #  para volver al estado anterior a la escritura. El método commit() valida las modificaciones, y no es posible ninguna vuelta atrás
    # después de eso.
    conexion.commit ()
    # Habiendo ejecutado el cursor el comando de actualización, podemos preguntarle cuántos registros se han modificado.
    print ("Número de líneas actualizadas: %d" % cursor.rowcount)
    # Cambio de Factory para los registros: en lugar de usar una tupla que contenga los campos, obtendremos un diccionario, por lo que las claves son los nombres de las
    #columnas.
    conexion.row_factory = sqlite3.Row
    # Obtenemos un nuevo cursor, de modo que el cambio de Factory se tiene en cuenta de manera efectiva. Utilizando el cursor antiguo, no podríamos acceder a los
    #  registros como los diccionarios, y la continuación del  programa causaría un error.

    cursor = conexion.cursor ()
    # Recuperamos todos los registros nuevamente de la tabla de SuperHeroes.
    cursor.execute ("SELECT * FROM SuperHeroes")
    lineas = cursor.fetchall ()

    for linea in lineas:
        # Ahora podemos usar los registros como diccionarios.
        print ("%s %s %s" % (linea["Nombre"], linea["Color"], linea["Accesorio"]))
        ## Si el script SQL alguna vez abarca varias líneas, debe usar el método executecript(). Aquí borramos el registro cuyo campo Id es igual a 3,
        #  luego se elimina la propia tabla SuperHeroes.
    cursor.executescript("""
                            DELETE FROM SuperHeroes WHERE Id=3;
                         DROP TABLE IF EXISTS SuperHeroes; """)
    try:
        # Dado que la tabla ha sido destruida, esta consulta debe  lanzar una excepción de SQLite.
        cursor.execute("SELECT * FROM SuperHeroes")
    except sqlite3.Error as e:
        print("Error : %s" % e.args[0])