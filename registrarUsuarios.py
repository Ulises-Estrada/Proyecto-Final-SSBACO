from conexionDB import create_conn, create_cursor
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox

conn = create_conn()
cursor = create_cursor(conn)

def validaciones():
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    telefono = telefono_entry.get()

    # Validación de nombre y apellido: no deben contener números
    if any(char.isdigit() for char in nombre) or any(char.isdigit() for char in apellido):
        messagebox.showerror("Error", "El nombre y el apellido no deben contener números.")
        return False

    # Validación de teléfono: solo deben ser números
    if not telefono.isdigit():
        messagebox.showerror("Error", "El teléfono debe contener solo números.")
        return False

    return True  # Devolver True si todas las validaciones son exitosas

def register():
    if not validaciones():
        return
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    genero = genero_combo.get()
    telefono = telefono_entry.get()
    correo = correo_entry.get()
    contrasena = contrasena_entry.get()
    rol = rol_combo.get()


    cursor.execute(
        "INSERT INTO usuarios (nombre, apellidos, genero, telefono, correo, contraseña, rol) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (nombre, apellido, genero, telefono, correo, contrasena, rol)
    )
    conn.commit()
    root.destroy()
    import VentanaBienvenida

root = tk.Tk()
root.title("Registro")
root.geometry("825x480")

bienvenida = tk.Label(root, text="Registro de usuarios",font=(12,'20')).grid(row=0, column=0, columnspan=4, pady=(20, 10))

info = tk.Label(root, text="Informacion Personal",font=(12,'15')).grid(row = 1, column = 0, sticky="nsew")

nombre = tk.Label(root, text="Nombre",font=(15)).grid(row = 2, column = 0,sticky="nsew")
nombre_entry = tk.Entry(root,width=30,font=(15))
nombre_entry.grid(row = 2, column = 1,sticky="W")

apellido = tk.Label(root, text="Apellido(s)",font=(15)).grid(row = 3, column = 0,sticky="nsew")
apellido_entry = tk.Entry(root,width=30,font=(15))
apellido_entry.grid(row = 3, column = 1)

genero_label = tk.Label(root, text="Genero", font=(15))
genero_label.grid(row=4, column=0, sticky="nsew")
genero_options = ["Masculino", "Femenino", "No Binario"]
genero_combo = ttk.Combobox(root, values=genero_options, width=27, font=(15),state="readonly")
genero_combo.grid(row=4, column=1)

telefono = tk.Label(root, text="Teléfono",font=(15)).grid(row = 5, column = 0,sticky="nsew")
telefono_entry = tk.Entry(root,width=30,font=(15))
telefono_entry.grid(row = 5, column = 1)

correo = tk.Label(root, text="Correo",font=(15)).grid(row = 6, column = 0,sticky="nsew")
correo_entry = tk.Entry(root,width=30,font=(15))
correo_entry.grid(row = 6, column = 1)

contra = tk.Label(root, text="Contraseña",font=(15)).grid(row = 7, column = 0,sticky="nsew")
contrasena_entry = tk.Entry(root, show="*",width=30,font=(15))
contrasena_entry.grid(row = 7, column = 1)

rol = tk.Label(root, text="Rol",font=(15)).grid(row = 8, column = 0,sticky="nsew")
rol_options = ["Administrador", "Médico", "Secretaria"]
rol_combo = ttk.Combobox(root, values=rol_options, width=27, font=(15), state="readonly")
rol_combo.grid(row=8, column=1)


image_path = "Logo.jpg"
image = Image.open(image_path)
image = image.resize((300, 300))
photo = ImageTk.PhotoImage(image)

image_label = tk.Label(root, image=photo)
image_label.grid(row=2, column=2, rowspan=8, columnspan=2, padx=10, pady=10, sticky="nsew")

boton_registrar = tk.Button(root,text="Registrarse", command=register,font=(15)).grid(row=10, column=2, columnspan=2, pady=(20, 10))

root.mainloop()