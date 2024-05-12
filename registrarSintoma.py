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
    nombre = nombre_entry.get().strip().lower()  # Convertimos el texto ingresado a minúsculas

    # Verificamos si el campo de nombre está vacío o no contiene solo letras
    if not nombre or not validate_input(nombre):
        messagebox.showerror("Error", "Por favor ingresa un nombre válido.")
        return

    # Verificamos si el síntoma ya existe en la base de datos (ignorando diferencias en capitalización)
    cursor.execute("SELECT * FROM sintomas WHERE LOWER(descripcion) = %s", (nombre,))
    sintoma_existente = cursor.fetchone()

    if sintoma_existente:
        messagebox.showerror("Error", "Este síntoma ya ha sido registrado.")
        return

    # Insertamos el nuevo síntoma en la base de datos
    cursor.execute("INSERT INTO sintomas (descripcion) VALUES (%s)", (nombre,))
    conn.commit()
    messagebox.showinfo("Éxito", "Síntoma registrado correctamente.")

root = tk.Tk()
root.title("Registro Paciente")
root.geometry("325x280")

bienvenida = tk.Label(root, text="Registro de síntoma",font=(12,'20')).grid(row=0, column=1, columnspan=3, pady=(20, 10))
info = tk.Label(root, text="Datos",font=(12,'15')).grid(row = 1, column = 0,sticky="E")

nombre_label = tk.Label(root, text="Nombre",font=(10)).grid(row = 3, column = 0, pady=(10, 0), sticky="nsew")
nombre_entry = tk.Entry(root,width=25,font=(15))
nombre_entry.grid(row = 3, column = 1, pady=(10, 0), sticky="W")

boton_registrar = tk.Button(root,text="Agregar",font=(15),command=register,relief="groove").grid(row=4, column=1, columnspan=2, pady=(20, 10))

root.mainloop()
