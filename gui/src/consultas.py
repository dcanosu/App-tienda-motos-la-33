from conexion import conexion_bd

def consultar_empleados():
    conexion, cursor = conexion_bd()  # Obtener conexion y cursor
    if not conexion or not cursor:
        print("❌ No se pudo establecer conexión con la base de datos.")
        return
    
    try:
        # Consulta de datos
        cursor.execute("SELECT * FROM tbl_empleados")
        empleados = cursor.fetchall()

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

def insertar_valores():
    conexion, cursor = conexion_bd()  # Obtener conexion y cursor
    if not conexion or not cursor:
        print("❌ No se pudo establecer conexión con la base de datos.")
        return
    try:
        # Consulta de datos
        cursor.execute("""INSERT INTO tbl_clientes (tipo_documento_cliente, numero_documento_cliente, nombre_cliente, apellido_cliente, direccion_cliente, telefono_cliente, correo_cliente) 
                    VALUES
                    ('Cédula de ciudadanía', '1001234567', 'Juan', 'Pérez', 'Calle 10 #20-30', '3001234567', 'juan.perez@email.com'),
                    ('Cédula de extranjería', '2002345678', 'Emily', 'Smith', 'Carrera 15 #45-50', '3102345678', 'emily.smith@email.com'),
                    ('Pasaporte', 'A12345678', 'Michael', 'Johnson', 'Avenida 5 #12-34', '3203456789', 'michael.johnson@email.com'),
                    ('Permiso Especial de Permanencia', 'P34567890', 'Carlos', 'Gómez', 'Diagonal 30 #25-40', '3004567890', 'carlos.gomez@email.com'),
                    ('Cédula de ciudadanía', '1012345678', 'Ana', 'Martínez', 'Transversal 8 #16-25', '3015678901', 'ana.martinez@email.com'),
                    ('Cédula de extranjería', '2023456789', 'David', 'Brown', 'Calle 50 #10-20', '3026789012', 'david.brown@email.com'),
                    ('Pasaporte', 'B98765432', 'Laura', 'Hernández', 'Carrera 80 #32-10', '3037890123', 'laura.hernandez@email.com'),
                    ('Permiso Especial de Permanencia', 'P56789012', 'Andrés', 'Ramírez', 'Avenida 33 #22-50', '3048901234', 'andres.ramirez@email.com'),
                    ('Cédula de ciudadanía', '1034567890', 'Sofía', 'Torres', 'Diagonal 44 #9-18', '3059012345', 'sofia.torres@email.com'),
                    ('Cédula de extranjería', '2045678901', 'Jorge', 'López', 'Calle 20 #8-55', '3060123456', 'jorge.lopez@email.com');""")
        conexion.commit()
        
        cursor.execute("""INSERT INTO tbl_empleados (tipo_documento_empleado, numero_documento_empleado, nombre_empleado, apellido_empleado, cargo_empleado, direccion_empleado, telefono_empleado, correo_empleado) 
                    VALUES
                    ('Cédula de ciudadanía', '1101234567', 'Luis', 'García', 'Coordinador', 'Calle 12 #30-40', '3101234567', 'luis.garcia@email.com'),
                    ('Cédula de extranjería', '2202345678', 'María', 'Fernández', 'Auxiliar', 'Carrera 8 #25-50', '3202345678', 'maria.fernandez@email.com'),
                    ('Pasaporte', 'C12345678', 'James', 'Williams', 'Vendedor', 'Avenida 15 #10-22', '3303456789', 'james.williams@email.com'),
                    ('Permiso Especial de Permanencia', 'P67890123', 'Andrea', 'Rodríguez', 'Cajero', 'Diagonal 45 #14-32', '3404567890', 'andrea.rodriguez@email.com'),
                    ('Cédula de ciudadanía', '1112345678', 'Pedro', 'López', 'Vendedor', 'Transversal 5 #20-10', '3115678901', 'pedro.lopez@email.com'),
                    ('Cédula de extranjería', '2223456789', 'Camila', 'Martínez', 'Auxiliar', 'Calle 33 #15-44', '3126789012', 'camila.martinez@email.com'),
                    ('Pasaporte', 'D98765432', 'Roberto', 'Díaz', 'Coordinador', 'Carrera 77 #40-15', '3137890123', 'roberto.diaz@email.com'),
                    ('Permiso Especial de Permanencia', 'P78901234', 'Elena', 'Gómez', 'Cajero', 'Avenida 28 #30-12', '3148901234', 'elena.gomez@email.com'),
                    ('Cédula de ciudadanía', '1134567890', 'Javier', 'Ruiz', 'Auxiliar', 'Diagonal 20 #5-18', '3159012345', 'javier.ruiz@email.com'),
                    ('Cédula de extranjería', '2245678901', 'Paula', 'Torres', 'Vendedor', 'Calle 50 #8-55', '3160123456', 'paula.torres@email.com');""")
        conexion.commit()
        
        cursor.execute("""INSERT INTO tbl_motos (ref_moto, modelo, color, precio, cantidad_disponible) 
                    VALUES
                    ('CBR500R', 2023, 'Rojo', 35000000, 5),
                    ('XRE300', 2024, 'Negro', 28000000, 3),
                    ('CRF250L', 2023, 'Blanco', 25000000, 4),
                    ('CB500X', 2024, 'Gris', 38000000, 2),
                    ('NC750X', 2023, 'Azul', 42000000, 3),
                    ('CBR650R', 2024, 'Rojo', 48000000, 1),
                    ('XR190L', 2023, 'Blanco', 15000000, 6),
                    ('CRF450R', 2024, 'Rojo', 32000000, 2),
                    ('CB125F', 2023, 'Negro', 9000000, 8),
                    ('PCX160', 2024, 'Gris', 17000000, 5);""")
        conexion.commit()
        
        cursor.execute("""INSERT INTO tbl_proveedores (nit, nombre_proveedor, direccion_proveedor, telefono_proveedor, correo_proveedor) 
                    VALUES
                    ('900123456', 'Honda Colombia S.A.', 'Calle 30 #15-50, Bogotá', '3101234567', 'contacto@hondacolombia.com'),
                    ('900234567', 'Motos y Repuestos S.A.S.', 'Carrera 45 #20-30, Medellín', '3202345678', 'ventas@motosyrepuestos.com'),
                    ('900345678', 'Distribuidora Motriz Ltda.', 'Avenida 10 #12-40, Cali', '3303456789', 'info@dismotriz.com'),
                    ('900456789', 'Importadora de Motos S.A.', 'Diagonal 5 #30-25, Barranquilla', '3404567890', 'importaciones@motos.com'),
                    ('900567890', 'MotoPartes Express', 'Transversal 12 #8-55, Bucaramanga', '3505678901', 'contacto@motopartesexpress.com'),
                    ('900678901', 'Repuestos Honda Oficial', 'Calle 50 #22-10, Pereira', '3606789012', 'ventas@repuestoshonda.com'),
                    ('900789012', 'MotoRepuestos y Accesorios', 'Carrera 8 #15-33, Cartagena', '3707890123', 'soporte@motoaccesorios.com'),
                    ('900890123', 'Mundo Motor S.A.', 'Avenida 25 #40-60, Cúcuta', '3808901234', 'ventas@mundomotor.com'),
                    ('900901234', 'MotoDistribuciones Ltda.', 'Calle 60 #30-20, Ibagué', '3909012345', 'contacto@motodistribuciones.com'),
                    ('900012345', 'ImportMotos S.A.S.', 'Diagonal 75 #18-44, Manizales', '3000123456', 'importaciones@importmotos.com');""")
        conexion.commit()
        
        cursor.execute("""INSERT INTO tbl_ventas (id_cliente, id_empleado, fecha_venta, total_venta) 
                    VALUES
                    (1, 2, '2025-03-01', 15000000),
                    (2, 3, '2025-03-02', 22000000),
                    (3, 1, '2025-03-03', 18000000),
                    (4, 5, '2025-03-04', 27000000),
                    (5, 4, '2025-03-05', 35000000),
                    (6, 2, '2025-03-06', 9000000),
                    (7, 6, '2025-03-07', 42000000),
                    (8, 8, '2025-03-08', 28000000),
                    (9, 9, '2025-03-09', 17000000),
                    (10, 7, '2025-03-10', 32000000);""")
        conexion.commit()
        
        cursor.execute("""INSERT INTO tbl_pedidos (id_proveedor, fecha_pedido, valor_total_pedido) VALUES
                    (1, '2025-03-01', 350000.00),
                    (2, '2025-03-02', 520000.50),
                    (3, '2025-03-03', 198000.75),
                    (4, '2025-03-04', 425500.00),
                    (5, '2025-03-05', 610000.90),
                    (1, '2025-03-06', 730000.30),
                    (2, '2025-03-07', 150000.00),
                    (3, '2025-03-08', 290500.80),
                    (4, '2025-03-09', 380000.20),
                    (5, '2025-03-10', 495000.50);""")
        conexion.commit()
        
        cursor.execute("""INSERT INTO tbl_detalle_pedido (id_pedido, id_moto, cantidad, precio_unitario) VALUES
                    (1, 1, 2, 15000000),
                    (1, 2, 1, 12000000),
                    (2, 3, 3, 18000000),
                    (2, 4, 1, 17500000),
                    (3, 5, 2, 16000000),
                    (4, 6, 1, 14500000),
                    (4, 7, 2, 15500000),
                    (5, 8, 1, 17000000),
                    (6, 9, 3, 19000000),
                    (6, 10, 1, 20000000);""")
        conexion.commit()
        
        cursor.execute("""INSERT INTO tbl_detalle_venta (id_moto, id_venta, cantidad, precio_unitario) VALUES
                    (1, 1, 1, 15000000),
                    (2, 1, 2, 12000000),
                    (3, 2, 1, 18000000),
                    (4, 3, 2, 17500000),
                    (5, 3, 1, 16000000),
                    (6, 4, 3, 14500000),
                    (7, 5, 1, 15500000),
                    (8, 5, 2, 17000000),
                    (9, 6, 1, 19000000),
                    (10, 6, 3, 20000000);""")
        conexion.commit()
        
    except Exception as e:
        print(f"❌ Error al ejecutar la consulta: {e}")

    finally:
        cursor.close()  # Cerrar el cursor primero
        conexion.close()  # Luego cerrar la conexión
        print("🔒 Conexión cerrada correctamente")

def consultar_valores():
    conexion, cursor = conexion_bd()  # Obtener conexion y cursor
    if not conexion or not cursor:
        print("❌ No se pudo establecer conexión con la base de datos.")
        return
    
    try:
        # Consulta de datos
        cursor.execute("""
                    SELECT dp.id_pedido, m.id_moto, m.ref_moto, dp.cantidad, dp.precio_unitario, 
                    (dp.cantidad * dp.precio_unitario) AS subtotal
                    FROM tbl_detalle_pedido dp
                    JOIN tbl_motos m ON dp.id_moto = m.id_moto;""")
        cursor.fetchall()

    except Exception as e:
        print(f"❌ Error al ejecutar la consulta: {e}")

    finally:
        cursor.close()  # Cerrar el cursor primero
        conexion.close()  # Luego cerrar la conexión
        print("🔒 Conexión cerrada correctamente")

# Ejecutar la consulta
if __name__ == "__main__":
    consultar_valores()