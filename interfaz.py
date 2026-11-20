"""Interfaz del Proyecto."""

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from ayuda import ayuda_guardar, ayuda_buscar, ayuda_actualizar


from biblioteca import (
    guardar_libro,
    buscar_libro,
    eliminar_libro,
    imprimir_catalogo,
    actualizar_libro
)

# Crear ventana principal

ventana = tk.Tk()

ventana.title("Biblioteca Digital")
ventana.geometry("450x550")
ventana.resizable(False, False)

# Cargar la imagen de fondo
imagen = Image.open("fondo.jpg")

# Adaptar la imagen al tamaño de la ventana
imagen = imagen.resize((600, 600), Image.Resampling.LANCZOS)

# Convertir la imagen para utilizarla en Tkinter
fondo = ImageTk.PhotoImage(imagen)

# Crear la etiqueta que contendrá la imagen
etiqueta_fondo = tk.Label(
    ventana,
    image=fondo
)

# Colocar la imagen en toda la ventana
etiqueta_fondo.place(
    x=0,
    y=0,
    relwidth=1,
    relheight=1
)

# Título principal

titulo = tk.Label(
    ventana,
    text="Biblioteca Digital  ",
    font=("Times New Roman", 19, "bold"),
    bg="#4375F2",
    fg="white"
)

titulo.grid(
    row=0,
    column=0,
    columnspan=2,
    pady=20
)

# Campo ISBN

tk.Label(
    ventana,
    text="ISBN",
    bg="#4375F2",
    fg="white"
).grid(
    row=1,
    column=0,
    padx=10,
    pady=10
)

entrada_isbn = tk.Entry(
    ventana,
    width=40
)

entrada_isbn.grid(
    row=1,
    column=1,
    padx=10,
    pady=10
)

# Campo título

tk.Label(
    ventana,
    text="Título",
    bg="#4375F2",
    fg="white"
).grid(
    row=2,
    column=0,
    padx=10,
    pady=10
)

entrada_titulo = tk.Entry(
    ventana,
    width=40
)

entrada_titulo.grid(
    row=2,
    column=1,
    padx=10,
    pady=10
)

# Campo autor

tk.Label(
    ventana,
    text="Autor",
    bg="#4375F2",
    fg="white"
).grid(
    row=3,
    column=0,
    padx=10,
    pady=10
)

entrada_autor = tk.Entry(
    ventana,
    width=40
)

entrada_autor.grid(
    row=3,
    column=1,
    padx=10,
    pady=10
)

# Campo género

tk.Label(
    ventana,
    text="Género",
    bg="#4375F2",
    fg="white"
).grid(
    row=4,
    column=0,
    padx=10,
    pady=10
)

entrada_genero = tk.Entry(
    ventana,
    width=40
)

entrada_genero.grid(
    row=4,
    column=1,
    padx=10,
    pady=10
)

# Campo fecha de publicación

tk.Label(
    ventana,
    text="Fecha de publicación",
    bg="#4375F2",
    fg="white"
).grid(
    row=5,
    column=0,
    padx=10,
    pady=10
)

entrada_fecha_publicacion = tk.Entry(
    ventana,
    width=40
)

entrada_fecha_publicacion.grid(
    row=5,
    column=1,
    padx=10,
    pady=10
)


def limpiar():
    """Limpia los campos del formulario."""
    entrada_isbn.delete(0, tk.END)
    entrada_titulo.delete(0, tk.END)
    entrada_autor.delete(0, tk.END)
    entrada_genero.delete(0, tk.END)
    entrada_fecha_publicacion.delete(0, tk.END)


def guardar():
    """Guarda un libro en el catálogo."""
    isbn = entrada_isbn.get()
    titulo = entrada_titulo.get()
    autor = entrada_autor.get()
    genero = entrada_genero.get()
    fecha_publicacion = entrada_fecha_publicacion.get()

    if (
        isbn == ""
        or titulo == ""
        or autor == ""
        or genero == ""
        or fecha_publicacion == ""
    ):

        messagebox.showerror(
            "Error",
            "Complete todos los campos por favor "
        )

        return

    resultado = guardar_libro(
        isbn,
        titulo,
        autor,
        genero,
        fecha_publicacion
    )

    if resultado:

        messagebox.showinfo(
            "Éxito",
            "Libro guardado correctamente :)"
        )

        limpiar()

    else:

        messagebox.showerror(
            "Error",
            "El ISBN ya existe , checa eso"
        )


