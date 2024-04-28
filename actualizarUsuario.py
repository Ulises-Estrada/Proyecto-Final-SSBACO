from ConexionDB import create_conn, create_cursor, psycopg2
from PIL import Image, ImageTk
import tkinter as tk

def actualizar_usuario():
  id = id_entry.get()
  nuevo_nombre = nombre_entry.get()
  nuevo_apellido = apellido_entry.get()
  nuevo_telefono = telefono_entry.get()
  nuevo_correo = correo_entry.get()
  nueva_contrasena = contrasena_entry.get()
  try:  
    conn = create_conn()
    cursor = create_cursor(conn)

    # Ejecutar la consulta SQL para actualizar la información del usuario
    cursor.execute("UPDATE usuarios SET nombre = %s, apellido = %s, telefono = %s, correo = %s, contraseña = %s WHERE idusuarios = %s",(nuevo_nombre, nuevo_apellido, nuevo_telefono, nuevo_correo, nueva_contrasena, id))
    
    # Confirmar la actualización de usuario
    conn.commit()
    root.destroy()
    import Perfil

  except (Exception, psycopg2.DatabaseError) as error: print("Error al actualizar la información del usuario:", error) 

root = tk.Tk()
root.title("Actualización")
root.geometry("300x300")

bienvenida = tk.Label(root, text="Actualización de perfil").grid(row = 0, column = 0, sticky="NSEW")

info = tk.Label(root, text="Informacion Personal").grid(row = 1, column = 0, sticky="W")

id = tk.Label(root, text="ID").grid(row = 2, column = 0, )
id_entry = tk.Entry(root)
id_entry.grid(row = 2, column = 1)

nombre = tk.Label(root, text="Nombre").grid(row = 3, column = 0, )
nombre_entry = tk.Entry(root)
nombre_entry.grid(row = 3, column = 1)

apellido = tk.Label(root, text="Apellido").grid(row = 4, column = 0)
apellido_entry = tk.Entry(root)
apellido_entry.grid(row = 4, column = 1)

telefono = tk.Label(root, text="Teléfono").grid(row = 5, column = 0)
telefono_entry = tk.Entry(root)
telefono_entry.grid(row = 5, column = 1)

correo = tk.Label(root, text="Correo").grid(row = 6, column = 0)
correo_entry = tk.Entry(root)
correo_entry.grid(row = 6, column = 1)

contra = tk.Label(root, text="Contraseña").grid(row = 7, column = 0)
contrasena_entry = tk.Entry(root, show="*")
contrasena_entry.grid(row = 7, column = 1)

boton_actualizar = tk.Button(root,text="Guardar cambios").grid(row= 9, column = 0)

root.mainloop()

