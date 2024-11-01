from tkinter import Frame, Tk

class MiVentana(Frame):
    # Constructor de la clase MiVentana, que hereda de Frame
    def __init__(self, master=None):
        # Llamamos al constructor de la clase padre (Frame) y configuramos el tamaño del frame
        super().__init__(master, width=320, height=240)

        # Configuramos el título de la ventana principal
        self.master.title("Mi Aplicación Gráfica")

        # Pack permite que el frame se ajuste en la ventana
        self.pack()

# Código principal
if __name__ == "__main__":
    root = Tk()              # Creamos la ventana raíz
    app = MiVentana(root)     # Creamos una instancia de la clase MiVentana
    app.mainloop()            # Ejecutamos el bucle principal de la aplicación
