from sqlite3 import Row
import tkinter
from tkinter import IntVar, StringVar, ttk

ventana = tkinter.Tk()

seleccionado = tkinter.StringVar()

def mostrar():
    texto.config(text={str(radio.get())})

radio = StringVar()

r1 = ttk.Radiobutton(ventana, text="Opción 1", value="1", variable=radio, command=mostrar)
r2 = ttk.Radiobutton(ventana, text="Opción 2", value="2", variable=radio, command=mostrar)
r3 = ttk.Radiobutton(ventana, text="Opción 3", value="3", variable=radio, command=mostrar)
texto = tkinter.Label(ventana, text="hola")

def limpiar():
    radio.set(None)

boton = tkinter.Button(ventana, text="Reiniciar", command=limpiar)

r1.grid(column=0,row=0)
r2.grid(column=0,row=1)
r3.grid(column=0,row=2)
boton.grid(column=0,row=3)
texto.grid(column=0,row=4)


ventana.mainloop()
