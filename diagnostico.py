import tkinter as tk
from conexionDB import create_conn, create_cursor, psycopg2
from tkinter import messagebox

conn = create_conn()
cursor = create_cursor(conn)

def obtener_sintomas_enfermedad(enfermedad_id):
    cursor.execute("SELECT s.descripcion FROM sintomas s JOIN enfermedades_sintomas es ON s.id = es.sintoma_id WHERE es.enfermedad_id = %s", (enfermedad_id,))
    sintomas_enfermedad = [row[0] for row in cursor.fetchall()]
    return sintomas_enfermedad

def obtener_signos_enfermedad(enfermedad_id):
    cursor.execute("SELECT s.descripcion FROM signos s JOIN enfermedades_signos es ON s.id = es.signo_id WHERE es.enfermedad_id = %s", (enfermedad_id,))
    signos_enfermedad = [row[0] for row in cursor.fetchall()]
    return signos_enfermedad

def buscar_paciente():
    try:
        id_paciente = id_entry.get()
        cursor.execute("SELECT * FROM pacientes WHERE id = %s", (id_paciente,))
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

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error al buscar al paciente:", error)

def diagnosticar_enfermedades():
    # Obtener datos del diagnostico
    paciente_id = id_entry.get()
    # hora_diagnostico = hora_entry.get() 
    fecha_diagnostico = fech_diag_entry.get()
    presion_arterial = presion_entry.get()
    temperatura = temp_entry.get()
    frecuencia_cardiaca = frec_card_entry.get()

    # Obtener signos y síntomas seleccionados
    sintomas_seleccionados = [sintomas_list.get(i) for i in sintomas_list.curselection()]
    signos_seleccionados = [signo_list.get(i) for i in signo_list.curselection()]

    # Consultar la base de datos para encontrar las enfermedades asociadas
    enfermedades_probabilidad = {}

    cursor.execute("SELECT id, nombre FROM enfermedades")
    enfermedades = cursor.fetchall()

    for enfermedad_id, nombre in enfermedades:
        # Calcular la probabilidad de esta enfermedad basada en signos y síntomas seleccionados
        probabilidad = calcular_probabilidad(enfermedad_id, sintomas_seleccionados, signos_seleccionados)
        enfermedades_probabilidad[nombre] = probabilidad

    # Ordenar las enfermedades por probabilidad (de mayor a menor)
    enfermedades_probabilidad_ordenadas = sorted(enfermedades_probabilidad.items(), key=lambda x: x[1], reverse=True)

    # Crear una nueva ventana para mostrar el resultado
    resultado_window = tk.Toplevel()
    resultado_window.title("Resultado del Diagnóstico")
    resultado_window.geometry("195x165")

    # Crear una lista para mostrar el resultado
    lista_resultado = tk.Listbox(resultado_window)
    lista_resultado.pack()

    # Mostrar las enfermedades sugeridas junto con su probabilidad
    lista_resultado.delete(0, tk.END)  # Limpiar la lista de enfermedades primero
    for enfermedad, probabilidad in enfermedades_probabilidad_ordenadas:
        lista_resultado.insert(tk.END, f"{enfermedad}: {probabilidad:.2f}%")

    # Obtener el nombre y el porcentaje de la enfermedad con la probabilidad más alta
    enfermedad_mas_probable, probabilidad_mas_alta = enfermedades_probabilidad_ordenadas[0]

    # Agregar un botón para crear el historial médico con los parámetros obtenidos
    boton_crear_historial = tk.Button(resultado_window, text="Crear Historial", command=lambda: crear_historial_medico(paciente_id,fecha_diagnostico,presion_arterial,temperatura,frecuencia_cardiaca,enfermedad_mas_probable,probabilidad_mas_alta))
    # boton_crear_historial.grid(row=16, column=0, sticky="nsew", pady=(10, 0))
    boton_crear_historial.pack()

    # boton_leer_historial = tk.Button(resultado_window, text="Leer Historial", command=leer_historial_medico)
    # boton_leer_historial.grid(row=16, column=1, sticky="nsew", pady=(10, 0))

    # boton_actualizar_historial = tk.Button(resultado_window, text="Actualizar Historial", command=lambda: actualizar_historial_medico(historial_id, fecha_diagnostico, probabilidad))
    # boton_actualizar_historial.grid(row=17, column=0, sticky="nsew", pady=(10, 0))

    # boton_eliminar_historial = tk.Button(resultado_window, text="Eliminar Historial", command=lambda: eliminar_historial_medico(historial_id))
    # boton_eliminar_historial.grid(row=17, column=1, sticky="nsew", pady=(10, 0))

