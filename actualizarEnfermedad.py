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

def actualizar_ventana():
    for row in treeview.get_children():
        treeview.delete(row)
    # Cargar las enfermedades desde la base de datos
    enfermedades = cargar_enfermedades()
    # Insertar las enfermedades en el Treeview
    for enfermedad in enfermedades:
        enfermedad_id, nombre_enfermedad, descripcion, pruebas_lab, tratamientos, pruebas_mortem = enfermedad
        sintomas, signos = cargar_sintomas_y_signos(enfermedad_id)
        treeview.insert('', 'end', values=(enfermedad_id, nombre_enfermedad, descripcion, pruebas_lab, tratamientos, pruebas_mortem, ', '.join(sintomas), ', '.join(signos)))


def abrir_ventana_actualizar():
    def actualizar_enfermedad():
        # Obtener los datos de los campos de entrada
        enfermedad_id = id_entry.get()
        nombre = nombre_entry.get()
        descripcion = descripcion_entry.get("1.0", tk.END).strip()
        pruebas = pruebas_entry.get("1.0", tk.END).strip()
        tratamientos = tratamientos_entry.get("1.0", tk.END).strip()
        pruebaPost = pruebaPost_entry.get("1.0", tk.END).strip()
        signos = signo_entry.get("1.0", tk.END).strip().split(', ')
        sintomas = sintomas_entry.get("1.0", tk.END).strip().split(', ')

        if enfermedad_id:
            # Actualizar los datos de la enfermedad en la base de datos
            cursor.execute(
                "UPDATE enfermedades SET nombre = %s, descripcion = %s, pruebas_lab = %s, tratamientos = %s, pruebas_mortem = %s WHERE id = %s",
                (nombre, descripcion, pruebas, tratamientos, pruebaPost, enfermedad_id))

            # Eliminar los signos y síntomas asociados a la enfermedad
            cursor.execute("DELETE FROM enfermedades_signos WHERE enfermedad_id = %s", (enfermedad_id,))
            cursor.execute("DELETE FROM enfermedades_sintomas WHERE enfermedad_id = %s", (enfermedad_id,))

            # Insertar los nuevos signos y síntomas asociados a la enfermedad
            for signo in signos:
                if signo:
                    cursor.execute("INSERT INTO signos (descripcion) VALUES (%s) ON CONFLICT DO NOTHING", (signo,))
                    cursor.execute("SELECT id FROM signos WHERE descripcion = %s", (signo,))
                    signo_id = cursor.fetchone()[0]
                    cursor.execute("INSERT INTO enfermedades_signos (enfermedad_id, signo_id) VALUES (%s, %s)",
                                   (enfermedad_id, signo_id))

            for sintoma in sintomas:
                if sintoma:
                    cursor.execute("INSERT INTO sintomas (descripcion) VALUES (%s) ON CONFLICT DO NOTHING", (sintoma,))
                    cursor.execute("SELECT id FROM sintomas WHERE descripcion = %s", (sintoma,))
                    sintoma_id = cursor.fetchone()[0]
                    cursor.execute("INSERT INTO enfermedades_sintomas (enfermedad_id, sintoma_id) VALUES (%s, %s)",
                                   (enfermedad_id, sintoma_id))

            # Confirmar los cambios en la base de datos
            conn.commit()

            # Mostrar un mensaje de éxito
            tk.messagebox.showinfo("Éxito", "Los datos de la enfermedad han sido actualizados exitosamente")
        else:
            # Si no se proporcionó un ID de enfermedad válido, mostrar un mensaje de advertencia
            tk.messagebox.showwarning("Advertencia", "Por favor ingrese un ID de enfermedad válido")

    def on_select(event):
        if signo_list.curselection():
            selected = [event.widget.get(i) for i in event.widget.curselection()]
            signo_entry.config(state=tk.NORMAL)
            signo_entry.delete('1.0', tk.END)
            signo_entry.insert(tk.END, ', '.join(selected))
            signo_entry.config(state='disabled')

    def on_selectSintomas(event):
        if sintomas_list.curselection():
            selected = [event.widget.get(i) for i in event.widget.curselection()]
            sintomas_entry.config(state=tk.NORMAL)
            sintomas_entry.delete('1.0', tk.END)
            sintomas_entry.insert(tk.END, ', '.join(selected))
            sintomas_entry.config(state='disabled')

    def llenar_con_id():
        enfermedad_id = id_entry.get()

        if enfermedad_id:
            nombre_entry.delete(0, tk.END)
            descripcion_entry.delete('1.0', tk.END)
            pruebas_entry.delete('1.0', tk.END)
            tratamientos_entry.delete('1.0', tk.END)
            pruebaPost_entry.delete('1.0', tk.END)
            signo_entry.delete('1.0', tk.END)
            sintomas_entry.delete('1.0', tk.END)

            # Consultar la base de datos para obtener los datos de la enfermedad con el ID proporcionado
            cursor.execute(
                "SELECT nombre, descripcion, pruebas_lab, tratamientos, pruebas_mortem FROM enfermedades WHERE id = %s",
                (enfermedad_id,))
            enfermedad_data = cursor.fetchone()

            if enfermedad_data:
                # Llenar los campos con los datos obtenidos
                nombre_entry.insert(0, enfermedad_data[0])
                descripcion_entry.insert(tk.END, enfermedad_data[1])
                pruebas_entry.insert(tk.END, enfermedad_data[2])
                tratamientos_entry.insert(tk.END, enfermedad_data[3])
                pruebaPost_entry.insert(tk.END, enfermedad_data[4])

                # Obtener los signos y síntomas asociados a la enfermedad
                cursor.execute(
                    "SELECT s.descripcion FROM signos s JOIN enfermedades_signos es ON s.id = es.signo_id WHERE es.enfermedad_id = %s",
                    (enfermedad_id,))
                signos = [row[0] for row in cursor.fetchall()]
                signo_entry.insert(tk.END, ', '.join(signos))

                cursor.execute(
                    "SELECT s.descripcion FROM sintomas s JOIN enfermedades_sintomas es ON s.id = es.sintoma_id WHERE es.enfermedad_id = %s",
                    (enfermedad_id,))
                sintomas = [row[0] for row in cursor.fetchall()]
                sintomas_entry.insert(tk.END, ', '.join(sintomas))
            else:
                tk.messagebox.showerror("Error", "No se encontró ninguna enfermedad con el ID proporcionado")
        else:
            tk.messagebox.showwarning("Advertencia", "Por favor ingrese un ID válido")

    ventana_actualizar = tk.Toplevel(root)
    ventana_actualizar.title("Actualizar Enfermedad")
    ventana_actualizar.geometry("500x995")

    bienvenida = tk.Label(ventana_actualizar, text="Actualizar Enfermedad", font=(12, '20')).grid(row=0, column=0, columnspan=4, pady=(10, 10))

    info = tk.Label(ventana_actualizar, text="Información", font=(12, '15')).grid(row=1, column=0, sticky="nsew")

    id = tk.Label(ventana_actualizar, text="ID", font=(15)).grid(row=2, column=0, sticky="nsew")
    id_entry = tk.Entry(ventana_actualizar, width=10, font=(15))
    id_entry.grid(row=2, column=1, sticky="W", pady=(10, 10))

    boton_id = tk.Button(ventana_actualizar, text="Llenar con ID", font=(15), command=llenar_con_id,relief="groove").grid(row=3, column=0, columnspan=2, pady=(10, 10))

    nombre = tk.Label(ventana_actualizar, text="Nombre", font=(15)).grid(row=4, column=0, sticky="nsew")
    nombre_entry = tk.Entry(ventana_actualizar, width=30, font=(15))
    nombre_entry.grid(row=4, column=1, sticky="W", pady=(10, 10))

    descripcion = tk.Label(ventana_actualizar, text="Descripción", font=(15)).grid(row=5, column=0, sticky="nsew")
    descripcion_entry = tk.Text(ventana_actualizar, height=5, width=30, font=(15))
    descripcion_entry.grid(row=5, column=1, pady=(10, 10))

    signo = tk.Label(ventana_actualizar, text="Signos", font=(15)).grid(row=6, column=0, sticky="nsew", pady=(10, 10))
    signo_list = tk.Listbox(ventana_actualizar, selectmode=tk.MULTIPLE)
    signo_list.grid(row=7, column=0, sticky="nsew", padx=(10, 10))

    cursor.execute("SELECT descripcion FROM signos")
    rows = cursor.fetchall()
    for row in rows:
        signo_list.insert(tk.END, row[0])

    signo_entry = tk.Text(ventana_actualizar, height=9, width=30, font=(12), state='normal')
    signo_entry.grid(row=7, column=1, pady=(10, 10))

    signo_list.bind('<<ListboxSelect>>', on_select)

    sintomas = tk.Label(ventana_actualizar, text="Sintomas", font=(15)).grid(row=8, column=0, sticky="nsew", pady=(10, 10))
    sintomas_list = tk.Listbox(ventana_actualizar, selectmode=tk.MULTIPLE)
    sintomas_list.grid(row=9, column=0, sticky="nsew", padx=(10, 10))

    cursor.execute("SELECT descripcion FROM sintomas")
    rows = cursor.fetchall()
    for row in rows:
        sintomas_list.insert(tk.END, row[0])

    sintomas_entry = tk.Text(ventana_actualizar, height=9, width=30, font=(12), state='normal')
    sintomas_entry.grid(row=9, column=1, pady=(10, 10))

    sintomas_list.bind('<<ListboxSelect>>', on_selectSintomas)

    pruebas = tk.Label(ventana_actualizar, text="Pruebas de laboratorio", font=(15)).grid(row=10, column=0, sticky="nsew")
    pruebas_entry = tk.Text(ventana_actualizar, height=2, width=30, font=(15))
    pruebas_entry.grid(row=10, column=1, pady=(10, 10))

    tratamientos = tk.Label(ventana_actualizar, text="Tratamientos", font=(15)).grid(row=11, column=0, sticky="nsew")
    tratamientos_entry = tk.Text(ventana_actualizar, height=2, width=30, font=(15))
    tratamientos_entry.grid(row=11, column=1, pady=(10, 10))

    pruebaPost = tk.Label(ventana_actualizar, text="Pruebas Post-mortem", font=(15)).grid(row=12, column=0, sticky="nsew")
    pruebaPost_entry = tk.Text(ventana_actualizar, height=2, width=30, font=(15))
    pruebaPost_entry.grid(row=12, column=1)

    boton_actualizar = tk.Button(ventana_actualizar, text="Actualizar", font=(15), command=actualizar_enfermedad, relief="groove").grid(row=13, column=1, columnspan=2, pady=(20, 10))

root = tk.Tk()
root.title("Actualizar Enfermedades")

frame_arbol = tk.Frame(root)
frame_arbol.grid(row=1, column=0, sticky="w")

bienvenida = tk.Label(root, text="Actualizar Enfermedad",font=(10,'15'))
bienvenida.grid(row=0,column=0)

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
treeview.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

actualizar_button = tk.Button(root, text="Actualizar", command=abrir_ventana_actualizar)
actualizar_button.grid(row=2, column=0, padx=10, pady=10)

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

actualizar_ventana()

root.mainloop()
