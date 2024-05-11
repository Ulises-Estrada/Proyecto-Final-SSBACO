import tkinter as tk
from tkinter import ttk, messagebox
from conexionDB import create_conn, create_cursor, psycopg2

conn = create_conn()
cursor = create_cursor(conn)


def cargar_sintomas(combobox):
    try:
        cursor.execute("SELECT descripcion FROM sintomas ORDER BY descripcion")
        sintomas = cursor.fetchall()
        combobox["values"] = [s[0] for s in sintomas]
    except (Exception, psycopg2.Error) as error:
        messagebox.showerror("Error", f"No se pudo conectar a la base de datos: {error}")

def eliminar_sintoma(combobox):
    sintoma_seleccionado = combobox.get()
    if not sintoma_seleccionado:
        messagebox.showerror("Error", "Por favor, seleccione un síntoma.")
        return
    try:

        # Eliminar referencias al síntoma en la tabla enfermedades_sintomas
        cursor.execute("DELETE FROM enfermedades_sintomas WHERE sintoma_id = (SELECT id FROM sintomas WHERE descripcion = %s)", (sintoma_seleccionado,))
        # Eliminar el síntoma de la tabla sintomas
        cursor.execute("DELETE FROM sintomas WHERE descripcion = %s", (sintoma_seleccionado,))
        conn.commit()
        messagebox.showinfo("Éxito", f"Se eliminó el síntoma '{sintoma_seleccionado}' correctamente.")
        cargar_sintomas(combobox)  # Actualizar ComboBox después de eliminar
    except (Exception, psycopg2.Error) as error:
        messagebox.showerror("Error", f"No se pudo eliminar el síntoma: {error}")

def crear_ventana():
    ventana = tk.Tk()
    ventana.title("Eliminar Síntoma")

    frame = tk.Frame(ventana)
    frame.pack()

    label = tk.Label(frame, text="Seleccione un síntoma:")
    label.grid(row=0, column=0, padx=5, pady=5)

    sintomas_combobox = ttk.Combobox(frame, width=50, state="readonly")
    sintomas_combobox.grid(row=0, column=1, padx=5, pady=5)

    cargar_sintomas(sintomas_combobox)

    eliminar_button = tk.Button(frame, text="Eliminar Síntoma", command=lambda: eliminar_sintoma(sintomas_combobox))
    eliminar_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    ventana.mainloop()

if __name__ == "__main__":
    crear_ventana()
