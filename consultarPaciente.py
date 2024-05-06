from conexionDB import create_conn, create_cursor, psycopg2
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

conn = create_conn()
cursor = create_cursor(conn)

def consultar_paciente_por_id():
    # Obtener el ID del paciente ingresado por el usuario
    paciente_id = id_entry.get()

    try:
        # Ejecutar consulta SQL para obtener los datos del paciente por su ID
        cursor.execute("SELECT * FROM pacientes WHERE idpaciente = %s", (paciente_id,))
        
        # Obtener los resultados de la consulta
        paciente = cursor.fetchone()
        
        if paciente:
            # Mostrar los resultados en una nueva ventana
            ventana_consulta = tk.Toplevel(root)
            ventana_consulta.title("Consulta de Paciente")
            
            for j, dato in enumerate(paciente):
                tk.Label(ventana_consulta, text=dato).grid(row=0, column=j)
        else:
            tk.messagebox.showinfo("Consulta de Paciente", "No se encontró ningún paciente con el ID proporcionado.")
        
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error al consultar paciente:", error)

root = tk.Tk()
root.title("Consulta de Paciente")
root.geometry("1300x400")

# Entrada para ingresar el ID del paciente
id_label = tk.Label(root, text="Ingrese ID del paciente:")
id_label.pack(pady=10)
id_entry = tk.Entry(root)
id_entry.pack(pady=5)

# Botón para consultar paciente por ID
boton_consultar = tk.Button(root, text="Consultar Paciente", command=consultar_paciente_por_id)
boton_consultar.pack(pady=10)

root.mainloop()