def buscar():
    """Busca un libro mediante su ISBN."""
    isbn = entrada_isbn.get()

    libro = buscar_libro(isbn)

    if libro:

        entrada_titulo.delete(0, tk.END)
        entrada_autor.delete(0, tk.END)
        entrada_genero.delete(0, tk.END)
        entrada_fecha_publicacion.delete(0, tk.END)

        entrada_titulo.insert(
            0,
            libro["titulo"]
        )

        entrada_autor.insert(
            0,
            libro["autor"]
        )

        entrada_genero.insert(
            0,
            libro["genero"]
        )

        entrada_fecha_publicacion.insert(
            0,
            libro["fecha_publicacion"]
        )

    else:

        messagebox.showerror(
            "Error",
            "Libro no encontrado"
        )


def eliminar():
    """Elimina un libro del catálogo."""
    isbn = entrada_isbn.get()

    resultado = eliminar_libro(isbn)

    if resultado:

        messagebox.showinfo(
            "Eliminado",
            "Libro eliminado correctamente"
        )

        limpiar()

    else:

        messagebox.showerror(
            "Error",
            "Libro no encontrado"
        )


def actualizar():
    """Actualiza la información de un libro."""
    isbn = entrada_isbn.get()
    titulo = entrada_titulo.get()
    autor = entrada_autor.get()
    genero = entrada_genero.get()
    fecha_publicacion = entrada_fecha_publicacion.get()

    resultado = actualizar_libro(
        isbn,
        titulo,
        autor,
        genero,
        fecha_publicacion
    )

    if resultado:
        messagebox.showinfo(
            "Actualizacion",
            "El libro se actualizó correctamente."
        )
        limpiar()

    else:
        messagebox.showerror(
            "Error",
            "No se encontró un libro con ese ISBN."
        )


def imprimir():
    """Genera el catálogo en formato TXT."""
    imprimir_catalogo()

    messagebox.showinfo(
        "Catálogo",
        "Se creó catalogo.txt ,"
        " checar en la carpeta"
    )


# Botones

tk.Button(
    ventana,
    text="ACTUALIZAR",
    command=actualizar,
    width=18,
    bg="#A8C93A",
    fg="white"
).grid(
    row=9,
    column=0,
    padx=5,
    pady=10
)


tk.Button(
    ventana,
    text="¿Cómo actualizar?",
    command=ayuda_actualizar,
    width=18
).grid(
    row=9,
    column=1,
    padx=5,
    pady=10
)


tk.Button(
    ventana,
    text="¿Cómo guardar mis libros?",
    command=ayuda_guardar,
    width=22,
).grid(
    row=8,
    column=0,
    padx=12,
    pady=10
)

tk.Button(
    ventana,
    text="¿Cómo buscar un libro?",
    command=ayuda_buscar,
    width=22,

).grid(
    row=8,
    column=1,
    padx=12,
    pady=10
)
tk.Button(
    ventana,
    text="Guardar",
    width=15,
    command=guardar,
    bg="#A8C93A",
    fg="white",
).grid(
    row=6,
    column=0,
    pady=20
)

tk.Button(
    ventana,
    text="Buscar",
    width=15,
    command=buscar,
    bg="#A8C93A",
    fg="white",
).grid(
    row=6,
    column=1,
    pady=20
)

tk.Button(
    ventana,
    text="Eliminar",
    width=15,
    command=eliminar,
    bg="#A8C93A",
    fg="white",
).grid(
    row=7,
    column=0,
    pady=10
)

tk.Button(
    ventana,
    text="Imprimir",
    width=15,
    command=imprimir,
    bg="#A8C93A",
    fg="white",
).grid(
    row=7,
    column=1,
    pady=10
)

ventana.mainloop()

