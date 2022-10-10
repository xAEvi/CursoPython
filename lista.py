import tkinter

ventana = tkinter.Tk()

lista = ["A", "B", "C", "D"]

texto = tkinter.Label(ventana, text="Abecedario")

lista_items = tkinter.StringVar(value=lista)

lista_box = tkinter.Listbox(ventana, listvariable=lista_items)

texto.pack()
lista_box.pack()

ventana.mainloop()
