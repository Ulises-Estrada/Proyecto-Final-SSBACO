import tkinter as tk
from experta import Fact, Rule, KnowledgeEngine
import psycopg2
from conexionDB import create_conn, create_cursor, psycopg2

conn = create_conn()
cursor = create_cursor(conn)

class Sintoma(Fact):
    pass

class Signo(Fact):
    pass

class Diagnostico(KnowledgeEngine):
    # Aquí irían tus reglas. Por ejemplo:
    @Rule(Sintoma(nombre='fiebre'))
    def regla_fiebre(self):
        self.declare(Sintoma(enfermedad='gripe'))

def obtener_enfermedades_desde_bd(sintoma, signo):
    # Aquí conectarías con tu base de datos para obtener las enfermedades
    cursor.execute(f"""
        SELECT e.nombre 
        FROM enfermedades_sintomas es
        JOIN enfermedades e ON es.enfermedad_id = e.id
        JOIN sintomas s ON es.sintoma_id = s.id
        WHERE s.descripcion = '{sintoma}'
        UNION 
        SELECT e.nombre 
        FROM enfermedades_signos eg
        JOIN enfermedades e ON eg.enfermedad_id = e.id
        JOIN signos g ON eg.signo_id = g.id
        WHERE g.descripcion = '{signo}'
    """)
    rows = cursor.fetchall()
    return [row[0] for row in rows]


def diagnosticar(sintoma, signo):
    motor = Diagnostico()
    motor.reset()
    motor.declare(Sintoma(nombre=sintoma))
    motor.declare(Signo(nombre=signo))
    motor.run()
    return motor.facts

"""def boton_diagnosticar_click():
    sintomas = entry_sintoma.get().split(",")  # Esto dividirá los síntomas ingresados por comas
    signos = entry_signo.get().split(",")  # Esto dividirá los signos ingresados por comas
    enfermedades_potenciales = set()

    for sintoma in sintomas:
        sintoma = sintoma.strip()  # Esto eliminará los espacios en blanco alrededor de los nombres de los síntomas
        for signo in signos:
            signo = signo.strip()  # Esto eliminará los espacios en blanco alrededor de los nombres de los signos
            enfermedades = obtener_enfermedades_desde_bd(sintoma, signo)

            if not enfermedades_potenciales:
                enfermedades_potenciales.update(enfermedades)
            else:
                enfermedades_potenciales.intersection_update(enfermedades)

    lista_enfermedades.delete(0, tk.END)

    for enfermedad in enfermedades_potenciales:
        lista_enfermedades.insert(tk.END, enfermedad)"""


def buscar_paciente():
    try:
        id_paciente = id_entry.get()  # Asegúrate de tener un campo de entrada para el ID del paciente
        cursor.execute("SELECT * FROM pacientes WHERE idpaciente = %s", (id_paciente,))
        row = cursor.fetchone()

        if row:
            nombre_entry.delete(0, tk.END)
            nombre_entry.insert(0, row[1])

            apellido_entry.delete(0, tk.END)
            apellido_entry.insert(0, row[2])

            fech_nac_entry.delete(0, tk.END)
            fech_nac_entry.insert(0, row[3])

            genero_entry.delete(0, tk.END)
            genero_entry.insert(0, row[4])

            # Añade aquí más campos según sea necesario

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error al buscar al paciente:", error)

def on_select(event):
    if signo_list.curselection():
        selected = [event.widget.get(i) for i in event.widget.curselection()]
        signo_entry.config(state=tk.NORMAL)
        signo_entry.delete('1.0', tk.END)
        signo_entry.insert(tk.END, ', '.join(selected))
        signo_entry.config(state='disabled')

def on_selectSintomas(event):
    if sintomas_list.curselection():
        selected = [event.widget.get(i) for i in event.widget.curselection()]
        sintomas_entry.config(state=tk.NORMAL)
        sintomas_entry.delete('1.0', tk.END)
        sintomas_entry.insert(tk.END, ', '.join(selected))
        sintomas_entry.config(state='disabled')

root = tk.Tk()
root.title("Registro-Enfermedad")
root.geometry("950x650")

# Frame para los Entry widgets
frame_izquierdo = tk.Frame(root)
frame_izquierdo.grid(row=1, column=0, sticky="nsew")

# Frame para los Listbox y Text widgets
frame_derecho = tk.Frame(root)
frame_derecho.grid(row=1, column=1, sticky="nsew")

bienvenida = tk.Label(root, text="Diagnostico",font=(12,'20')).grid(row=0, column=0, columnspan=4, pady=(10, 10))

info = tk.Label(frame_izquierdo, text="Paciente",font=(12,'15')).grid(row = 1, column = 0, sticky="nsew")

nombre = tk.Label(frame_izquierdo, text="Nombre",font=(15)).grid(row = 3, column = 0,sticky="nsew")
nombre_entry = tk.Entry(frame_izquierdo,width=30,font=(15))
nombre_entry.grid(row = 3, column = 1,sticky="W",pady=(10, 10))

