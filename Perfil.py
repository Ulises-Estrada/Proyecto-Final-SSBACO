from conexionDB import create_conn, create_cursor, close_conn, psycopg2
from PIL import ImageTk, Image
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
    if rolUsuario[0] == 'Administrador' or rolUsuario[0] == 'Administradora':
        # Solo los administradores pueden registrar usuarios
        import registrarUsuarios
    else:
        # Muestra un mensaje de error si el usuario no tiene permiso
        messagebox.showerror("Error", "No tienes permiso para realizar esta acción")

def editar_perfil():
    if rolUsuario[0] == 'Administrador' or rolUsuario[0] == 'Administradora':
        # Solo los administradores pueden editar perfiles de usuario
        import actualizarUsuario
    else:
        # Muestra un mensaje de error si el usuario no tiene permiso
        messagebox.showerror("Error", "No tienes permiso para realizar esta acción")

def eliminar_perfil():
    if rolUsuario[0] == 'Administrador' or rolUsuario[0] == 'Administradora':
        # Solo los administradores pueden eliminar perfiles
        import eliminarUsuario
    else:
        # Muestra un mensaje de error si el usuario no tiene permiso
        messagebox.showerror("Error", "No tienes permiso para realizar esta acción")

def registrar_pacientes():
    if rolUsuario[0] == 'Administrador' or rolUsuario[0] == 'Administradora' or rolUsuario[0] == 'Secretario' or rolUsuario[0] == 'Secretaria':
        # Solo el administrador y la secretaria pueden registrar pacientes
        import pacientesRegistro
    else:
        # Muestra un mensaje de error si el usuario no tiene permiso
        messagebox.showerror("Error", "No tienes permiso para realizar esta acción")

def consultar_pacientes():
    if rolUsuario[0] == 'Administrador' or rolUsuario[0] == 'Administradora' or rolUsuario[0] == 'Secretario' or rolUsuario[0] == 'Secretaria':
        # Solo el administrador y la secretaria pueden consultar pacientes
        import consultarPaciente
    else:
        # Muestra un mensaje de error si el usuario no tiene permiso
        messagebox.showerror("Error", "No tienes permiso para realizar esta acción")

def eliminar_pacientes():
    if rolUsuario[0] == 'Administrador' or rolUsuario[0] == 'Administradora':
         # Solo el administrador puede eliminar pacientes
         import eliminarPaciente
    else:
        # Muestra un mensaje de error si el usuario no tiene permiso
        messagebox.showerror("Error", "No tienes permiso para realizar esta acción")

def actualizar_pacientes():
    if rolUsuario[0] == 'Administrador' or rolUsuario[0] == 'Administradora':
         # Solo el administrador puede eliminar pacientes
         import actualizarPaciente
    else:
        # Muestra un mensaje de error si el usuario no tiene permiso
        messagebox.showerror("Error", "No tienes permiso para realizar esta acción")

def eliminar_enfermedad():
    if rolUsuario[0] == 'Administrador' or rolUsuario[0] == 'Administradora' or rolUsuario[0] == 'Médico':
         # Solo el administrador puede eliminar pacientes
         import eliminarEnfermedad
    else:
        # Muestra un mensaje de error si el usuario no tiene permiso
        messagebox.showerror("Error", "No tienes permiso para realizar esta acción")

def registrar_enfermedad():
    if rolUsuario[0] == 'Administrador' or rolUsuario[0] == 'Administradora' or rolUsuario[0] == 'Médico':
        # Solo el administrador y la secretaria pueden registrar pacientes
        import registrarEnfermedad
    else:
        # Muestra un mensaje de error si el usuario no tiene permiso
        messagebox.showerror("Error", "No tienes permiso para realizar esta acción")

def actualizar_enfermedad():
    if rolUsuario[0] == 'Administrador' or rolUsuario[0] == 'Administradora' or rolUsuario[0] == 'Médico':
         # Solo el administrador puede eliminar pacientes
         import actualizarEnfermedad
    else:
        # Muestra un mensaje de error si el usuario no tiene permiso
        messagebox.showerror("Error", "No tienes permiso para realizar esta acción")

def agregar_signo():
    if rolUsuario[0] == 'Administrador' or rolUsuario[0] == 'Administradora' or rolUsuario[0] == 'Médico':
        # Solo el administrador y la secretaria pueden registrar pacientes
        import registrarSigno
    else:
        # Muestra un mensaje de error si el usuario no tiene permiso
        messagebox.showerror("Error", "No tienes permiso para realizar esta acción")

def agregar_sintoma():
    if rolUsuario[0] == 'Administrador' or rolUsuario[0] == 'Administradora' or rolUsuario[0] == 'Médico':
        # Solo el administrador y la secretaria pueden registrar pacientes
        import registrarSintoma
    else:
        # Muestra un mensaje de error si el usuario no tiene permiso
        messagebox.showerror("Error", "No tienes permiso para realizar esta acción")


def eliminar_signo():
    if rolUsuario[0] == 'Administrador' or rolUsuario[0] == 'Administradora' or rolUsuario[0] == 'Médico':
        # Solo el administrador y la secretaria pueden registrar pacientes
        import eliminarSignos
    else:
        # Muestra un mensaje de error si el usuario no tiene permiso
        messagebox.showerror("Error", "No tienes permiso para realizar esta acción")

