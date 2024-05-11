from conexionDB import create_conn, create_cursor, psycopg2
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk

conn = create_conn()
cursor = create_cursor(conn)

def tabla():
    cursor.execute("SELECT * FROM usuarios")
    rows = cursor.fetchall()
    return rows

def buscar():
    try:
        id_usuario = id_entry.get()
        cursor.execute("SELECT * FROM usuarios WHERE idusuario = %s", (id_usuario,))
        row = cursor.fetchone()

        if row:
            nombre_entry.delete(0, tk.END)
            nombre_entry.insert(0, row[1])

            apellido_entry.delete(0, tk.END)
            apellido_entry.insert(0, row[2])

            genero_combo.delete(0, tk.END)
            genero_combo.insert(0, row[3])

            telefono_entry.delete(0, tk.END)
            telefono_entry.insert(0, row[4])

            correo_entry.delete(0, tk.END)
            correo_entry.insert(0, row[5])

            contrasena_entry.delete(0, tk.END)
            contrasena_entry.insert(0, row[6])

            rol_combo.delete(0, tk.END)
            rol_combo.insert(0, row[7])
            actualizar_treeview()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error al buscar al usuario:", error)

def actualizar():
    id_usuario = id_entry.get()
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    genero = genero_combo.get()
    telefono = telefono_entry.get()
    correo = correo_entry.get()
    contrasena = contrasena_entry.get()
    rol = rol_combo.get()

    cursor.execute("""
        UPDATE usuarios
        SET nombre = %s, apellidos = %s, genero = %s, telefono = %s, correo = %s, contraseña = %s, rol = %s
        WHERE idusuario = %s
    """, (nombre, apellido, genero, telefono, correo, contrasena, rol, id_usuario))

    conn.commit()
    actualizar_treeview()

def actualizar_treeview():
    for i in tree.get_children():
        tree.delete(i)

    datos_actualizados = tabla()

    for dato in datos_actualizados:
        tree.insert('', 'end', values=dato)


root = tk.Tk()
root.title("Registro")
root.geometry("1300x400")

bienvenida = tk.Label(root, text="Actualizar Usuarios",font=(12,'20')).grid(row=0, column=0, columnspan=4, pady=(20, 10))

frame_entrada = tk.Frame(root)
frame_entrada.grid(row=2, column=0, sticky="nsew",padx=10)

info = tk.Label(root, text="Informacion de Usuario",font=(12,'15')).grid(row = 1, column = 0, sticky="nsew")

id = tk.Label(frame_entrada, text="ID",font=(15)).grid(row = 2, column = 0,sticky="nsew",)
id_entry = tk.Entry(frame_entrada,width=5,font=(15))
id_entry.grid(row = 2, column = 1,sticky="W")


nombre = tk.Label(frame_entrada, text="Nombre",font=(15)).grid(row = 3, column = 0,sticky="nsew")
nombre_entry = tk.Entry(frame_entrada,width=30,font=(15))
nombre_entry.grid(row = 3, column = 1,sticky="W")

apellido = tk.Label(frame_entrada, text="Apellido",font=(15)).grid(row = 4, column = 0,sticky="nsew")
apellido_entry = tk.Entry(frame_entrada,width=30,font=(15))
apellido_entry.grid(row = 4, column = 1)

genero_label = tk.Label(frame_entrada, text="Genero",font=(15))
genero_label.grid(row = 5, column = 0,sticky="nsew")
genero_options = ["Masculino", "Femenino", "No Binario"]
genero_combo = ttk.Combobox(frame_entrada, values=genero_options, width=27, font=(15), state="readonly")
genero_combo.grid(row=5, column=1)

telefono = tk.Label(frame_entrada, text="Teléfono",font=(15)).grid(row = 6, column = 0,sticky="nsew")
telefono_entry = tk.Entry(frame_entrada,width=30,font=(15))
telefono_entry.grid(row = 6, column = 1)

correo = tk.Label(frame_entrada, text="Correo",font=(15)).grid(row = 7, column = 0,sticky="nsew")
correo_entry = tk.Entry(frame_entrada,width=30,font=(15))
correo_entry.grid(row = 7, column = 1)

contra = tk.Label(frame_entrada, text="Contraseña",font=(15)).grid(row = 8, column = 0,sticky="nsew")
contrasena_entry = tk.Entry(frame_entrada, show="*",width=30,font=(15))
contrasena_entry.grid(row = 8, column = 1)

rol_label = tk.Label(frame_entrada, text="Rol",font=(15))
rol_label.grid(row = 9, column = 0,sticky="nsew")
rol_options = ["Administrador", "Médico", "Secretaria"]
rol_combo = ttk.Combobox(frame_entrada, values=rol_options, width=27, font=(15), state="readonly")
rol_combo.grid(row=9, column=1)

boton_buscar = tk.Button(frame_entrada,text="Buscar con ID", command=buscar,font=(15)).grid(row=10, column=0,sticky="nsew",pady=(10, 0))
boton_actualizar = tk.Button(frame_entrada,text="Actualizar", command=actualizar,font=(15)).grid(row=10, column=1,sticky="nsew",pady=(10, 0))


frame_tabla = tk.Frame(root)
frame_tabla.grid(row=2, column=1, sticky="nsew")

data = tabla()
tree = ttk.Treeview(frame_tabla)

tree["columns"]=("idusuarios", "nombre", "apellido", "genero","telefono", "correo", "contraseña", "rol")

# Crea las columnas en el widget
tree.column("#0", width=0, stretch=tk.NO)
tree.column("idusuarios", width=100)
tree.column("nombre", width=100)
tree.column("apellido", width=100)
tree.column("genero", width=100)
tree.column("telefono", width=100)
tree.column("correo", width=100)
tree.column("contraseña", width=100)
tree.column("rol", width=100)

    # Crea los encabezados de las columnas
tree.heading("#0",text="",anchor=tk.W)
tree.heading("idusuarios", text="ID",anchor=tk.W)
tree.heading("nombre", text="Nombre",anchor=tk.W)
tree.heading("apellido", text="Apellido",anchor=tk.W)
tree.heading("genero", text="Genero",anchor=tk.W)
tree.heading("telefono", text="Teléfono",anchor=tk.W)
tree.heading("correo", text="Correo",anchor=tk.W)
tree.heading("contraseña", text="Contraseña",anchor=tk.W)
tree.heading("rol", text="Rol",anchor=tk.W)

# Añade los registros a la tabla
for row in data:
    tree.insert("", tk.END, values=row)

tree.grid(row=1,column=0)

root.mainloop()