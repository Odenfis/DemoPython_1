import psycopg2

# Configuración de la conexión a la base de datos
DB_HOST = 'dpg-cr6bdj1u0jms73bn1teg-a.oregon-postgres.render.com'
DB_NAME = 'dbtest_h0hy'
DB_USER = 'dbtest_h0hy_user'
DB_PASSWORD = 'xkmD4V6rmoGNJ27uGLq1k76ynORQ8HTd'

def conectar_db():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
        return conn
    except psycopg2.Error as e:
        print("Error al conectar a la base de datos:", e)
        return None

def verificar_conexion():
    conn = conectar_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT version();")
            version = cursor.fetchone()
            print("Conexión exitosa a PostgreSQL")
            print("Versión del servidor:", version[0])
        except psycopg2.Error as e:
            print("Error al ejecutar la consulta:", e)
        finally:
            conn.close()
    else:
        print("No se pudo establecer la conexión")

verificar_conexion()
