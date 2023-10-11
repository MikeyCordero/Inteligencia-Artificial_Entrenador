import tkinter  as tk
from tkinter import PhotoImage

fuente = ("Arial", 15)

# Crear una instancia de la ventana principal
ventana = tk.Tk()

# Configurar las propiedades de la ventana
ventana.title("Mikey")
ventana.geometry("400x300")  # Establece el tamaño de la ventana (ancho x alto)

# Reemplaza "icono.png" con el nombre de tu archivo de imagen
ruta_icono = "icono.png"
imagen_icono = PhotoImage(file=ruta_icono)
ventana.iconphoto(True, imagen_icono)

# Agregar elementos a la ventana
etiqueta = tk.Label(ventana, text="Entrenador de Inteligencia artificial",font=fuente)
etiqueta.pack()  # Coloca la etiqueta en la ventana

# Iniciar el bucle principal de la aplicación
ventana.mainloop()