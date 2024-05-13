import tkinter as tk
from tkinter import ttk
from conexionDB import create_conn, create_cursor
from tkinter import messagebox

conn = create_conn()
cursor = create_cursor(conn)

def volver():
    import Perfil
    root.destroy()

def cargar_enfermedades():
    cursor.execute("SELECT id, nombre, descripcion, pruebas_lab, tratamientos, pruebas_mortem FROM enfermedades")
    return cursor.fetchall()

def cargar_sintomas_y_signos(enfermedad_id):
    cursor.execute("SELECT s.descripcion FROM sintomas s JOIN enfermedades_sintomas es ON s.id = es.sintoma_id WHERE es.enfermedad_id = %s", (enfermedad_id,))
    sintomas = cursor.fetchall()
    cursor.execute("SELECT s.descripcion FROM signos s JOIN enfermedades_signos es ON s.id = es.signo_id WHERE es.enfermedad_id = %s", (enfermedad_id,))
    signos = cursor.fetchall()
    return [s[0] for s in sintomas], [s[0] for s in signos]

def eliminar_enfermedad():
    # Obtener el ID de la enfermedad ingresado por el usuario
    enfermedad_id = id_entry.get()

    # Verificar si se ingresó un ID válido
    if enfermedad_id.strip() == "":
        messagebox.showerror("Error", "Por favor ingresa un ID de enfermedad válido.")
        return

    try:
        enfermedad_id = int(enfermedad_id)
    except ValueError:
        messagebox.showerror("Error", "El ID de la enfermedad debe ser un número entero.")
        return

    try:
        # Eliminar las filas de la tabla enfermedades_sintomas relacionadas con la enfermedad a eliminar
        cursor.execute("DELETE FROM enfermedades_sintomas WHERE enfermedad_id = %s", (enfermedad_id,))
        # Eliminar las filas de la tabla enfermedades_signos relacionadas con la enfermedad a eliminar
        cursor.execute("DELETE FROM enfermedades_signos WHERE enfermedad_id = %s", (enfermedad_id,))
        # Eliminar la enfermedad de la tabla enfermedades
        cursor.execute("DELETE FROM enfermedades WHERE id = %s", (enfermedad_id,))
        # Confirmar los cambios en la base de datos
        conn.commit()
        # Mostrar un mensaje de éxito
        messagebox.showinfo("Éxito", "Enfermedad eliminada exitosamente de la base de datos.")
    except Exception as e:
        # Mostrar un mensaje de error si no se pudo eliminar la enfermedad
        messagebox.showerror("Error", f"No se pudo eliminar la enfermedad: {str(e)}")

    # Actualizar la ventana después de eliminar la enfermedad
    actualizar_ventana()


def actualizar_ventana():
    # Limpiar el Treeview antes de volver a cargar los datos
    for row in treeview.get_children():
        treeview.delete(row)
    # Cargar las enfermedades desde la base de datos
    enfermedades = cargar_enfermedades()
    # Insertar las enfermedades en el Treeview
    for enfermedad in enfermedades:
        enfermedad_id, nombre_enfermedad, descripcion, pruebas_lab, tratamientos, pruebas_mortem = enfermedad
        sintomas, signos = cargar_sintomas_y_signos(enfermedad_id)
        treeview.insert('', 'end', values=(enfermedad_id, nombre_enfermedad, descripcion, pruebas_lab, tratamientos, pruebas_mortem, ', '.join(sintomas), ', '.join(signos)))

# Crear la ventana principal
root = tk.Tk()
root.title("Eliminar Enfermedades")

bienvenida = tk.Label(root, text="Elimninar Enfermedad",font=(10,'15'))
bienvenida.grid(row=0,column=0)

frame_id = tk.Frame(root)
frame_id.grid(row=1, column=0, sticky="w")

id = tk.Label(frame_id, text="ID", font=(10,'15')).grid(row=1, column=0, sticky="nsew")
id_entry = tk.Entry(frame_id, width=10, font=(15))
id_entry.grid(row=1, column=1, sticky="W", pady=(10, 10))

boton_id = tk.Button(frame_id, text="Eliminar", font=(15),relief="groove",command=eliminar_enfermedad).grid(row=1, column=2, pady=(10, 10),padx=(10, 10))

frame_arbol = tk.Frame(root)
frame_arbol.grid(row=2, column=0, sticky="w")

# Crear un Treeview para mostrar las enfermedades
treeview = ttk.Treeview(frame_arbol, columns=('ID', 'Nombre', 'Descripción', 'Pruebas Lab', 'Tratamientos', 'Pruebas Mortem', 'Síntomas', 'Signos'), show='headings')
treeview.heading('ID', text='ID')
treeview.heading('Nombre', text='Nombre')
treeview.heading('Descripción', text='Descripción')
treeview.heading('Pruebas Lab', text='Pruebas Lab')
treeview.heading('Tratamientos', text='Tratamientos')
treeview.heading('Pruebas Mortem', text='Pruebas Mortem')
treeview.heading('Síntomas', text='Síntomas')
treeview.heading('Signos', text='Signos')
treeview.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

volver_button = tk.Button(root, text="Regresar", command=volver)
volver_button.grid(row=3, column=0, padx=10, pady=10)

# Ajustar el tamaño de las columnas en el Treeview
treeview.column('ID', width=50)
treeview.column('Nombre', width=100)
treeview.column('Descripción', width=150)
treeview.column('Pruebas Lab', width=150)
treeview.column('Tratamientos', width=150)
treeview.column('Pruebas Mortem', width=150)
treeview.column('Síntomas', width=200)
treeview.column('Signos', width=200)

# Cargar las enfermedades al iniciar la ventana
actualizar_ventana()

root.mainloop()
