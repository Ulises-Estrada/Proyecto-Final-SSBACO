from conexionDB import create_conn, create_cursor
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox

conn = create_conn()
cursor = create_cursor(conn)

def register():
    id_paciente = id_entry.get()
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    genero = genero_entry.get()
    fecha_nac = fecha_entry.get()
    telefono = telefono_entry.get()
    alergias = alergias_entry.get()
    cirugias = cirugias_entry.get()
    medicamentos = medicamentos_entry.get()
    cursor.execute(
        "INSERT INTO pacientes (idpaciente, nombre, apellido, fecha_nac, genero,telefono, alergias, cirugias, medicamentos) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (id_paciente, nombre, apellido, fecha_nac, genero,telefono, alergias, cirugias, medicamentos)
    )
    conn.commit()
    root.destroy()
    import Perfil

root = tk.Tk()
root.title("Registro Paciente")
root.geometry("825x480")

bienvenida = tk.Label(root, text="Registro de pacientes",font=(12,'20')).grid(row=0, column=1, columnspan=3, pady=(20, 10))
info = tk.Label(root, text="Datos",font=(12,'15')).grid(row = 1, column = 0,sticky="E")

id = tk.Label(root, text="ID",font=(15)).grid(row = 2, column = 0, pady=(10, 0), sticky="nsew")
id_entry = tk.Entry(root,width=15,font=(15))
id_entry.grid(row = 2, column = 1, pady=(10, 0), sticky="W")

nombre = tk.Label(root, text="Nombre",font=(10)).grid(row = 3, column = 0, pady=(10, 0), sticky="nsew")
nombre_entry = tk.Entry(root,width=15,font=(15))
nombre_entry.grid(row = 3, column = 1, pady=(10, 0), sticky="W")

apellido = tk.Label(root, text="Apellido",font=(15)).grid(row = 4, column = 0, pady=(10, 0), sticky="nsew")
apellido_entry = tk.Entry(root,width=15,font=(15))
apellido_entry.grid(row = 4, column = 1, pady=(10, 0), sticky="W")

genero = tk.Label(root, text="Genero",font=(15)).grid(row = 5, column = 0, pady=(10, 0), sticky="nsew")
genero_entry = tk.Entry(root,width=15,font=(2))
genero_entry.grid(row = 5, column = 1, pady=(10, 0), sticky="W")

fecha_nac = tk.Label(root, text="Fecha Nacimiento",font=(15)).grid(row = 6, column = 0, pady=(10, 0), sticky="nsew")
fecha_entry = tk.Entry(root,width=15,font=(15))
fecha_entry.grid(row = 6, column = 1, pady=(10, 0), sticky="W")

telefono = tk.Label(root, text="Teléfono",font=(15)).grid(row = 7, column = 0, pady=(10, 0), sticky="nsew")
telefono_entry = tk.Entry(root,width=15,font=(15))
telefono_entry.grid(row = 7, column = 1, pady=(10, 0), sticky="W")

info_med = tk.Label(root, text="Informacion Medica",font=(12,'15')).grid(row = 1, column = 2,sticky="nsew")

alergias = tk.Label(root, text="Alergias",font=(15)).grid(row = 2, column = 2, pady=(10, 0), sticky="nsew")
alergias_entry = tk.Entry(root,width=30,font=(15))
alergias_entry.grid(row = 2, column = 3, pady=(10, 0), sticky="W")

cirugias = tk.Label(root, text="Cirugias",font=(15)).grid(row = 3, column = 2, pady=(10, 0), sticky="nsew")
cirugias_entry = tk.Entry(root,width=30,font=(15))
cirugias_entry.grid(row = 3, column = 3, pady=(10, 0), sticky="W")

medicamentos = tk.Label(root, text="Medicamentos",font=(15)).grid(row = 4, column = 2, pady=(10, 0), sticky="nsew")
medicamentos_entry = tk.Entry(root,width=30,font=(15))
medicamentos_entry.grid(row = 4, column = 3, pady=(10, 0), sticky="W")

boton_registrar = tk.Button(root,text="Registrar", command=register,font=(15)).grid(row=10, column=2, columnspan=2, pady=(20, 10))

root.mainloop()