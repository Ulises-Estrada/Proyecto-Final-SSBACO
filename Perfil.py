from conexionDB import create_conn, create_cursor, close_conn, psycopg2
from PIL import Image, ImageTk
from login import getRolUsuario
import tkinter as tk
from tkinter import messagebox

conn = create_conn()
cursor = create_cursor(conn)
rolUsuario = getRolUsuario()

def cerrar_sesion():
   close_conn(conn)
   root.destroy()
   import VentanaBienvenida

def registrarUsuario():
    if rolUsuario[0] == 'Administrador':
        # Solo los administradores pueden registrar usuarios
        import registrarUsuarios
    else:
        # Muestra un mensaje de error si el usuario no tiene permiso
        messagebox.showerror("Error", "No tienes permiso para realizar esta acción")

def editar_perfil():
    if rolUsuario[0] == 'Administrador':
        # Solo los administradores pueden editar perfiles de usuario
        import actualizarUsuario
    else:
        # Muestra un mensaje de error si el usuario no tiene permiso
        messagebox.showerror("Error", "No tienes permiso para realizar esta acción")

def eliminar_perfil():
    if rolUsuario[0] == 'Administrador':
        # Solo los administradores pueden eliminar perfiles
        import eliminarUsuario
    else:
        # Muestra un mensaje de error si el usuario no tiene permiso
        messagebox.showerror("Error", "No tienes permiso para realizar esta acción")

def registrar_pacientes():
    if rolUsuario[0] == 'Administrador' or rolUsuario[0] == 'Secretaria':
        # Solo el administrador y la secretaria pueden registrar pacientes
        import pacientesRegistro
    else:
        # Muestra un mensaje de error si el usuario no tiene permiso
        messagebox.showerror("Error", "No tienes permiso para realizar esta acción")

def consultar_pacientes():
    if rolUsuario[0] == 'Administrador'or rolUsuario[0] == 'Secretaria':
        # Solo el administrador y la secretaria pueden consultar pacientes
        import consultarPaciente
    else:
        # Muestra un mensaje de error si el usuario no tiene permiso
        messagebox.showerror("Error", "No tienes permiso para realizar esta acción")

def eliminar_pacientes():
    if rolUsuario[0] == 'Administrador':
         # Solo el administrador puede eliminar pacientes
         import eliminarPaciente
    else:
        # Muestra un mensaje de error si el usuario no tiene permiso
        messagebox.showerror("Error", "No tienes permiso para realizar esta acción")

def actualizar_pacientes():
    if rolUsuario[0] == 'Administrador':
         # Solo el administrador puede actualizar pacientes
         import actualizarPaciente
    else:
        # Muestra un mensaje de error si el usuario no tiene permiso
        messagebox.showerror("Error", "No tienes permiso para realizar esta acción")

def registrar_enfermedad():
    if rolUsuario[0] == 'Administrador' or rolUsuario[0] == 'Medico':
        # Solo el administrador y el medico pueden registrar enfermedades
        import registrarEnfermedad
    else:
        # Muestra un mensaje de error si el usuario no tiene permiso
        messagebox.showerror("Error", "No tienes permiso para realizar esta acción")

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

# Crear botón para cerrar sesión
boton_cerrar_sesion = tk.Button(root, text="Cerrar sesión", command=cerrar_sesion)
boton_cerrar_sesion.grid()

# Usuarios
boton_registrar = tk.Button(info_frame, text=" Registrar ↵ ",command=registrarUsuario,width=10,relief="groove")
boton_registrar.grid(row=2,column=1)

boton_actualizar = tk.Button(info_frame, text=" Actualizar ↵ ",command=editar_perfil,width=10,relief="groove")
boton_actualizar.grid(row=3,column=1)

boton_eliminar = tk.Button(info_frame, text=" Eliminar ↵ ",command=eliminar_perfil,width=10,relief="groove")
boton_eliminar.grid(row=4,column=1)

# Pacientes
boton_registar_paciente = tk.Button(info_frame, text=" Registrar ↵ ", command=registrar_pacientes, width=10,relief="groove")
boton_registar_paciente.grid(row=6,column=1)

boton_actualizar_paciente = tk.Button(info_frame, text=" Actualizar ↵ ", command=actualizar_pacientes, width=10,relief="groove")
boton_actualizar_paciente.grid(row=7,column=1)

boton_consultar_paciente = tk.Button(info_frame, text=" Consultar ↵ ", command=consultar_pacientes, width=10,relief="groove")
boton_consultar_paciente.grid(row=8,column=1)

boton_eliminar_paciente = tk.Button(info_frame, text=" Eliminar ↵ ", command=eliminar_pacientes, width=10,relief="groove")
boton_eliminar_paciente.grid(row=9,column=1)

# Enfermedad
boton_registrar_enefermedad = tk.Button(info_frame, text=" Registrar ↵ ", command=registrar_enfermedad, width=10,relief="groove")
boton_registrar_enefermedad.grid(row=10,column=1)

boton_actualizar_enefermedad = tk.Button(info_frame, text=" Actualizar ↵ ", command=actualizar_enfermedad, width=10,relief="groove")
boton_actualizar_enefermedad.grid(row=11,column=1)

boton_eliminar_enefermedad = tk.Button(info_frame, text=" Eliminar ↵ ", command=eliminar_enfermedad, width=10,relief="groove")
boton_eliminar_enefermedad.grid(row=12,column=1)

root.mainloop()