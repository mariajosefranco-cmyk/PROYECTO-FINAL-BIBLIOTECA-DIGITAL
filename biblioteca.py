"""Biblioteca del Proyecto."""

import json



def cargar_datos():
    """Lee los datos guardados en JSON."""
    archivo = open(
        "libros.json",
        "r",
    )

    datos = json.load(archivo)

    archivo.close()

    return datos


def guardar_datos(datos):
    """Guarda los datos en JSON."""
    archivo = open(
        "libros.json",
        "w",
    )

    json.dump(
        datos,
        archivo,
        indent=4,
    )

    archivo.close()


def guardar_libro(
    isbn,
    titulo,
    autor,
    genero,
    fecha_publicacion
):
    """Agrega un libro nuevo."""
    datos = cargar_datos()

    if isbn in datos:

        return False

    datos[isbn] = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "fecha_publicacion": fecha_publicacion
    }

    guardar_datos(datos)

    return True


def buscar_libro(isbn):
    """Busca un libro por ISBN."""
    datos = cargar_datos()

    if isbn in datos:

        return datos[isbn]

    return None


def eliminar_libro(isbn):
    """Elimina un libro por ISBN."""
    datos = cargar_datos()

    if isbn in datos:

        del datos[isbn]

        guardar_datos(datos)

        return True

    return False

def actualizar_libro(
    isbn,
    titulo,
    autor,
    genero,
    fecha_publicacion
):
    """Actualiza la información de un libro."""

    datos = cargar_datos()

    if isbn not in datos:
        return False

    datos[isbn] = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "fecha_publicacion": fecha_publicacion
    }

    guardar_datos(datos)

    return True

def imprimir_catalogo():
    """Crea el archivo catalogo.txt."""
    datos = cargar_datos()

    archivo = open(
        "catalogo.txt",
        "w",
    )

    for isbn in datos:

        archivo.write("----------------------\n")

        archivo.write(
            "ISBN: "
            + isbn
            + "\n"
        )

        archivo.write(
            "Título: "
            + datos[isbn]["titulo"]
            + "\n"
        )

        archivo.write(
            "Autor: "
            + datos[isbn]["autor"]
            + "\n"
        )

        archivo.write(
            "Género: "
            + datos[isbn]["genero"]
            + "\n"
        )

        archivo.write(
            "Fecha de publicación: "
            + datos[isbn]["fecha_publicacion"]
            + "\n"
        )

        archivo.write("----------------------\n\n")

    archivo.close()
