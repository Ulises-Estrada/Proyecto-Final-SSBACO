from conexionDB import create_conn, create_cursor
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox

conn = create_conn()
cursor = create_cursor(conn)

"""def register():
    id = id_entry.get()
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    genero = genero_entry.get()
    telefono = telefono_entry.get()
    correo = correo_entry.get()
    contrasena = contrasena_entry.get()
    rol = rol_entry.get()

    cursor.execute(
        "INSERT INTO usuarios (idusuarios,nombre, apellido, genero, telefono, correo, contraseña, rol) VALUES (%s, %s, %s, %s, %s, %s, %s,%s)",
        (id,nombre, apellido, genero, telefono, correo, contrasena, rol)
    )
    conn.commit()
    root.destroy()
    import Perfil"""

root = tk.Tk()
root.title("Registro Paciente")
root.geometry("825x480")


bienvenida = tk.Label(root, text="Registro de pacientes",font=(12,'20')).grid(row=0, column=1, columnspan=2, pady=(20, 10))
info = tk.Label(root, text="Datos",font=(12,'15')).grid(row = 1, column = 0, sticky="nsew")

id = tk.Label(root, text="ID",font=(15)).grid(row = 2, column = 0,sticky="nsew")
id_entry = tk.Entry(root,width=30,font=(15))
id_entry.grid(row = 2, column = 1,sticky="W")

nombre = tk.Label(root, text="Nombre",font=(15)).grid(row = 3, column = 0,sticky="nsew")
nombre_entry = tk.Entry(root,width=30,font=(15))
nombre_entry.grid(row = 3, column = 1,sticky="W")

apellido = tk.Label(root, text="Apellido",font=(15)).grid(row = 4, column = 0,sticky="nsew")
apellido_entry = tk.Entry(root,width=30,font=(15))
apellido_entry.grid(row = 3, column = 1)



#boton_registrar = tk.Button(root,text="Registrarse", command=register,font=(15)).grid(row=10, column=2, columnspan=2, pady=(20, 10))


root.mainloop()