from conexionDB import create_conn, create_cursor
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re

conn = create_conn()
cursor = create_cursor(conn)

def validar_texto(texto):
    return bool(re.match(r'^[a-zA-Z\s]+$', texto))

def validar_telefono(telefono):
    return telefono.isdigit()

def validar_fecha(fecha):
    return bool(re.match(r'^\d{4}-\d{2}-\d{2}$', fecha))

def register():
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    genero = genero_combobox.get()
    fecha_nac = fecha_entry.get()
    telefono = telefono_entry.get()
    alergias = alergias_text.get("1.0", "end-1c")
    cirugias = cirugias_text.get("1.0", "end-1c")
    medicamentos = medicamentos_text.get("1.0", "end-1c")

    if not validar_texto(nombre):
        messagebox.showerror("Error", "El nombre solo debe contener letras y espacios.")
        return
    if not validar_texto(apellido):
        messagebox.showerror("Error", "El apellido solo debe contener letras y espacios.")
        return
    if not validar_texto(alergias):
        messagebox.showerror("Error", "Las alergias solo deben contener letras y espacios.")
        return
    if not validar_texto(cirugias):
        messagebox.showerror("Error", "Las cirugías solo deben contener letras y espacios.")
        return
    if not validar_texto(medicamentos):
        messagebox.showerror("Error", "Los medicamentos solo deben contener letras y espacios.")
        return
    if not validar_telefono(telefono):
        messagebox.showerror("Error", "El teléfono solo debe contener números.")
        return
    if not validar_fecha(fecha_nac):
        messagebox.showerror("Error", "La fecha debe estar en formato 'aaaa-mm-dd'.")
        return

    cursor.execute(
        "INSERT INTO pacientes (nombre, apellido, fecha_nac, genero,telefono, alergias, cirugias, medicamentos) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        (nombre, apellido, fecha_nac, genero,telefono, alergias, cirugias, medicamentos)
    )
    conn.commit()
    root.destroy()
    import Perfil

root = tk.Tk()
root.title("Registro Paciente")
root.geometry("825x380")

frame_izquierdo = tk.Frame(root)
frame_izquierdo.grid(row=1, column=0, sticky="nsew")

frame_derecho = tk.Frame(root)
frame_derecho.grid(row=1, column=1, sticky="nsew")

bienvenida = tk.Label(root, text="Registro de pacientes",font=(12,'20')).grid(row=0, column=0, columnspan=3, pady=(20, 10))
info = tk.Label(frame_izquierdo, text="Datos",font=(12,'15')).grid(row = 1, column = 0,sticky="E")

nombre = tk.Label(frame_izquierdo, text="Nombre",font=(10)).grid(row = 2, column = 0, pady=(10, 0), sticky="nsew")
nombre_entry = tk.Entry(frame_izquierdo,width=20,font=(15))
nombre_entry.grid(row = 2, column = 1, pady=(10, 0), sticky="W")

apellido = tk.Label(frame_izquierdo, text="Apellidos",font=(15)).grid(row = 3, column = 0, pady=(10, 0), sticky="nsew")
apellido_entry = tk.Entry(frame_izquierdo,width=20,font=(15))
apellido_entry.grid(row = 3, column = 1, pady=(10, 0), sticky="W")

genero = tk.Label(frame_izquierdo, text="Genero",font=(15)).grid(row = 4, column = 0, pady=(10, 0), sticky="nsew")
genero_combobox = ttk.Combobox(frame_izquierdo, width=18, font=(15),state="readonly")
genero_combobox['values'] = ('Masculino', 'Femenino', 'No binario')
genero_combobox.grid(row=4, column=1, pady=(10, 0), sticky="W")

fecha_nac = tk.Label(frame_izquierdo, text="Fecha Nacimiento",font=(15)).grid(row = 5, column = 0, pady=(10, 0), sticky="nsew")
fecha_entry = tk.Entry(frame_izquierdo,width=20,font=(15))
fecha_entry.grid(row = 5, column = 1, pady=(10, 0), sticky="W")

telefono = tk.Label(frame_izquierdo, text="Teléfono",font=(15)).grid(row = 6, column = 0, pady=(10, 0), sticky="nsew")
telefono_entry = tk.Entry(frame_izquierdo,width=20,font=(15))
telefono_entry.grid(row = 6, column = 1, pady=(10, 0), sticky="W")

info_med = tk.Label(frame_derecho, text="Informacion Medica",font=(12,'15')).grid(row = 1, column = 2,sticky="nsew")

alergias_label = tk.Label(frame_derecho, text="Alergias", font=(15))
alergias_label.grid(row=2, column=2, pady=(10, 0), sticky="nsew")
alergias_text = tk.Text(frame_derecho, width=30, height=2, font=(15))
alergias_text.grid(row=2, column=3, pady=(10, 0), sticky="W")

cirugias_label = tk.Label(frame_derecho, text="Cirugias", font=(15))
cirugias_label.grid(row=3, column=2, pady=(10, 0), sticky="nsew")
cirugias_text = tk.Text(frame_derecho, width=30, height=2, font=(15))
cirugias_text.grid(row=3, column=3, pady=(10, 0), sticky="W")

medicamentos_label = tk.Label(frame_derecho, text="Medicamentos", font=(15))
medicamentos_label.grid(row=4, column=2, pady=(10, 0), sticky="nsew")
medicamentos_text = tk.Text(frame_derecho, width=30, height=2, font=(15))
medicamentos_text.grid(row=4, column=3, pady=(10, 0), sticky="W")

boton_registrar = tk.Button(frame_derecho,text="Registrar", command=register,font=(15)).grid(row=10, column=2, columnspan=2, pady=(20, 10))

root.mainloop()