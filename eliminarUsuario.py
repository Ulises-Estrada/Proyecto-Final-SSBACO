from conexionDB import create_conn, create_cursor, psycopg2
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk


def eliminar_usuario():
    id_usuario = id_entry.get()
    try:
        conn = create_conn()
        cursor = create_cursor(conn)

        # Ejecutar la consulta SQL para eliminar el usuario
        cursor.execute("DELETE FROM usuarios WHERE idusuarios = %s", (id_usuario))

        # Confirmar la eliminacion de usuario
        conn.commit()

        root.destroy()
        import Perfil

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error al eliminar al usuario:", error)

def tabla():
    conn = create_conn()
    cursor = create_cursor(conn)
    cursor.execute("SELECT * FROM usuarios")
    rows = cursor.fetchall()
    conn.close()
    return rows

root = tk.Tk()
root.title("Registro")
root.geometry("1000x300")

data = tabla()
tree = ttk.Treeview(root)

tree["columns"]=("idusuarios", "nombre", "apellido", "fecha_nac", "genero","telefono", "correo", "contraseña", "rol")

# Crea las columnas en el widget
tree.column("#0", width=0, stretch=tk.NO)
tree.column("idusuarios", width=100)
tree.column("nombre", width=100)
tree.column("apellido", width=100)
tree.column("fecha_nac", width=100)
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
tree.heading("fecha_nac", text="Fecha de Nacimiento",anchor=tk.W)
tree.heading("genero", text="Genero",anchor=tk.W)
tree.heading("telefono", text="Teléfono",anchor=tk.W)
tree.heading("correo", text="Correo",anchor=tk.W)
tree.heading("contraseña", text="Contraseña",anchor=tk.W)
tree.heading("rol", text="Rol",anchor=tk.W)

# Añade los registros a la tabla
for row in data:
    tree.insert("", tk.END, values=row)


bienvenida = tk.Label(root, text="Eliminación de Usuarios",font=(12,'20')).grid(row=0, column=1, sticky="NSEW",columnspan=2,)

tree.grid(row=1,column=1,columnspan=2)



id = tk.Label(root, text="ID").grid(row=2, column=0, )
id_entry = tk.Entry(root)
id_entry.grid(row=2, column=1)

boton_eliminar = tk.Button(root, text="Eliminar", command=eliminar_usuario).grid(row=2, column=2)

root.mainloop()