from tkinter import Frame, Label, Scale, Tk
from tkinter import LEFT, HORIZONTAL
from tkinter import Label as Etiqueta

class MiVentana(Frame):
    # Cada widget tiene un primer parámetro de constructor
    # que es su widget 'maestro', es decir, el que lo contiene.
    # Si no se especifica este parámetro, y si el widget en cuestión
    # es un frame, entonces este estará contenido automáticamente
    # en la ventana de la aplicación.

    def __init__(self, master=None):
        # Llamamos al constructor de la clase madre de MiVentana, es decir, Frame.
        # Además del widget maestro, especificamos las dimensiones de la ventana:
        # un ancho de 320 píxeles y un alto de 240.
        # super(MiVentana,self).__init__(master)
        super().__init__(master, width=320, height=240)
        
        # La ventana que contiene el frame está referenciada por el atributo master.
        # Entonces es él el que debe usar para modificar el título de la ventana
        # mostrada por el sistema operativo.
        self.master.title("Conversor Cº a Fº ")
        
        # pack() permite consolidar la geometría del frame en la ventana.
        # Sin esta llamada, el dimensionamiento dado en el constructor de Frame
        # no tendría lugar.
        self.pack()
        
        # Bandera para controlar la dependencia entre los controles deslizantes
        self.actualizando = False
        
        # Inicializamos los widgets de la ventana
        self.initWidgets()

    def initWidgets(self):
        # Declaracion de una etiqueta que muestra el texto 'F'. El primer argumento es el widget 'padre' que contendrá esta etiqueta, self, el frame principal.
        self.FTEXTO = Etiqueta(self, text='F')
         
        # Declaración de un cursor que mostrará los grados Fahrenheit. Los parámetros llamados del constructor permiten personalizar el widget: 
        # su orientación es horizontal y los valores que recorre van de -148 a 212.
        self.FCursor = Scale(self, from_=-148, to=212, orient=HORIZONTAL, command=self.convertirFEnC)
        
        # Idem aquí para los Grados Celsius 
        self.CTexto = Label(self, text="C")
        self.CCursor = Scale(self, from_=-273.15, to=100, orient=HORIZONTAL, command=self.convertirCEnF)

        # Creamos una lista de widgets sobre la que hacemos un bucle 
        for widget in [self.CTexto, self.CCursor, self.FTEXTO, self.FCursor]:
            # El widget actual está pegado a la izquierda en la ventana de la aplicación 
            widget.pack(side=LEFT)

    # Método llamado cuando el cursor de grados Celsius se ha movido. Calcula la equivalencia en grados Fahrenheit y modifica el valor del cursor de esta escala de grados en consecuencia.
    def convertirCEnF(self, valor):
        if not self.actualizando:  # Evita bucle de actualización infinita
            self.actualizando = True
            C = float(valor)
            F = C * 9 / 5 + 32
            self.FCursor.set(F)  # Actualiza el valor del deslizador de Fahrenheit
            self.actualizando = False

    # Como convertirCEnF(), pero en el sentido opuesto de conversión de escalas de grados.
    def convertirFEnC(self, valor):
        if not self.actualizando:  # Evita bucle de actualización infinita
            self.actualizando = True
            F = float(valor)
            C = (F - 32) * 5 / 9
            self.CCursor.set(C)  # Actualiza el valor del deslizador de Celsius
            self.actualizando = False

# Instanciación de la ventana 
mi_ventana = MiVentana()
# Lanzamiento del bucle principal 
mi_ventana.mainloop()