def eliminar_sintoma():
    if rolUsuario[0] == 'Administrador' or rolUsuario[0] == 'Administradora' or rolUsuario[0] == 'Médico':
        # Solo el administrador y la secretaria pueden registrar pacientes
        import eliminarSintoma
    else:
        # Muestra un mensaje de error si el usuario no tiene permiso
        messagebox.showerror("Error", "No tienes permiso para realizar esta acción")


root = tk.Tk()
root.title("Inicio")
root.geometry("700x500")


bienvenida = tk.Label(root, text="Bienvenido a nuestra aplicación de diagnósticos médicos",font=(10,'15'))
bienvenida.grid(row=0,column=1)

frame_info = tk.Frame(root)
frame_info.grid(row=1, column=0, sticky="w")

img = Image.open("icono_usuario.png")
img = img.resize((20, 20))
photo = ImageTk.PhotoImage(img)


icon_usuario = tk.Label(frame_info, image=photo)
icon_usuario.image = photo
icon_usuario.grid(row=1, column=0)

usuarios_label = tk.Label(frame_info, text="Usuarios",font=(12,'15'))
usuarios_label.grid(row=1, column=1,sticky="w")

boton_registrar_usuario = tk.Button(frame_info, text=" Registrar ↵ ",command=registrarUsuario,width=10,relief="groove")
boton_registrar_usuario .grid(row=2,column=1)

boton_actualizar_usuario = tk.Button(frame_info, text=" Actualizar ↵ ",command=editar_perfil,width=10,relief="groove")
boton_actualizar_usuario .grid(row=3,column=1)

boton_eliminar_usuario = tk.Button(frame_info, text=" Eliminar ↵ ",command=eliminar_perfil,width=10,relief="groove")
boton_eliminar_usuario .grid(row=4,column=1)

img = Image.open("patient.png")
img = img.resize((20, 20))
photo = ImageTk.PhotoImage(img)


icon_paciente = tk.Label(frame_info, image=photo)
icon_paciente.image = photo
icon_paciente.grid(row=5, column=0)

pacientes_label = tk.Label(frame_info, text="Pacientes",font=(12,'15'))
pacientes_label.grid(row=5, column=1,sticky="w")

boton_registar_paciente = tk.Button(frame_info, text=" Registrar ↵ ", command=registrar_pacientes, width=10,relief="groove")
boton_registar_paciente.grid(row=6,column=1)

boton_actualizar_paciente = tk.Button(frame_info, text=" Actualizar ↵ ", command=actualizar_pacientes, width=10,relief="groove")
boton_actualizar_paciente.grid(row=7,column=1)

boton_eliminar_paciente = tk.Button(frame_info, text=" Eliminar ↵ ", command=eliminar_pacientes, width=10,relief="groove")
boton_eliminar_paciente.grid(row=8,column=1)

img = Image.open("virus.png")
img = img.resize((20, 20))
photo = ImageTk.PhotoImage(img)


icon_paciente = tk.Label(frame_info, image=photo)
icon_paciente.image = photo
icon_paciente.grid(row=9, column=0)

enfermedades_label = tk.Label(frame_info, text="Enfermedades",font=(12,'15'))
enfermedades_label.grid(row=9, column=1,sticky="w")

boton_registrar_enefermedad = tk.Button(frame_info, text=" Registrar Enfermedad ↵ ", command=registrar_enfermedad, width=18,relief="groove")
boton_registrar_enefermedad.grid(row=10,column=1)

boton_actualizar_enefermedad = tk.Button(frame_info, text=" Actualizar Enfermedad ↵ ", command=registrar_enfermedad, width=18,relief="groove")
boton_actualizar_enefermedad.grid(row=11,column=1)

boton_eliminar_enefermedad = tk.Button(frame_info, text=" Eliminar Enfermedad ↵ ", command=registrar_enfermedad, width=18,relief="groove")
boton_eliminar_enefermedad.grid(row=12,column=1)

boton_registrar_signos= tk.Button(frame_info, text=" Registrar Signos ↵ ", command=agregar_signo, width=18,relief="groove")
boton_registrar_signos.grid(row=13,column=1)

boton_eliminar_signos = tk.Button(frame_info, text=" Eliminar Signos ↵ ", command=eliminar_signo, width=18,relief="groove")
boton_eliminar_signos.grid(row=14,column=1)

boton_registrar_sintomas= tk.Button(frame_info, text=" Registrar Sintomas ↵ ", command=agregar_sintoma, width=18,relief="groove")
boton_registrar_sintomas.grid(row=15,column=1)

boton_eliminar_sintomas = tk.Button(frame_info, text=" Eliminar Sintomas ↵ ", command=eliminar_sintoma, width=18,relief="groove")
boton_eliminar_sintomas.grid(row=16,column=1)

image_path = "Logo.jpg"
image = Image.open(image_path)
image = image.resize((320, 320))
photo = ImageTk.PhotoImage(image)

image_label = tk.Label(root, image=photo)
image_label.grid(row=1,column=1)


root.mainloop()