from src.conexion import conexion_bd

def guardar_empleado_bd(empleado):
    """ Guarda un empleado en la base de datos """
    Empleado = dict(empleado)
    
    try:
        conexion, cursor = conexion_bd()  # Obtener conexión y cursor
        if not conexion or not cursor:
            print("❌ No se pudo establecer conexión con la base de datos.")
            return {"RESPUESTA": False, "Mensaje": "No se pudo conectar a la base de datos"}

        columnas = tuple(Empleado.keys())
        valores = tuple(Empleado.values())

        consulta = """INSERT INTO tbl_empleados {campos} VALUES(?,?,?,?,?,?,?,?,?,?)""".format(campos=columnas)

        cursor.execute(consulta, valores)

        conexion.commit()
        creado = cursor.rowcount > 0
        if creado:
            return {"RESPUESTA": True, "Mensaje": "Empleado registrado con éxito"}
        else:
            return {"RESPUESTA": False, "Mensaje": "Empleado ¡NO! registrado con éxito"}
    
    except Exception as ex:
        return {"RESPUESTA": False, "Mensaje": str(ex)}

def buscar_empleado_bd(numero_documento):
    """ Busca un empleado en la base de datos por su número de documento """
    try:
        conexion, cursor = conexion_bd()
        if not conexion or not cursor:
            print("❌ No se pudo establecer conexión con la base de datos.")
            return {"RESPUESTA": False, "Mensaje": "No se pudo conectar a la base de datos"}

        consulta = "SELECT * FROM tbl_empleados WHERE numero_documento_empleado = ?"
        cursor.execute(consulta, (numero_documento,))
        empleado = cursor.fetchone()

        if empleado:
            return {"RESPUESTA": True, "Empleado": empleado}
        else:
            return {"RESPUESTA": False, "Mensaje": "Empleado no encontrado"}

    except Exception as ex:
        return {"RESPUESTA": False, "Mensaje": str(ex)}

def eliminar_empleado_bd(numero_documento):
    """ Elimina un empleado de la base de datos basado en su número de documento """
    try:
        conexion, cursor = conexion_bd()  # Obtener conexión y cursor
        if not conexion or not cursor:
            print("❌ No se pudo establecer conexión con la base de datos.")
            return {"RESPUESTA": False, "Mensaje": "No se pudo conectar a la base de datos"}

        consulta = "DELETE FROM tbl_empleados WHERE numero_documento_empleado = ?"
        cursor.execute(consulta, (numero_documento,))

        conexion.commit()
        eliminado = cursor.rowcount > 0
        if eliminado:
            return {"RESPUESTA": True, "Mensaje": "Empleado eliminado con éxito"}
        else:
            return {"RESPUESTA": False, "Mensaje": "Empleado no encontrado"}

    except Exception as ex:
        return {"RESPUESTA": False, "Mensaje": str(ex)}

def actualizar_empleado_bd(empleado_actualizado):
    try:
        conexion, cursor = conexion_bd()  # Obtener conexión y cursor
        if not conexion or not cursor:
            print("❌ No se pudo establecer conexión con la base de datos.")
            return {"RESPUESTA": False, "Mensaje": "No se pudo conectar a la base de datos"}

        consulta = """UPDATE tbl_empleados 
                      SET tipo_documento_empleado = ?, nombre_empleado = ?, apellido_empleado = ?, 
                          cargo_empleado = ?, direccion_empleado = ?, telefono_empleado = ?, correo_empleado = ?
                      WHERE numero_documento_empleado = ?"""

        valores = (
            empleado_actualizado["tipo_documento_empleado"],
            empleado_actualizado["nombre_empleado"],
            empleado_actualizado["apellido_empleado"],
            empleado_actualizado["cargo_empleado"],
            empleado_actualizado["direccion_empleado"],
            empleado_actualizado["telefono_empleado"],
            empleado_actualizado["correo_empleado"],
            empleado_actualizado["numero_documento_empleado"]
        )

        cursor.execute(consulta, valores)

        conexion.commit()
        actualizado = cursor.rowcount > 0
        if actualizado:
            return {"RESPUESTA": True, "Mensaje": "Empleado actualizado con éxito"}
        else:
            return {"RESPUESTA": False, "Mensaje": "Empleado no encontrado o sin cambios"}

    except Exception as ex:
        return {"RESPUESTA": False, "Mensaje": str(ex)}
