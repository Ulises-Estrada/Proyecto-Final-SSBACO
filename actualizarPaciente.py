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

            fecha_entry.delete(0, tk.END)
            fecha_entry.insert(0, row[3])

            genero_combobox.delete(0, tk.END)
            genero_combobox.insert(0, row[4])

            telefono_entry.delete(0, tk.END)
            telefono_entry.insert(0, row[5])

            alergias_text.delete(0, tk.END)
            alergias_text.insert(0, row[6])

            alergias_text.delete(0, tk.END)
            alergias_text.insert(0, row[7])

            medicamentos_text.delete(0, tk.END)
            medicamentos_text.insert(0, row[8])

            actualizar_treeview()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error al buscar al usuario:", error)

def actualizar():
    id_paciente = id_entry.get()
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    fecha_nac = fecha_entry.get()
    genero = genero_combobox.get()
    telefono = telefono_entry.get()
    alergias = alergias_text.get()
    cirugias = alergias_text.get()
    medicamentos = alergias_text.get()

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
root.geometry("1800x400")

bienvenida = tk.Label(root, text="Actualizar Pacientes",font=(12,'20')).grid(row=0, column=0, columnspan=4, pady=(20, 10))

frame_izquierdo = tk.Frame(root)
frame_izquierdo.grid(row=1, column=0, sticky="nsew")

frame_derecho = tk.Frame(root)
frame_derecho.grid(row=1, column=1, sticky="nsew")

info = tk.Label(frame_izquierdo, text="Datos",font=(12,'15')).grid(row = 1, column = 0,sticky="E")

id = tk.Label(frame_izquierdo, text="ID",font=(15)).grid(row = 2, column = 0,sticky="nsew",)
id_entry = tk.Entry(frame_izquierdo,width=5,font=(15))
id_entry.grid(row = 2, column = 1,sticky="W")

nombre = tk.Label(frame_izquierdo, text="Nombre",font=(10)).grid(row = 3, column = 0, pady=(10, 0), sticky="nsew")
nombre_entry = tk.Entry(frame_izquierdo,width=20,font=(15))
nombre_entry.grid(row = 3, column = 1, pady=(10, 0), sticky="W")

apellido = tk.Label(frame_izquierdo, text="Apellidos",font=(15)).grid(row =4, column = 0, pady=(10, 0), sticky="nsew")
apellido_entry = tk.Entry(frame_izquierdo,width=20,font=(15))
apellido_entry.grid(row = 4, column = 1, pady=(10, 0), sticky="W")

genero = tk.Label(frame_izquierdo, text="Genero",font=(15)).grid(row = 5, column = 0, pady=(10, 0), sticky="nsew")
genero_combobox = ttk.Combobox(frame_izquierdo, width=18, font=(15),state="readonly")
genero_combobox['values'] = ('Masculino', 'Femenino', 'No binario')
genero_combobox.grid(row=5, column=1, pady=(10, 0), sticky="W")

fecha_nac = tk.Label(frame_izquierdo, text="Fecha Nacimiento",font=(15)).grid(row = 6, column = 0, pady=(10, 0), sticky="nsew")
fecha_entry = tk.Entry(frame_izquierdo,width=20,font=(15))
fecha_entry.grid(row = 6, column = 1, pady=(10, 0), sticky="W")

telefono = tk.Label(frame_izquierdo, text="Teléfono",font=(15)).grid(row = 7, column = 0, pady=(10, 0), sticky="nsew")
telefono_entry = tk.Entry(frame_izquierdo,width=20,font=(15))
telefono_entry.grid(row = 7, column = 1, pady=(10, 0), sticky="W")

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

boton_buscar = tk.Button(frame_derecho,text="Buscar con ID", command=buscar,font=(11),relief="groove").grid(row=5, column=2,sticky="nsew",pady=(10, 0))
boton_actualizar = tk.Button(frame_derecho,text="Actualizar", command=actualizar,font=(11),relief="groove").grid(row=5, column=3,sticky="nsew",pady=(10, 0))

frame_tabla = tk.Frame(root)
frame_tabla.grid(row=1, column=3, sticky="nsew",padx=(20, 10))

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

tree.grid()
frame_tabla.rowconfigure(0, weight=1)
frame_tabla.columnconfigure(0, weight=1)



root.mainloop()
