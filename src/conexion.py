# Importar la libreria sql3lite para realizar la conexión y las diferentes transacciones
import sqlite3 as bd

# Método para crear la conexión
def conexion_bd():
    try:
        # Apertura de la conexión a la base de datos
        conexion = bd.connect("db_tienda_motos_la33.db")
        cursor = conexion.cursor()
        print("✅ Conexión exitosa a la base de datos")
        return conexion, cursor # Retornar conexion y cursor

    except Exception as e:
        print(f"❌ Error al conectar con la base de datos: {e}")
        return None, None # Retornar valores seguros en caso de error

if __name__ == "__main__":
    conexion, cursor = conexion_bd()
    if conexion:
        conexion.close()
        print("🔒 Conexión cerrada correctamente")


