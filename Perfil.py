from conexionDB import create_conn, create_cursor, close_conn
from PIL import Image, ImageTk
import tkinter as tk

conn = create_conn()
cursor = create_cursor(conn)

def cerrar_sesion():
   close_conn(conn)
   root.destroy()

def editar_perfil():
    root.destroy()
    import actualizarUsuario

def eliminar_perfil():
    root.destroy()
    import eliminarUsuario

root = tk.Tk()
root.title("Inicio")
root.geometry("600x500")

bienvenida = tk.Label(root, text="Bienvenido a nuestra aplicación de diagnósticos médicos")
bienvenida.pack()

image_path = "Logo.jpg"
image = Image.open(image_path)
image = image.resize((220, 220))
photo = ImageTk.PhotoImage(image)

image_label = tk.Label(root, image=photo)
image_label.pack()

# Crear botón para cerrar sesión
boton_cerrar_sesion = tk.Button(root, text="Editar perfil", command=editar_perfil)
boton_cerrar_sesion.place(relx=0.2, rely=0.8, anchor='center')

# Crear botón para cerrar sesión
boton_cerrar_sesion = tk.Button(root, text="Cerrar sesión",)
boton_cerrar_sesion.place(relx=0.4, rely=0.8, anchor='center')

# Crear botón para cerrar sesión
boton_cerrar_sesion = tk.Button(root, text="Eliminar cuenta", command=eliminar_perfil)
boton_cerrar_sesion.place(relx=0.6, rely=0.8, anchor='center')

root.mainloop()