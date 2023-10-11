import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk

# Fuente para el label
fuente = ("Arial", 15)

# Crear una instancia de la ventana principal
ventana = tk.Tk()

# Obtener el ancho y el largo de la pantalla
ancho = ventana.winfo_screenwidth()
largo = ventana.winfo_screenheight()

# Configurar las propiedades de la ventana
ventana.title("Mikey")
ventana.config(background="GRAY")
# Establece el tamaño de la ventana (ancho x alto)
ventana.geometry(f"{ancho}x{largo}")

# Utilizamos el estilo 'TButton' para crear un botón redondeado
estilo = ttk.Style()
estilo.configure("TButton", borderwidth=0, focuscolor="none")

# Reemplaza "icono.png" con el nombre de tu archivo de imagen
ruta_icono = "icono.png"
imagen_icono = PhotoImage(file=ruta_icono)
ventana.iconphoto(True, imagen_icono)

# Agregar elementos a la ventana
etiqueta = tk.Label(
    ventana, text="Entrenador de Inteligencia artificial", font=fuente)
etiqueta.place(x=500, y=50)
etiqueta.config(background="Gray")

# Crear un botón
boton = ttk.Button(ventana, text="Entrenar", style="TButton", width=20)
boton.place(x=580, y=450)

# Crear un cuadro de texto
txtEntrada1 = tk.Text(ventana, width=40, height=1.5)
txtEntrada1.place(x=250, y=150)
txtEntrada2 = tk.Text(ventana, width=40, height=1.5)
txtEntrada2.place(x=720, y=150)
txtEntrada3 = tk.Text(ventana, width=40, height=1.5)
txtEntrada3.place(x=250, y=250)
txtEntrada4 = tk.Text(ventana, width=40, height=1.5)
txtEntrada4.place(x=720, y=250)
txtEntrada5 = tk.Text(ventana, width=40, height=1.5)
txtEntrada5.place(x=250, y=350)
txtEntrada6 = tk.Text(ventana, width=40, height=1.5)
txtEntrada6.place(x=720, y=350)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
