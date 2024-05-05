import tkinter as tk
from experta import Fact, Rule, KnowledgeEngine
import psycopg2 
from conexionDB import create_conn, create_cursor, psycopg2

conn = create_conn()
cursor = create_cursor(conn)

"""
CREATE TABLE enfermedades_sintomas (
    id SERIAL PRIMARY KEY,
    enfermedad VARCHAR(255),
    sintoma VARCHAR(255)
);

INSERT INTO enfermedades_sintomas (enfermedad, sintoma) VALUES
('Gripe', 'Fiebre'),
('Gripe', 'Tos'),
('Gripe', 'Dolor de garganta'),
('Gripe', 'Congestión nasal'),
('Gripe', 'Dolor muscular'),
('Gripe', 'Fatiga'),
('COVID-19', 'Fiebre'),
('COVID-19', 'Tos seca'),
('COVID-19', 'Fatiga'),
('COVID-19', 'Dificultad para respirar'),
('COVID-19', 'Dolor de garganta'),
('COVID-19', 'Pérdida del gusto y el olfato');

"""

class Sintoma(Fact):
    pass

class Diagnostico(KnowledgeEngine):
    # Aquí irían tus reglas. Por ejemplo:
    @Rule(Sintoma(nombre='fiebre'))
    def regla_fiebre(self):
        self.declare(Sintoma(enfermedad='gripe'))

def obtener_sintomas_desde_bd(sintoma):
    # Aquí conectarías con tu base de datos para obtener los síntomas
    cursor.execute(f"SELECT enfermedad FROM enfermedades_sintomas WHERE sintoma = '{sintoma}'")
    rows = cursor.fetchall()
    return [row[0] for row in rows]

def diagnosticar(sintoma):
    motor = Diagnostico()
    motor.reset()
    motor.declare(Sintoma(nombre=sintoma))
    motor.run()
    return motor.facts


def boton_diagnosticar_click():
    sintomas = entry_sintoma.get().split(",")  # Esto dividirá los síntomas ingresados por comas
    enfermedades_potenciales = set()

    for sintoma in sintomas:
        sintoma = sintoma.strip()  # Esto eliminará los espacios en blanco alrededor de los nombres de los síntomas
        enfermedades = obtener_sintomas_desde_bd(sintoma)

        if not enfermedades_potenciales:
            enfermedades_potenciales.update(enfermedades)
        else:
            enfermedades_potenciales.intersection_update(enfermedades)

    lista_enfermedades.delete(0, tk.END)

    for enfermedad in enfermedades_potenciales:
        lista_enfermedades.insert(tk.END, enfermedad)

root = tk.Tk()

label_sintoma = tk.Label(root, text="Síntoma")
label_sintoma.pack()

entry_sintoma = tk.Entry(root)
entry_sintoma.pack()

boton_diagnosticar = tk.Button(root, text="Diagnosticar", command=boton_diagnosticar_click)
boton_diagnosticar.pack()

lista_enfermedades = tk.Listbox(root)
lista_enfermedades.pack()

root.mainloop()