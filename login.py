from conexionDB import create_conn, create_cursor
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox

conn = create_conn()
cursor = create_cursor(conn)

resultado = None

def registrarse():
    root.destroy()
    import registrarUsuarios

def getRolUsuario():
    return resultado

# Función para iniciar sesión
def iniciar_sesion():
    correo = correo_entry.get()
    contrasena = contrasena_entry.get()

    global resultado

    # Verificar las credenciales en la base de datos
    cursor.execute("SELECT rol FROM usuarios WHERE correo = %s AND contraseña = %s", (correo, contrasena))
    
    resultado = cursor.fetchone()

    if resultado is not None:
        # Si se encuentra el usuario, cerrar la ventana de login y abrir la ventana de home
        root.destroy()
        import Perfil
    else:
        # Si no se encuentra el usuario, mostrar un mensaje de error
        messagebox.showerror("Inicio de sesión", "Correo electrónico o contraseña incorrectos")

# Configuración de la ventana de la GUI
root = tk.Tk()
root.title("Inicio de sesión")
root.geometry("500x450")

# Crear elementos de la interfaz gráfica
bienvenida = tk.Label(root, text="Inicio Sesión",font=(12,'20')).grid(row=0, column=1, columnspan=4, pady=(20, 10))

correo_label = tk.Label(root, text="Correo electrónico:",font=(15))
correo_label.grid(row=1, column=0,pady=10)
correo_entry = tk.Entry(root,width=30,font=(15))
correo_entry.grid(row=1, column=1)

contrasena_label = tk.Label(root, text="Contraseña:",font=(15))
contrasena_label.grid(row=2, column=0)
contrasena_entry = tk.Entry(root, show="*",width=30,font=(15))
contrasena_entry.grid(row=2, column=1,sticky="W")

iniciar_sesion_button = tk.Button(root, text="Iniciar sesión", command=iniciar_sesion,relief="groove")
iniciar_sesion_button.grid(row=3, column=1,pady=10,padx=(10,10))

registrarse_button = tk.Button(root, text="Registrarse", command=registrarse,relief="groove")
registrarse_button.grid(row=3, column=0,pady=10,)

image_path = "Logo.jpg"
image = Image.open(image_path)
image = image.resize((220, 220))
photo = ImageTk.PhotoImage(image)

image_label = tk.Label(root, image=photo)
image_label.grid(row=4, column=1, rowspan=7, columnspan=2, padx=10, pady=10, sticky="nsew")

root.mainloop()
