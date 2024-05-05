from conexionDB import create_conn, create_cursor
from PIL import Image, ImageTk
import tkinter as tk

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
    import VentanaBienvenida"""

root = tk.Tk()
root.title("Registro-Enfermedad")
root.geometry("825x750")

bienvenida = tk.Label(root, text="Registro de Enfermedad",font=(12,'20')).grid(row=0, column=0, columnspan=4, pady=(10, 10))

info = tk.Label(root, text="Información",font=(12,'15')).grid(row = 1, column = 0, sticky="nsew")

nombre = tk.Label(root, text="Nombre",font=(15)).grid(row = 3, column = 0,sticky="nsew")
nombre_entry = tk.Entry(root,width=30,font=(15))
nombre_entry.grid(row = 3, column = 1,sticky="W",pady=(10, 10))

descripcion = tk.Label(root, text="Descripción",font=(15)).grid(row = 4, column = 0,sticky="nsew")
descripcion_entry = tk.Text(root,height=6, width=30,font=(15))
descripcion_entry.grid(row = 4, column = 1,pady=(10, 10))

signo = tk.Label(root, text="Signos",font=(15)).grid(row = 5, column = 0,sticky="nsew")
signo_entry = tk.Text(root,height=2, width=30,font=(15))
signo_entry.grid(row = 5, column = 1,pady=(10, 10))

sintomas = tk.Label(root, text="Síntomas",font=(15)).grid(row = 6, column = 0,sticky="nsew")
sintomas_entry = tk.Text(root,height=2, width=30,font=(15))
sintomas_entry.grid(row = 6, column = 1,pady=(10, 10))

pruebas = tk.Label(root, text="Pruebas de laboratorio",font=(15)).grid(row = 7, column = 0,sticky="nsew")
pruebas_entry = tk.Text(root,height=2, width=30,font=(15))
pruebas_entry.grid(row = 7, column = 1,pady=(10, 10))

tratamientos = tk.Label(root, text="Tratamientos",font=(15)).grid(row = 8, column = 0,sticky="nsew")
tratamientos_entry = tk.Text(root,height=2, width=30,font=(15))
tratamientos_entry.grid(row = 8, column = 1,pady=(10, 10))

pruebaPost = tk.Label(root, text="Pruebas Post-mortem",font=(15)).grid(row = 9, column = 0,sticky="nsew")
pruebaPost_entry = tk.Text(root,height=2, width=30,font=(15))
pruebaPost_entry.grid(row = 9, column = 1)

image_path = "Logo.jpg"
image = Image.open(image_path)
image = image.resize((300, 300))
photo = ImageTk.PhotoImage(image)

image_label = tk.Label(root, image=photo)
image_label.grid(row=2, column=2, rowspan=8, columnspan=2, padx=10, pady=10, sticky="nsew")


boton_registrar = tk.Button(root,text="Registrarse", font=(15)).grid(row=10, column=2, columnspan=2, pady=(20, 10))

root.mainloop()