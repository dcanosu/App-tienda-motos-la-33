# Importar la libreria sql3lite para realizar la conexión y las diferentes transacciones
import sqlite3 as bd

# Crear un metodo para crear la conexión
def conexion():
    # Apertura de la conexión a la base de datos
    conexion = bd.connect("db_tienda_motos_la33.db")
    cursor = conexion.cursor()

    try:
        # Crear la tabla motos
        tbl_motos: str = """
        CREATE TABLE IF NOT EXISTS tbl_motos(
            id_moto INTEGER PRIMARY KEY AUTOINCREMENT,
            ref_moto VARCHAR(20) NOT NULL,
            modelo TEXT NOT NULL,
            color VARCHAR(20) NOT NULL,
            precio DOUBLE NOT NULL,
            cantidad_disponible INTEGER
            );
        """
        cursor.execute(tbl_motos)
        conexion.commit()
        print("✅ tabla [tbl_motos] creada con éxito")
        
        # Crear la tabla proveedores        
        tbl_proveedores = """
        CREATE TABLE IF NOT EXISTS tbl_proveedores(
            id_proveedor INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_proveedor VARCHAR(50) NOT NULL,
            direccion_proveedor VARCHAR(50) NOT NULL,
            telefono_proveedor VARCHAR(10) NOT NULL,
            correo_proveedor VARCHAR(50) NOT NULL
            );
        """
        cursor.execute(tbl_proveedores)
        conexion.commit()
        print("✅ tabla [tbl_proveedores] creada con éxito")
        
        # Crear tabla empleados
        tbl_empleados = """
        CREATE TABLE IF NOT EXISTS tbl_empleados(
            id_empleado INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_empleado VARCHAR(50) NOT NULL,
            apellido_empleado VARCHAR(50) NOT NULL,
            cargo_empleado VARCHAR(50) NOT NULL,
            direccion_empleado VARCHAR(50) NOT NULL,
            telefono_empleado VARCHAR(10) NOT NULL,
            correo_empleado VARCHAR(50) NOT NULL
            );
        """
        cursor.execute(tbl_empleados)
        conexion.commit()
        print("✅ tabla [tbl_empleados] creada con éxito")
        
        # Crear tabla clientes
        tbl_clientes = """
        CREATE TABLE IF NOT EXISTS tbl_clientes(
            id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_cliente VARCHAR(50) NOT NULL,
            apellido_cliente VARCHAR(50) NOT NULL,
            direccion_cliente VARCHAR(50) NOT NULL,
            telefono_cliente VARCHAR(50) NOT NULL,
            correo_cliente VARCHAR(50) NOT NULL
            );
        """
        cursor.execute(tbl_clientes)
        conexion.commit()
        print("✅ tabla [tbl_clientes] creada con éxito")
        
    except Exception as e:
        print(f"❌ Error {e}")
    finally:
        # Cerrar la conexión de cursor y conexión a la base de datos
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

if __name__ == "__main__":
    conexion()

