import sqlite3
import tkinter as tk
from tkinter import *


def cambios(sentencia):
    conexion = sqlite3.connect('basededatos.sqlite')
    ejec = conexion.cursor()
    ejec.execute(sentencia)
    conexion.commit()
    ejec.close()
    conexion.close()


def busquedas(sentencia):
    conexion = sqlite3.connect('basededatos.sqlite')
    ejec = conexion.cursor()
    ejec.execute(sentencia)
    records = ejec.fetchall()
    ejec.close()
    conexion.close()
    return records


def main():
    for elemento in root.winfo_children():
        elemento.destroy()

    titulo = tk.Label(text="Menu principal")
    titulo.grid(column=0, row=1)

    botoncrear = tk.Button(text="Crear", command=lambda: menucrear())
    botonleer = tk.Button(text="Leer", command=lambda: menuleer())
    botoncambiar = tk.Button(text="Cambiar", command=lambda: menueditar())
    botoneliminar = tk.Button(text="Eliminar", command=lambda: menuborrar())
    botoncrear.grid(column=0, row=2)
    botonleer.grid(column=0, row=3)
    botoncambiar.grid(column=0, row=4)
    botoneliminar.grid(column=0, row=5)


def menucrear():
    for elemento in root.winfo_children():
        elemento.destroy()

    botonatras = tk.Button(text="atras", command=lambda: main())
    botonatras.grid(column=0, row=0)
    titulo = tk.Label(text="Pelicula nueva ingresar datos")
    textoid = tk.Label(text="id")
    textotitulo = tk.Label(text="Titulo")
    textopersonaje = tk.Label(text="Personaje")
    textoestreno = tk.Label(text="Estreno")
    textodirector = tk.Label(text="Director")
    entradaid = tk.Entry()
    entradatitulo = tk.Entry()
    entradapersonaje = tk.Entry()
    entradaestreno = tk.Entry()
    titulo.grid(column=0, row=1)
    textotitulo.grid(column=0, row=4)
    textoid.grid(column=0, row=2)
    textopersonaje.grid(column=0, row=6)
    textoestreno.grid(column=0, row=8)
    textodirector.grid(column=0, row=10)
    entradaid.grid(column=0, row=3)
    entradatitulo.grid(column=0, row=5)
    entradapersonaje.grid(column=0, row=7)
    entradaestreno.grid(column=0, row=9)
    entradadirector = tk.Entry()
    entradadirector.grid(column=0, row=11)

    botoncrear = tk.Button(text="Nueva pelicula", command=lambda: cambios(
        f"""INSERT INTO Peliculas (Id, Titulo, Personaje, Estreno, Director) VALUES ({entradaid.get()}, '{entradatitulo.get()}', '{entradapersonaje.get()}', '{entradaestreno.get()}', '{entradadirector.get()}')"""))
    botoncrear.grid(column=0, row=12)


def menuleer():
    for elemento in root.winfo_children():
        elemento.destroy()

    botonatras = tk.Button(text="atras", command=lambda: main())
    botonatras.grid(column=0, row=0)
    titulo = tk.Label(text="Modos de lectura")
    titulo.grid(column=1, row=1)
    botoncompleto = tk.Button(text="Vista completa",
                              command=lambda: vistacompleta())
    botonanual = tk.Button(text="Peliculas por año", command=lambda: anual())
    botondirector = tk.Button(
        text="Peliculas por director", command=lambda: pordirector())
    botoncompleto.grid(column=0, row=2)
    botondirector.grid(column=1, row=2)
    botonanual.grid(column=2, row=2)

    def vistacompleta():
        root = Tk()
        listbox = Listbox(root, width=70, height=50)

        listbox.pack(side=LEFT, fill=BOTH)
        scrollbar = Scrollbar(root)
        scrollbar.pack(side=RIGHT, fill=BOTH)
        respuesta = busquedas("""SELECT *FROM Peliculas m """)
        for values in respuesta:
            listbox.insert(END, values)

        scrollbar.config(command=listbox.yview)
        root.mainloop()

    def pordirector():
        root = Tk()
        listbox = Listbox(root, width=25, height=20)

        listbox.pack(side=LEFT, fill=BOTH)
        scrollbar = Scrollbar(root)
        scrollbar.pack(side=RIGHT, fill=BOTH)
        respuesta = busquedas(
            """SELECT COUNT(Id) as cantidad, Director FROM Peliculas m GROUP BY Director ORDER BY cantidad desc""")
        for values in respuesta:
            listbox.insert(END, values)

        scrollbar.config(command=listbox.yview)
        root.mainloop()

    def anual():
        root = Tk()
        listbox = Listbox(root, width=15, height=20)

        listbox.pack(side=LEFT, fill=BOTH)
        scrollbar = Scrollbar(root)
        scrollbar.pack(side=RIGHT, fill=BOTH)
        respuesta = busquedas(
            """SELECT COUNT(Id) as cantidad,strftime('%Y', Estreno) as dat FROM Peliculas m GROUP BY dat ORDER BY cantidad desc""")
        for values in respuesta:
            listbox.insert(END, values)

        scrollbar.config(command=listbox.yview)
        root.mainloop()


def menueditar():
    for elemento in root.winfo_children():
        elemento.destroy()

    botonatras = tk.Button(text="atras",
                           command=lambda: main())
    botonatras.grid(column=0, row=0)
    titulo = tk.Label(text="Cambiar datos de una pelicula")
    titulo.grid(column=0, row=1)
    textoid = tk.Label(text="Id")
    textoid.grid(column=0, row=2)
    entradaid = tk.Entry()
    entradaid.grid(column=1, row=2)
    titulo = tk.Label(text="Titulo")
    titulo.grid(column=0, row=3)
    entradatitulo = tk.Entry()
    entradatitulo.grid(column=1, row=3)
    textopersonaje = tk.Label(text="Personaje")
    textopersonaje.grid(column=0, row=4)
    entradapersonaje = tk.Entry()
    entradapersonaje.grid(column=1, row=4)
    textoestreno = tk.Label(text="Estreno")
    textoestreno.grid(column=0, row=5)
    entradaestreno = tk.Entry()
    entradaestreno.grid(column=1, row=5)
    textodirector = tk.Label(text="Director")
    textodirector.grid(column=0, row=6)
    entradadirector = tk.Entry()
    entradadirector.grid(column=1, row=6)

    botoncambiar = tk.Button(text="Cambiar", command=lambda: cambios(
        f"""UPDATE Peliculas SET Titulo = '{entradatitulo.get()}',Personaje = '{entradapersonaje.get()}',Estreno = '{entradaestreno.get()}',Director = '{entradadirector.get()}'WHERE Id = {entradaid.get()}"""))
    botoncambiar.grid(column=0, row=7)


def menuborrar():
    for elemento in root.winfo_children():
        elemento.destroy()

    botonatras = tk.Button(text="atras", command=lambda: main())
    botonatras.grid(column=0, row=0)
    titulo = tk.Label(text="Delete Movie")
    titulo.grid(column=0, row=1)

    textoid = tk.Label(text="Id")
    textoid.grid(column=0, row=2)
    entradaid = tk.Entry()
    entradaid.grid(column=0, row=3)

    botonborrar = tk.Button(text="Borrar", command=lambda: cambios(
        f"""DELETE FROM Peliculas WHERE Id = {entradaid.get()}"""))
    botonborrar.grid(column=0, row=4)


if __name__ == '__main__':
    root = tk.Tk(className='Programa')
    main()
    root.mainloop()
