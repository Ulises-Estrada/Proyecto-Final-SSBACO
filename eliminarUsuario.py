from ConexionDB import create_conn, create_cursor, psycopg2
from PIL import Image, ImageTk
import tkinter as tk


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

root = tk.Tk()
root.title("Registro")
root.geometry("300x300")

bienvenida = tk.Label(root, text="Eliminación de perfil").grid(row=0, column=0, sticky="NSEW")

id = tk.Label(root, text="ID").grid(row=1, column=0, )
id_entry = tk.Entry(root)
id_entry.grid(row=1, column=1)

boton_eliminar = tk.Button(root, text="Eliminar", ).grid(row=2, column=0)

root.mainloop()