apellido = tk.Label(frame_izquierdo, text="Apellido",font=(15)).grid(row = 4, column = 0,sticky="nsew")
apellido_entry = tk.Entry(frame_izquierdo,width=30,font=(15))
apellido_entry.grid(row = 4, column = 1,sticky="W",pady=(10, 10))

fech_nac = tk.Label(frame_izquierdo, text="Fecha de nacimiento",font=(15)).grid(row = 5, column = 0,sticky="nsew")
fech_nac_entry = tk.Entry(frame_izquierdo,width=20,font=(15))
fech_nac_entry.grid(row = 5, column = 1,sticky="W",pady=(10, 10))

genero = tk.Label(frame_izquierdo, text="Genero",font=(15)).grid(row = 6, column = 0,sticky="nsew")
genero_entry = tk.Entry(frame_izquierdo,width=20,font=(15))
genero_entry.grid(row = 6, column = 1,sticky="W",pady=(10, 10))

id = tk.Label(frame_izquierdo, text="ID",font=(15)).grid(row = 7, column = 0,sticky="nsew")
id_entry = tk.Entry(frame_izquierdo,width=10,font=(15))
id_entry.grid(row = 7, column = 1,sticky="W",pady=(10, 10))


signo = tk.Label(frame_derecho, text="Signos",font=(12,'15')).grid(row = 1, column = 2,sticky="nsew",pady=(10, 10))
signo_list = (tk.Listbox(frame_derecho, selectmode=tk.MULTIPLE,width=30))
signo_list.grid(row = 2, column = 2,sticky="nsew",padx=(10, 10))

cursor.execute("SELECT descripcion FROM signos")

rows = cursor.fetchall()

for row in rows:
    signo_list.insert(tk.END, row[0])

signo_entry = tk.Text(frame_derecho,height=9, width=30,font=(15),state='disabled')
signo_entry.grid(row = 2, column = 3,pady=(10, 10))

signo_list.bind('<<ListboxSelect>>', on_select)

sintomas = tk.Label(frame_derecho, text="Sintomas",font=(12,'15')).grid(row = 3, column = 2,sticky="nsew",pady=(10, 10))
sintomas_list = (tk.Listbox(frame_derecho, selectmode=tk.MULTIPLE))
sintomas_list.grid(row = 4, column = 2,sticky="nsew",padx=(10, 10))

cursor.execute("SELECT descripcion FROM sintomas")

rows = cursor.fetchall()

for row in rows:
    sintomas_list.insert(tk.END, row[0])

sintomas_entry = tk.Text(frame_derecho,height=9, width=30,font=(15),state='disabled')
sintomas_entry.grid(row = 4, column = 3,pady=(10, 10))

sintomas_list.bind('<<ListboxSelect>>', on_selectSintomas)

boton_buscar = tk.Button(frame_izquierdo,text="Buscar con ID", command=buscar_paciente,font=(15)).grid(row=8, column=1,sticky="nsew",pady=(10, 0))

info = tk.Label(frame_izquierdo, text="Datos",font=(12,'15')).grid(row = 9, column = 0, sticky="nsew")

hora = tk.Label(frame_izquierdo, text="Hora",font=(15)).grid(row = 10, column = 0,sticky="nsew")
hora_entry = tk.Entry(frame_izquierdo,width=30,font=(15))
hora_entry.grid(row = 10, column = 1,sticky="W",pady=(10, 10))

fech_diag = tk.Label(frame_izquierdo, text="Fecha consulta",font=(15)).grid(row = 11, column = 0,sticky="nsew")
fech_diag_entry = tk.Entry(frame_izquierdo,width=30,font=(15))
fech_diag_entry.grid(row = 11, column = 1,sticky="W",pady=(10, 10))

info = tk.Label(frame_izquierdo, text="Examenes",font=(12,'15')).grid(row = 12, column = 0, sticky="nsew")

presion = tk.Label(frame_izquierdo, text="Presion arterial",font=(15)).grid(row = 13, column = 0,sticky="nsew")
presion_entry = tk.Entry(frame_izquierdo,width=30,font=(15))
presion_entry.grid(row = 13, column = 1,sticky="W",pady=(10, 10))

temp = tk.Label(frame_izquierdo, text="Temperatura",font=(15)).grid(row = 14, column = 0,sticky="nsew")
temp_entry = tk.Entry(frame_izquierdo,width=30,font=(15))
temp_entry.grid(row = 14, column = 1,sticky="W",pady=(10, 10))

temp = tk.Label(frame_izquierdo, text="Frecuencia cardiaca",font=(15)).grid(row = 15, column = 0,sticky="nsew")
temp_entry = tk.Entry(frame_izquierdo,width=30,font=(15))
temp_entry.grid(row = 15, column = 1,sticky="W",pady=(10, 10))


root.mainloop()
