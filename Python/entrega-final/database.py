import mysql.connector
from mysql.connector import Error
from colorama import Fore

#Configuración de la conexión a la base de datos
DB_CONFIG = {
    'host': 'localhost',
    'database': 'almacen_db',
    'user': 'root',
    'password': '1234',
    'port': 3306
}

try:
    # 1. Conectar a MySQL general
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    #2. Crear la base de datos si no existe
    cursor.execute("CREATE DATABASE IF NOT EXISTS almacen_db")
    print(f"{Fore.GREEN}✅ Base de datos 'almacen_db' verificada/creada correctamente.")
    
    #3. Usar la base de datos
    cursor.execute("USE almacen_db")
    
    #4. Crear la tabla de productos si no existe
    tabla_query = """
    CREATE TABLE IF NOT EXISTS productos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        categoria VARCHAR(100) NOT NULL,
        precio DECIMAL(10, 2) NOT NULL
    )
    """
    cursor.execute(tabla_query)
    print(f"{Fore.GREEN}✅ Tabla 'productos' verificada/creada correctamente.")
    
except Error as e:
    print(f"{Fore.RED}❌ Error al conectar o configurar la base de datos: {e}")
finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        
def conectar_bd():
    """Función para conectar a la base de datos y retornar la conexión y el cursor."""
    try:
        # El asterisco ** desempaqueta el diccionario DB_CONFIG#
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print(f"{Fore.RED}❌ Error al conectar a la base de datos: {e}")
        return None