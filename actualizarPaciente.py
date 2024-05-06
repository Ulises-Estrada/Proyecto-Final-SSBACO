from conexionDB import create_conn, create_cursor, psycopg2
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk

conn = create_conn()
cursor = create_cursor(conn)

def tabla():
    cursor.execute("SELECT * FROM pacientes")
    rows = cursor.fetchall()
    return rows

def buscar():
    try:
        id_paciente = id_entry.get()
        cursor.execute("SELECT * FROM pacientes WHERE idpaciente = %s", (id_paciente,))
        row = cursor.fetchone()

        if row:
            nombre_entry.delete(0, tk.END)
            nombre_entry.insert(0, row[1])

            apellido_entry.delete(0, tk.END)
            apellido_entry.insert(0, row[2])

            fecha_nac_entry.delete(0, tk.END)
            fecha_nac_entry.insert(0, row[3])

            genero_entry.delete(0, tk.END)
            genero_entry.insert(0, row[4])

            telefono_entry.delete(0, tk.END)
            telefono_entry.insert(0, row[5])

            alergias_entry.delete(0, tk.END)
            alergias_entry.insert(0, row[6])

            cirugias_entry.delete(0, tk.END)
            cirugias_entry.insert(0, row[7])

            medicamentos_entry.delete(0, tk.END)
            medicamentos_entry.insert(0, row[8])

            actualizar_treeview()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error al buscar al usuario:", error)

def actualizar():
    id_paciente = id_entry.get()
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    fecha_nac = fecha_nac_entry.get()
    genero = genero_entry.get()
    telefono = telefono_entry.get()
    alergias = alergias_entry.get()
    cirugias = cirugias_entry.get()
    medicamentos = medicamentos_entry.get()

    cursor.execute("""
        UPDATE pacientes
        SET nombre = %s, apellido = %s, fecha_nac = %s, genero = %s, telefono = %s, alergias = %s, cirugias = %s, medicamentos = %s,
        WHERE idpaciente = %s
    """, (nombre, apellido, fecha_nac, genero, telefono, alergias, cirugias, medicamentos, id_paciente))

    conn.commit()
    actualizar_treeview()

def actualizar_treeview():
    for i in tree.get_children():
        tree.delete(i)

    datos_actualizados = tabla()

    for dato in datos_actualizados:
        tree.insert('', 'end', values=dato)


root = tk.Tk()
root.title("Actualizar paciente")
root.geometry("1300x400")

bienvenida = tk.Label(root, text="Actualizar Pacientes",font=(12,'20')).grid(row=0, column=0, columnspan=4, pady=(20, 10))

frame_entrada = tk.Frame(root)
frame_entrada.grid(row=2, column=0, sticky="nsew",padx=10)

info = tk.Label(root, text="Informacion de Paciente",font=(12,'15')).grid(row = 1, column = 0, sticky="nsew")

id = tk.Label(frame_entrada, text="ID",font=(15)).grid(row = 2, column = 0,sticky="nsew")
id_entry = tk.Entry(frame_entrada,width=30,font=(15))
id_entry.grid(row = 2, column = 1,sticky="W")

nombre = tk.Label(frame_entrada, text="Nombre",font=(15)).grid(row = 3, column = 0,sticky="nsew")
nombre_entry = tk.Entry(frame_entrada,width=30,font=(15))
nombre_entry.grid(row = 3, column = 1,sticky="W")

apellido = tk.Label(frame_entrada, text="Apellido",font=(15)).grid(row = 4, column = 0,sticky="nsew")
apellido_entry = tk.Entry(frame_entrada,width=30,font=(15))
apellido_entry.grid(row = 4, column = 1)

genero = tk.Label(frame_entrada, text="Fecha de nacimiento",font=(15)).grid(row = 5, column = 0,sticky="nsew")
genero_entry = tk.Entry(frame_entrada,width=30,font=(15))
genero_entry.grid(row = 5, column = 1)

telefono = tk.Label(frame_entrada, text="Género",font=(15)).grid(row = 6, column = 0,sticky="nsew")
telefono_entry = tk.Entry(frame_entrada,width=30,font=(15))
telefono_entry.grid(row = 6, column = 1)

correo = tk.Label(frame_entrada, text="Teléfono",font=(15)).grid(row = 7, column = 0,sticky="nsew")
correo_entry = tk.Entry(frame_entrada,width=30,font=(15))
correo_entry.grid(row = 7, column = 1)

contra = tk.Label(frame_entrada, text="Alergias",font=(15)).grid(row = 8, column = 0,sticky="nsew")
contrasena_entry = tk.Entry(frame_entrada, show="*",width=30,font=(15))
contrasena_entry.grid(row = 8, column = 1)

rol = tk.Label(frame_entrada, text="Cirugías",font=(15)).grid(row = 9, column = 0,sticky="nsew")
rol_entry = tk.Entry(frame_entrada,width=30,font=(15))
rol_entry.grid(row = 9, column = 1)

rol = tk.Label(frame_entrada, text="Cirugías",font=(15)).grid(row = 10, column = 0,sticky="nsew")
rol_entry = tk.Entry(frame_entrada,width=30,font=(15))
rol_entry.grid(row = 10, column = 1)

boton_buscar = tk.Button(frame_entrada,text="Buscar con ID", command=buscar,font=(15)).grid(row=10, column=0,sticky="nsew",pady=(10, 0))

boton_actualizar = tk.Button(frame_entrada,text="Actualizar", command=actualizar,font=(15)).grid(row=10, column=1,sticky="nsew",pady=(10, 0))


frame_tabla = tk.Frame(root)
frame_tabla.grid(row=2, column=1, sticky="nsew")

data = tabla()
tree = ttk.Treeview(frame_tabla)

tree["columns"]=("idpaciente", "nombre", "apellido", "fecha_nac","genero", "telefono", "alergias", "cirugias", "medicamentos")

# Crea las columnas en el widget
tree.column("#0", width=0, stretch=tk.NO)
tree.column("idpaciente", width=100)
tree.column("nombre", width=100)
tree.column("apellido", width=100)
tree.column("fecha_nac", width=100)
tree.column("genero", width=100)
tree.column("telefono", width=100)
tree.column("alergias", width=100)
tree.column("cirugias", width=100)
tree.column("medicamentos", width=100)

    # Crea los encabezados de las columnas
tree.heading("#0",text="",anchor=tk.W)
tree.heading("idpaciente", text="ID",anchor=tk.W)
tree.heading("nombre", text="Nombre",anchor=tk.W)
tree.heading("apellido", text="Apellido",anchor=tk.W)
tree.heading("fecha_nac", text="Fecha de nac.",anchor=tk.W)
tree.heading("genero", text="Género",anchor=tk.W)
tree.heading("telefono", text="Telefono",anchor=tk.W)
tree.heading("alergias", text="Alergias",anchor=tk.W)
tree.heading("cirugias", text="Cirugias",anchor=tk.W)
tree.heading("medicamentos", text="Medicamentos",anchor=tk.W)

# Añade los registros a la tabla
for row in data:
    tree.insert("", tk.END, values=row)

tree.grid(row=1,column=0)


root.mainloop()
