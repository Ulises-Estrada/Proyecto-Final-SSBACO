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

def registrarUsuario():
    root.destroy()
    import registrarUsuarios

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
image_label.grid(row=1,column=1)

icon_user_image  = Image.open("icono_usuario.png")
icon_user_image = icon_user_image .resize((30, 30))
icon_user = ImageTk.PhotoImage(image=icon_user_image)

icon_user_label = tk.Label(frame_icon,image=icon_user).grid(row=1,column=0)

icon_patient_image = Image.open("patient.png")
icon_patient_image = icon_patient_image .resize((30, 30))
icon_patient = ImageTk.PhotoImage(image=icon_patient_image)

icon_patient_label = tk.Label(frame_icon,image=icon_patient).grid(row=5,column=0)

icon_virus_image = Image.open("virus.png")
icon_virus_image = icon_virus_image .resize((30, 30))
icon_virus = ImageTk.PhotoImage(image=icon_virus_image)

icon_virus_label = tk.Label(frame_icon,image=icon_virus).grid(row=6,column=0)

info_frame = tk.Frame(root)
info_frame.grid(row=1, column=1, sticky="w")

usuarios = tk.Label(info_frame, text="Usuarios",font=(12,'15'))
usuarios.grid(row=1,column=1,pady=(20, 0))

pacientes = tk.Label(info_frame, text="Pacientes",font=(12,'15'))
pacientes.grid(row=5,column=1,pady=(20, 0))

enfermedades = tk.Label(info_frame, text="Enfermedades",font=(12,'15'))
enfermedades.grid(row=9,column=1,pady=(20, 0))

"""
# Crear botón para cerrar sesión
boton_cerrar_sesion = tk.Button(root, text="Cerrar sesión",)
boton_cerrar_sesion.grid()
"""

boton_registrar = tk.Button(info_frame, text=" Registrar ↵ ",command=editar_perfil,width=10,relief="groove")
boton_registrar.grid(row=2,column=1)

boton_actualizar = tk.Button(info_frame, text=" Actualizar ↵ ",command=registrarUsuario,width=10,relief="groove")
boton_actualizar.grid(row=3,column=1)

boton_eliminar = tk.Button(info_frame, text=" Eliminar ↵ ",command=eliminar_perfil,width=10,relief="groove")
boton_eliminar.grid(row=4,column=1)

boton_registar_paciente = tk.Button(info_frame, text=" Registrar ↵ ",width=10,relief="groove")
boton_registar_paciente.grid(row=6,column=1)

boton_actualizar_paciente = tk.Button(info_frame, text=" Actualizar ↵ ",width=10,relief="groove")
boton_actualizar_paciente.grid(row=7,column=1)

boton_eliminar_paciente = tk.Button(info_frame, text=" Eliminar ↵ ",width=10,relief="groove")
boton_eliminar_paciente.grid(row=8,column=1)

boton_eliminar_enefermedad = tk.Button(info_frame, text=" Registrar ↵ ",width=10,relief="groove")
boton_eliminar_enefermedad.grid(row=10,column=1)

boton_actualizar_enefermedad = tk.Button(info_frame, text=" Actualizar ↵ ",width=10,relief="groove")
boton_actualizar_enefermedad.grid(row=11,column=1)

boton_eliminar_enefermedad = tk.Button(info_frame, text=" Eliminar ↵ ",width=10,relief="groove")
boton_eliminar_enefermedad.grid(row=12,column=1)

root.mainloop()