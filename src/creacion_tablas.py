import time
from src.conexion import conexion_bd

def crear_tablas():
    print("⏳ Conectando a la base de datos...")
    time.sleep(3)  # Simula el tiempo de conexión
    conn, cur = conexion_bd()
    
    if not conn or not cur:
        print("❌ No se pudo establecer conexión con la base de datos.")
        return
    
    try:
        print("🚀 Creando tablas principales...")
        time.sleep(0.5)
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
        cur.execute(tbl_motos)
        conn.commit()
        print("✅ tabla [tbl_motos] creada con éxito")
        
        time.sleep(0.5)      
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
        cur.execute(tbl_proveedores)
        conn.commit()
        print("✅ tabla [tbl_proveedores] creada con éxito")
        
        time.sleep(0.5)
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
        cur.execute(tbl_empleados)
        conn.commit()
        print("✅ tabla [tbl_empleados] creada con éxito")
        
        time.sleep(0.5)
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
        cur.execute(tbl_clientes)
        conn.commit()
        print("✅ tabla [tbl_clientes] creada con éxito")
        
    except Exception as e:
        print(f"❌ Error al crear las tablas: {e}")

    finally:
        cur.close()
        conn.close()
        print("-> query ejecutada con éxito")  
        print("🔒 Conexión cerrada correctamente")

def crear_tablas_relacionales():
    print("⏳ Conectando a la base de datos...")
    time.sleep(3)
    conn, cur = conexion_bd()

    if not conn or not cur:
        print("❌ No se pudo establecer conexión con la base de datos.")
        return
    
    try:
        tablas_relacionadas = {
            "tbl_pedidos":"""
                CREATE TABLE IF NOT EXISTS tbl_pedidos(
                    id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_proveedor INTEGER,
                    fecha_pedido TEXT,
                    valor_total_pedido DOUBLE,
                    FOREIGN KEY (id_proveedor) REFERENCES tbl_proveedores(id_proveedor)
                );
            """,
            "tbl_detalle_pedido":"""
                CREATE TABLE IF NOT EXISTS tbl_detalle_pedido(
                    id_pedido INTEGER ,
                    id_moto INTEGER ,
                    cantidad INTEGER,
                    precio_unitario DOUBLE,
                    PRIMARY KEY (id_pedido, id_moto),
                    FOREIGN KEY (id_pedido) REFERENCES tbl_pedidos(id_pedido),
                    FOREIGN KEY (id_moto) REFERENCES tbl_motos(id_moto)
                );
            """,
            "tbl_ventas":"""
                CREATE TABLE IF NOT EXISTS tbl_ventas(
                    id_venta INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_cliente INTEGER,
                    id_empleado INTEGER,
                    fecha_venta TEXT,
                    total_venta DOUBLE,
                    FOREIGN KEY (id_cliente) REFERENCES tbl_clientes(id_cliente),
                    FOREIGN KEY (id_empleado) REFERENCES tbl_empleados(id_empleado)
                );
            """,
            "tbl_detalle_venta":"""
                CREATE TABLE IF NOT EXISTS tbl_detalle_venta(
                    id_moto INTEGER,
                    id_venta INTEGER,
                    cantidad INTEGER,
                    precio_unitario DOUBLE,
                    PRIMARY KEY (id_moto, id_venta),
                    FOREIGN KEY (id_moto) REFERENCES tbl_motos(id_moto),
                    FOREIGN KEY (id_venta) REFERENCES tbl_ventas(id_venta)
                );
            """
        }
        
        # Ejecutar la consulta del diccionario en un bucle
        print("🚀 Creando tablas relacionales...")
        for nombre_tabla, query in tablas_relacionadas.items():
            cur.execute(query)
            print(f"✅ Tabla [{nombre_tabla}] creada con éxito")
            time.sleep(0.5)      
        
        conn.commit() # Confirmar todos los cambios al final
    
    except Exception as e:
        print(f"❌ Error al ejecutar la consulta: {e}")
        print("📝 Consulta fallida:\n", query)

    finally:
        cur.close()
        conn.close()        
        print("🔒 Conexión cerrada correctamente")

