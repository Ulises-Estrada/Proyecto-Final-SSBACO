from conexionDB import create_conn, create_cursor
from PIL import Image, ImageTk
import tkinter as tk

conn = create_conn()
cursor = create_cursor(conn)

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

def registrar_enfermedad():
    nombre = nombre_entry.get()
    descripcion = descripcion_entry.get("1.0", tk.END).strip()
    pruebas = pruebas_entry.get("1.0", tk.END).strip()
    tratamientos = tratamientos_entry.get("1.0", tk.END).strip()
    pruebaPost = pruebaPost_entry.get("1.0", tk.END).strip()

    cursor.execute("INSERT INTO enfermedades (nombre, descripcion, pruebas_lab, tratamientos, pruebas_mortem) VALUES (%s, %s, %s, %s, %s) RETURNING id", (nombre, descripcion, pruebas, tratamientos, pruebaPost))
    id_enfermedad = cursor.fetchone()[0]

    signos = signo_entry.get("1.0", tk.END).strip().split(', ')
    for signo in signos:
        cursor.execute("SELECT id FROM signos WHERE descripcion = %s", (signo,))
        result = cursor.fetchone()
        if result is not None:
            id_signo = result[0]
            cursor.execute("INSERT INTO enfermedades_signos (enfermedad_id, signo_id) VALUES (%s, %s)", (id_enfermedad, id_signo))

    sintomas = sintomas_entry.get("1.0", tk.END).strip().split(', ')
    for sintoma in sintomas:
        cursor.execute("SELECT id FROM sintomas WHERE descripcion = %s", (sintoma,))
        result = cursor.fetchone()
        if result is not None:
            id_sintoma = result[0]
            cursor.execute("INSERT INTO enfermedades_sintomas (enfermedad_id, sintoma_id) VALUES (%s, %s)", (id_enfermedad, id_sintoma))

    conn.commit()

root = tk.Tk()
root.title("Registro-Enfermedad")
root.geometry("825x950")

bienvenida = tk.Label(root, text="Registro de Enfermedad",font=(12,'20')).grid(row=0, column=0, columnspan=4, pady=(10, 10))

info = tk.Label(root, text="Información",font=(12,'15')).grid(row = 1, column = 0, sticky="nsew")

nombre = tk.Label(root, text="Nombre",font=(15)).grid(row = 3, column = 0,sticky="nsew")
nombre_entry = tk.Entry(root,width=30,font=(15))
nombre_entry.grid(row = 3, column = 1,sticky="W",pady=(10, 10))

descripcion = tk.Label(root, text="Descripción",font=(15)).grid(row = 4, column = 0,sticky="nsew")
descripcion_entry = tk.Text(root,height=6, width=30,font=(15))
descripcion_entry.grid(row = 4, column = 1,pady=(10, 10))

signo = tk.Label(root, text="Signos",font=(15)).grid(row = 5, column = 0,sticky="nsew",pady=(10, 10))
signo_list = (tk.Listbox(root, selectmode=tk.MULTIPLE))
signo_list.grid(row = 6, column = 0,sticky="nsew",padx=(10, 10))

cursor.execute("SELECT descripcion FROM signos")

rows = cursor.fetchall()

for row in rows:
    signo_list.insert(tk.END, row[0])

signo_entry = tk.Text(root,height=9, width=30,font=(15),state='disabled')
signo_entry.grid(row = 6, column = 1,pady=(10, 10))

signo_list.bind('<<ListboxSelect>>', on_select)

sintomas = tk.Label(root, text="Sintomas",font=(15)).grid(row = 7, column = 0,sticky="nsew",pady=(10, 10))
sintomas_list = (tk.Listbox(root, selectmode=tk.MULTIPLE))
sintomas_list.grid(row = 8, column = 0,sticky="nsew",padx=(10, 10))

cursor.execute("SELECT descripcion FROM sintomas")

rows = cursor.fetchall()

for row in rows:
    sintomas_list.insert(tk.END, row[0])

sintomas_entry = tk.Text(root,height=9, width=30,font=(15),state='disabled')
sintomas_entry.grid(row = 8, column = 1,pady=(10, 10))

sintomas_list.bind('<<ListboxSelect>>', on_selectSintomas)

pruebas = tk.Label(root, text="Pruebas de laboratorio",font=(15)).grid(row = 9, column = 0,sticky="nsew")
pruebas_entry = tk.Text(root,height=2, width=30,font=(15))
pruebas_entry.grid(row = 9, column = 1,pady=(10, 10))

tratamientos = tk.Label(root, text="Tratamientos",font=(15)).grid(row = 10, column = 0,sticky="nsew")
tratamientos_entry = tk.Text(root,height=2, width=30,font=(15))
tratamientos_entry.grid(row = 10, column = 1,pady=(10, 10))

pruebaPost = tk.Label(root, text="Pruebas Post-mortem",font=(15)).grid(row = 11, column = 0,sticky="nsew")
pruebaPost_entry = tk.Text(root,height=2, width=30,font=(15))
pruebaPost_entry.grid(row = 11, column = 1)

image_path = "Logo.jpg"
image = Image.open(image_path)
image = image.resize((300, 300))
photo = ImageTk.PhotoImage(image)

image_label = tk.Label(root, image=photo)
image_label.grid(row=2, column=2, rowspan=8, columnspan=2, padx=10, pady=10, sticky="nsew")


boton_registrar = tk.Button(root,text="Registrarse", font=(15),command=registrar_enfermedad).grid(row=10, column=2, columnspan=2, pady=(20, 10))

root.mainloop()