from conexionDB import create_conn, create_cursor, close_conn
from PIL import Image, ImageTk
import tkinter as tk

"""conn = create_conn()
cursor = create_cursor(conn)

def cerrar_sesion():
   close_conn(conn)
   root.destroy()

"""
def editar_perfil():
    root.destroy()
    import actualizarUsuario

def eliminar_perfil():
    root.destroy()
    import eliminarUsuario

root = tk.Tk()
root.title("Inicio")
root.geometry("600x500")

bienvenida = tk.Label(root, text="Bienvenido a nuestra aplicación de diagnósticos médicos",font=(12,'15'))
bienvenida.grid(row=0,column=1)

frame_icon = tk.Frame(root)
frame_icon.grid(row=1, column=0, sticky="w")

image_path = "Logo.jpg"
image = Image.open(image_path)
image = image.resize((220, 220))
photo = ImageTk.PhotoImage(image)

image_label = tk.Label(root, image=photo)
image_label.grid(row=2,column=1)

icon_user_image  = Image.open("icono_usuario.png")
icon_user_image = icon_user_image .resize((30, 30))
icon_user = ImageTk.PhotoImage(image=icon_user_image)

icon_user_label = tk.Label(frame_icon,image=icon_user).grid(row=1,column=0)

info_frame = tk.Frame(root)
info_frame.grid(row=1, column=1, sticky="w")

usuarios = tk.Label(info_frame, text="Usuarios",font=(12,'15'))
usuarios.grid(row=1,column=1,pady=(20, 0))

actualizar = tk.Label(info_frame, text="Actualizar",font=12)
actualizar.grid(row=2,column=1)

eliminar = tk.Label(info_frame, text="Eliminar",font=12)
eliminar.grid(row=3,column=1)

regisrar = tk.Label(info_frame, text="Registrar",font=12)
regisrar.grid(row=4,column=1)


"""# Crear botón para cerrar sesión
boton_cerrar_sesion = tk.Button(root, text="Editar perfil", )
boton_cerrar_sesion.grid()

# Crear botón para cerrar sesión
boton_cerrar_sesion = tk.Button(root, text="Cerrar sesión",)
boton_cerrar_sesion.grid()
"""

boton_actualizar = tk.Button(info_frame, text=" ↵ ",command=editar_perfil)
boton_actualizar.grid(row=2,column=2)

boton_cerrar_sesion = tk.Button(info_frame, text=" ↵ ",command=eliminar_perfil)
boton_cerrar_sesion.grid(row=3,column=2)

root.mainloop()