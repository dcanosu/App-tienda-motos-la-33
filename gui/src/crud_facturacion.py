from src.conexion import conexion_bd

def guardar_venta_bd(venta):
    try:
        conexion, cursor = conexion_bd()
        if not conexion or not cursor:
            print("❌ No se pudo establecer conexión con la base de datos.")
            return {"RESPUESTA": False, "Mensaje": "No se pudo conectar a la base de datos"}

        consulta = """INSERT INTO tbl_ventas 
                    (id_cliente, id_empleado, fecha_venta, total_venta) 
                    VALUES (?, ?, ?, ?)"""
        valores = (
            venta["id_cliente"],
            venta["id_empleado"],
            venta["fecha_venta"],
            venta["total_venta"]
        )

        cursor.execute(consulta, valores)
        conexion.commit()

        creado = cursor.rowcount > 0
        if creado:
            return {"RESPUESTA": True, "Mensaje": "Venta registrada con éxito"}
        else:
            return {"RESPUESTA": False, "Mensaje": "Venta ¡NO! registrada"}

    except Exception as ex:
        return {"RESPUESTA": False, "Mensaje": str(ex)}

def buscar_venta_bd(id_venta):
    try:
        conexion, cursor = conexion_bd()
        if not conexion or not cursor:
            print("❌ No se pudo establecer conexión con la base de datos.")
            return {"RESPUESTA": False, "Mensaje": "No se pudo conectar a la base de datos"}

        consulta = "SELECT * FROM tbl_ventas WHERE id_venta = ?"
        cursor.execute(consulta, (id_venta,))
        venta = cursor.fetchone()

        if venta:
            return {"RESPUESTA": True, "Venta": venta}
        else:
            return {"RESPUESTA": False, "Mensaje": "Venta no encontrada"}

    except Exception as ex:
        return {"RESPUESTA": False, "Mensaje": str(ex)}

def eliminar_venta_bd(id_venta):
    try:
        conexion, cursor = conexion_bd()
        if not conexion or not cursor:
            print("❌ No se pudo establecer conexión con la base de datos.")
            return {"RESPUESTA": False, "Mensaje": "No se pudo conectar a la base de datos"}

        consulta = "DELETE FROM tbl_ventas WHERE id_venta = ?"
        cursor.execute(consulta, (id_venta,))
        conexion.commit()

        eliminado = cursor.rowcount > 0
        if eliminado:
            return {"RESPUESTA": True, "Mensaje": "Venta eliminada con éxito"}
        else:
            return {"RESPUESTA": False, "Mensaje": "Venta no encontrada"}

    except Exception as ex:
        return {"RESPUESTA": False, "Mensaje": str(ex)}

def actualizar_venta_bd(venta_actualizada):
    try:
        conexion, cursor = conexion_bd()
        if not conexion or not cursor:
            print("❌ No se pudo establecer conexión con la base de datos.")
            return {"RESPUESTA": False, "Mensaje": "No se pudo conectar a la base de datos"}

        consulta = """UPDATE tbl_ventas 
                    SET id_cliente = ?, id_empleado = ?, fecha_venta = ?, total_venta = ? 
                    WHERE id_venta = ?"""
        valores = (
            venta_actualizada["id_cliente"],
            venta_actualizada["id_empleado"],
            venta_actualizada["fecha_venta"],
            venta_actualizada["total_venta"],
            venta_actualizada["id_venta"]
        )

        cursor.execute(consulta, valores)
        conexion.commit()

        actualizado = cursor.rowcount > 0
        if actualizado:
            return {"RESPUESTA": True, "Mensaje": "Venta actualizada con éxito"}
        else:
            return {"RESPUESTA": False, "Mensaje": "Venta no encontrada o sin cambios"}

    except Exception as ex:
        return {"RESPUESTA": False, "Mensaje": str(ex)}

def buscar_cliente_dni(numero_documento):
    try:
        conexion, cursor = conexion_bd()
        if not conexion or not cursor:
            print("❌ No se pudo establecer conexión con la base de datos.")
            return {"RESPUESTA": False, "Mensaje": "No se pudo conectar a la base de datos"}

        consulta = "SELECT * FROM tbl_clientes WHERE numero_documento_cliente = ?"
        cursor.execute(consulta, (numero_documento,))
        cliente = cursor.fetchone()

        if cliente:
            return {"RESPUESTA": True, "Cliente": cliente}
        else:
            return {"RESPUESTA": False, "Mensaje": "Cliente no encontrado"}

    except Exception as ex:
        return {"RESPUESTA": False, "Mensaje": str(ex)}

def listar_detalles_ventas_empleado_db():
    try:
        conexion, cursor = conexion_bd()
        if not conexion or not cursor:
            print("❌ No se pudo establecer conexión con la base de datos.")
            return {"RESPUESTA": False, "Mensaje": "No se pudo conectar a la base de datos"}

        consulta = """SELECT 
                        e.id_empleado, 
                        e.nombre_empleado, 
                        e.apellido_empleado, 
                        e.cargo_empleado,
                        COALESCE(SUM(ve.total_venta), 0) AS total_ventas
                    FROM tbl_empleados e
                    LEFT JOIN tbl_ventas ve ON e.id_empleado = ve.id_empleado
                    GROUP BY e.id_empleado, e.nombre_empleado, e.apellido_empleado, e.cargo_empleado
                    ORDER BY total_ventas DESC"""
        
        cursor.execute(consulta)
        resultados = cursor.fetchall()

        if resultados:
            empleados_ventas = [
                {
                    "ID Empleado": fila[0],
                    "Nombre": fila[1],
                    "Apellido": fila[2],
                    "Cargo": fila[3],
                    "Total Ventas": fila[4]
                }
                for fila in resultados
            ]
            return {"RESPUESTA": True, "Empleados": empleados_ventas}
        else:
            return {"RESPUESTA": False, "Mensaje": "No se encontraron ventas registradas"}

    except Exception as ex:
        return {"RESPUESTA": False, "Mensaje": str(ex)}