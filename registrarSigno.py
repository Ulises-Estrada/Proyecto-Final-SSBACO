from conexionDB import create_conn, create_cursor
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox

conn = create_conn()
cursor = create_cursor(conn)

root = tk.Tk()
root.title("Registro-Signo")
root.geometry("825x480")

bienvenida = tk.Label(root, text="Registro de signo",font=(12,'20')).grid(row=0, column=1, columnspan=3, pady=(20, 10))
info = tk.Label(root, text="Datos",font=(12,'15')).grid(row = 1, column = 0,sticky="E")

nombre = tk.Label(root, text="Nombre",font=(10)).grid(row = 3, column = 0, pady=(10, 0), sticky="nsew")
nombre_entry = tk.Entry(root,width=15,font=(15))
nombre_entry.grid(row = 3, column = 1, pady=(10, 0), sticky="W")


boton_registrar = tk.Button(root,text="Registrarse",font=(15)).grid(row=10, column=2, columnspan=2, pady=(20, 10))


root.mainloop()