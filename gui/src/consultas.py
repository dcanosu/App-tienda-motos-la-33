from conexion import conexion_bd

def consultar_empleados():
    conexion, cursor = conexion_bd()  # Obtener conexion y cursor
    if not conexion or not cursor:
        print("❌ No se pudo establecer conexión con la base de datos.")
        return
    
    try:
        # Consulta de datos
        cursor.execute("SELECT * FROM tbl_clientes")
        empleados = cursor.fetchall()  # Obtener todos los registros

        # Mostrar los resultados
        if empleados:
            for empleado in empleados:
                print(empleado)
        else:
            print("❌ No hay empleados registrados en la base de datos.")
            
    except Exception as e:
        print(f"❌ Error al ejecutar la consulta: {e}")

    finally:
        cursor.close()  # Cerrar el cursor primero
        conexion.close()  # Luego cerrar la conexión
        print("🔒 Conexión cerrada correctamente")

# Ejecutar la consulta
if __name__ == "__main__":
    consultar_empleados()