def crear_historial_medico(paciente_id,fecha_diagnostico,presion_arterial,temperatura,frecuencia_cardiaca,enfermedad_mas_probable,probabilidad_mas_alta):
    try:
        # Ejecutar la consulta SQL para insertar un nuevo registro en Historial_Medico
        cursor.execute("""
            INSERT INTO historial_medico (id_paciente, fecha_diagnostico, presion_arterial, temperatura, frecuencia_cardiaca, enfermedad, probabilidad)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (paciente_id,fecha_diagnostico,presion_arterial,temperatura,frecuencia_cardiaca,enfermedad_mas_probable,probabilidad_mas_alta))

        # Confirmar los cambios en la base de datos
        conn.commit()

        print("Historial médico creado exitosamente.")

    except psycopg2.Error as e:
        print("Error al crear el historial médico:", e)


def leer_historial_medico(paciente_id):
    try:
        # Ejecutar la consulta SQL para leer el historial médico de un paciente
        cursor.execute("""
            SELECT * FROM historial_medico WHERE paciente_id = %s""", (paciente_id,))
        
        # Obtener los resultados de la consulta
        historial = cursor.fetchall()

        # Retornar los resultados
        return historial

    except psycopg2.Error as e:
        print("Error al leer el historial médico:", e)

def actualizar_historial_medico(historial_id, fecha_diagnostico, probabilidad):
    try:
        # Ejecutar la consulta SQL para actualizar el historial médico
        cursor.execute("""
            UPDATE historial_medico SET fecha_diagnostico = %s, probabilidad = %s WHERE historial_id = %s""", (fecha_diagnostico, probabilidad, historial_id))

        # Confirmar los cambios en la base de datos
        conn.commit()

        print("Historial médico actualizado exitosamente.")

    except psycopg2.Error as e:
        print("Error al actualizar el historial médico:", e)

def eliminar_historial_medico(historial_id):
    try:
        # Ejecutar la consulta SQL para eliminar el historial médico
        cursor.execute("""
            DELETE FROM historial_medico WHERE historial_id = %s
        """, (historial_id,))

        # Confirmar los cambios en la base de datos
        conn.commit()

        print("Historial médico eliminado exitosamente.")

    except psycopg2.Error as e:
        print("Error al eliminar el historial médico:", e)

def calcular_probabilidad(enfermedad, sintomas_seleccionados, signos_seleccionados):
    # Obtener signos y síntomas asociados a esta enfermedad desde la base de datos
    sintomas_enfermedad = obtener_sintomas_enfermedad(enfermedad)
    signos_enfermedad = obtener_signos_enfermedad(enfermedad)

    # Calcular la cantidad de signos y síntomas compartidos con los seleccionados
    sintomas_compartidos = len(set(sintomas_seleccionados).intersection(sintomas_enfermedad))
    signos_compartidos = len(set(signos_seleccionados).intersection(signos_enfermedad))

    # Calcular la probabilidad como el porcentaje de signos y síntomas compartidos
    total_sintomas_signos_enfermedad = len(sintomas_enfermedad) + len(signos_enfermedad)
    probabilidad = ((sintomas_compartidos + signos_compartidos) / total_sintomas_signos_enfermedad) * 100

    return probabilidad

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

lista_enfermedades = (tk.Listbox(frame_derecho, selectmode=tk.MULTIPLE))
lista_enfermedades.grid(row = 5, column = 3,sticky="nsew",padx=(10, 10))

boton_diagnosticar = tk.Button(frame_derecho, text="Diagnosticar",command=diagnosticar_enfermedades,font=(15))
boton_diagnosticar.grid(row=5, column=2,sticky="nsew",pady=(10, 0))

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

frec_card = tk.Label(frame_izquierdo, text="Frecuencia cardiaca",font=(15)).grid(row = 15, column = 0,sticky="nsew")
frec_card_entry = tk.Entry(frame_izquierdo,width=30,font=(15))
frec_card_entry.grid(row = 15, column = 1,sticky="W",pady=(10, 10))

root.mainloop()