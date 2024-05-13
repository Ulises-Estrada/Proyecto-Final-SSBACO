import tkinter as tk
from tkinter import ttk, messagebox
from conexionDB import create_conn, create_cursor, psycopg2

conn = create_conn()
cursor = create_cursor(conn)
def cargar_signos(combobox):
    try:
        cursor.execute("SELECT descripcion FROM signos ORDER BY descripcion")
        signos = cursor.fetchall()
        combobox["values"] = [s[0] for s in signos]
    except (Exception, psycopg2.Error) as error:
        messagebox.showerror("Error", f"No se pudo conectar a la base de datos: {error}")

def eliminar_signo(combobox):
    signo_seleccionado = combobox.get()
    if not signo_seleccionado:
        messagebox.showerror("Error", "Por favor, seleccione un signo.")
        return
    try:
        cursor = conn.cursor()
        # Eliminar referencias al signo en la tabla enfermedades_sintomas
        cursor.execute("DELETE FROM enfermedades_signos WHERE signo_id = (SELECT id FROM signos WHERE descripcion = %s)", (signo_seleccionado,))
        # Eliminar el signo de la tabla signos
        cursor.execute("DELETE FROM signos WHERE descripcion = %s", (signo_seleccionado,))
        conn.commit()
        messagebox.showinfo("Éxito", f"Se eliminó el signo '{signo_seleccionado}' correctamente.")
        cargar_signos(combobox)  # Actualizar ComboBox después de eliminar
    except (Exception, psycopg2.Error) as error:
        messagebox.showerror("Error", f"No se pudo eliminar el signo: {error}")

ventana = tk.Tk()
ventana.title("Eliminar Signo")

frame = tk.Frame(ventana)
frame.pack()

label = tk.Label(frame, text="Seleccione un signo:")
label.grid(row=0, column=0, padx=5, pady=5)

signos_combobox = ttk.Combobox(frame, width=50, state="readonly")
signos_combobox.grid(row=0, column=1, padx=5, pady=5)

cargar_signos(signos_combobox)

eliminar_button = tk.Button(frame, text="Eliminar Signo", command=lambda: eliminar_signo(signos_combobox))
eliminar_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

ventana.mainloop()

