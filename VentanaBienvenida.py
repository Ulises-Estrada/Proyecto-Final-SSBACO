from conexionDB import create_conn, create_cursor, close_conn
from PIL import Image, ImageTk
import tkinter as tk

def abrir_ventana_registro():
    root.destroy()
    import registrarUsuarios

def abrir_ventana_login():
    root.destroy()
    import login

conn = create_conn()
cursor = create_cursor(conn)

descripcion = """
Ofrecemos una solución informática que simplifica el diagnóstico médico, reduciendo errores. 
Nuestra plataforma permite a médicos y administradores gestionar usuarios, crear perfiles, 
de pacientes registrar diagnósticos y tratamientos, y actualizar información sobre enfermedades. 
Cada usuario tiene acceso a funciones específicas, garantizando un trabajo eficiente sin  
interferencias. Confíe en nosotros para mejorar la precisión y eficiencia en el diagnóstico médico.
"""

root = tk.Tk()
root.title("Inicio")
root.geometry("700x500")

bienvenida = tk.Label(root, text="Bienvenido a nuestra aplicación de diagnósticos médicos",font=(12,'18'))
bienvenida.pack()

descrip = tk.Label(root, text=descripcion)
descrip.pack()

image_path = "Logo.jpg"
image = Image.open(image_path)
image = image.resize((220, 220))
photo = ImageTk.PhotoImage(image)

image_label = tk.Label(root, image=photo)
image_label.pack()

btn_registrar = tk.Button(root, text="Regístrate",command=abrir_ventana_registro)
btn_registrar.place(relx=0.4, rely=0.8, anchor='center')

btn_isesion = tk.Button(root, text="Iniciar sesión",command=abrir_ventana_login)
btn_isesion.place(relx=0.6, rely=0.8, anchor='center')

root.mainloop()

