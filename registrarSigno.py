from conexionDB import create_conn, create_cursor
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import re

conn = create_conn()
cursor = create_cursor(conn)

def validate_input(text):
    # Utilizamos una expresión regular para verificar si el texto contiene solo letras
    return bool(re.match("^[A-Za-z]+$", text))

def register():
    nombre = nombre_entry.get().strip()
    if not nombre or not validate_input(nombre):
        messagebox.showerror("Error", "Por favor ingresa un nombre válido.")
        return

    # Verificamos si el signo ya existe en la base de datos
    cursor.execute("SELECT * FROM signos WHERE descripcion = %s", (nombre,))
    signo_existente = cursor.fetchone()

    if signo_existente:
        messagebox.showerror("Error", "Este signo ya ha sido registrado.")
        return

    nombre = nombre_entry.get()

    cursor.execute(
        "INSERT INTO signos (descripcion) VALUES (%s)",
        (nombre,)
    )
    conn.commit()

root = tk.Tk()
root.title("Registro-Signo")
root.geometry("325x280")

bienvenida = tk.Label(root, text="Registro de signo",font=(12,'20')).grid(row=0, column=1, columnspan=3, pady=(20, 10))
info = tk.Label(root, text="Datos",font=(12,'15')).grid(row = 1, column = 0,sticky="E")

nombre = tk.Label(root, text="Nombre",font=(15)).grid(row = 3, column = 0, pady=(10, 0), sticky="nsew")
nombre_entry = tk.Entry(root,width=25,font=(15))
nombre_entry.grid(row = 3, column = 1, pady=(10, 0), sticky="W")


boton_registrar = tk.Button(root,text="Agregar",font=(15),command=register,relief="groove").grid(row=4, column=1, columnspan=2, pady=(20, 10))


root.mainloop()