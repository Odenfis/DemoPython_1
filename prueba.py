import psycopg2

# Configuración de la conexión a la base de datos
DB_HOST = 'dpg-co7nn3a1hbls73ed3cr0-a.oregon-postgres.render.com'
DB_NAME = 'odarusdb'
DB_USER = 'odarus'
DB_PASSWORD = 'Mn907bM0orDoDIO0yEQw0ZwxMSKbLLML'

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
