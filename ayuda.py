from tkinter import messagebox

def ayuda_guardar():
    messagebox.showinfo(
        "¿Cómo guardar un libro?",
        "1. Escribe el ISBN del libro.\n"
        "2. Introduce el título.\n"
        "3. Escribe el nombre del autor.\n"
        "4. Selecciona el género.\n"
        "5. Introduce la fecha de publicación.\n"
        "6. Presiona el botón GUARDAR.\n\n"
        "¡Listo! Tu libro quedará registrado XD! ."
    )


def ayuda_buscar():
    messagebox.showinfo(
        "¿Cómo buscar un libro?",
        "1. Escribe el ISBN del libro que deseas encontrar.\n"
        "2. Verifica que esté escrito correctamente.\n"
        "3. Presiona el botón BUSCAR.\n"
        "4. Si el libro está registrado, aparecerán sus datos.\n\n"
        "¡Listo! Podrás consultar tu libro guardado :)."
    )

def ayuda_actualizar():
    messagebox.showinfo(
        "¿Cómo actualizar un libro?",
        "1. Escribe el ISBN del libro que deseas modificar.\n"
        "2. Presiona el botón BUSCAR.\n"
        "3. Aparecerán los datos actuales del libro.\n"
        "4. Modifica la información que deseas cambiar.\n"
        "5. Presiona el botón ACTUALIZAR.\n\n"
        "¡Listo! Los nuevos datos quedarán guardados :)."
    )