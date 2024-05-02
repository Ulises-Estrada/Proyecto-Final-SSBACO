import psycopg2
def create_conn():
    # Crear una conexión a la base de datos
        conexion = psycopg2.connect(
            database="proyectoFinal",
            user="postgres",
            password="",
            host="localhost",
            port="5432"
        )
        return conexion

def create_cursor(conexion):
    cur = conexion.cursor()
    return cur

def close_conn(conexion):
    conexion.close()