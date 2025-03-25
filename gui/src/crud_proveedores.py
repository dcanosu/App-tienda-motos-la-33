from src.conexion import conexion_bd

def guardar_proveedor_bd(proveedor):
    """ Guarda un proveedor en la base de datos """
    Proveedor = dict(proveedor)
    
    try:
        conexion, cursor = conexion_bd()  # Obtener conexión y cursor
        if not conexion or not cursor:
            print("❌ No se pudo establecer conexión con la base de datos.")
            return {"RESPUESTA": False, "Mensaje": "No se pudo conectar a la base de datos"}

        columnas = tuple(Proveedor.keys())
        valores = tuple(Proveedor.values())

        consulta = """INSERT INTO tbl_proveedores {campos} VALUES(?,?,?,?,?)""".format(campos=columnas)

        cursor.execute(consulta, valores)

        conexion.commit()
        creado = cursor.rowcount > 0
        if creado:
            return {"RESPUESTA": True, "Mensaje": "Proveedor creado con éxito"}
        else:
            return {"RESPUESTA": False, "Mensaje": "Proveedor ¡NO! creado con éxito"}
    
    except Exception as ex:
        return {"RESPUESTA": False, "Mensaje": str(ex)}

def buscar_proveedor_bd(nit):
    """ Busca un proveedor en la base de datos por su NIT """
    try:
        conexion, cursor = conexion_bd()
        if not conexion or not cursor:
            print("❌ No se pudo establecer conexión con la base de datos.")
            return {"RESPUESTA": False, "Mensaje": "No se pudo conectar a la base de datos"}

        consulta = "SELECT * FROM tbl_proveedores WHERE nit = ?"
        cursor.execute(consulta, (nit,))
        proveedor = cursor.fetchone()

        if proveedor:
            return {"RESPUESTA": True, "Proveedor": proveedor}
        else:
            return {"RESPUESTA": False, "Mensaje": "Proveedor no encontrado"}

    except Exception as ex:
        return {"RESPUESTA": False, "Mensaje": str(ex)}

def eliminar_proveedor_bd(nit):
    """ Elimina un proveedor de la base de datos basado en su NIT """
    try:
        conexion, cursor = conexion_bd()  # Obtener conexión y cursor
        if not conexion or not cursor:
            print("❌ No se pudo establecer conexión con la base de datos.")
            return {"RESPUESTA": False, "Mensaje": "No se pudo conectar a la base de datos"}

        consulta = "DELETE FROM tbl_proveedores WHERE nit = ?"
        cursor.execute(consulta, (nit,))

        conexion.commit()
        eliminado = cursor.rowcount > 0
        if eliminado:
            return {"RESPUESTA": True, "Mensaje": "Proveedor eliminado con éxito"}
        else:
            return {"RESPUESTA": False, "Mensaje": "Proveedor no encontrado"}

    except Exception as ex:
        return {"RESPUESTA": False, "Mensaje": str(ex)}

def actualizar_proveedor_bd(proveedor_actualizado):
    """ Actualiza los datos de un proveedor en la base de datos """
    try:
        conexion, cursor = conexion_bd()  # Obtener conexión y cursor
        if not conexion or not cursor:
            print("❌ No se pudo establecer conexión con la base de datos.")
            return {"RESPUESTA": False, "Mensaje": "No se pudo conectar a la base de datos"}

        consulta = """UPDATE tbl_proveedores 
                      SET nombre_proveedor = ?, direccion_proveedor = ?, 
                          telefono_proveedor = ?, correo_proveedor = ?
                      WHERE nit = ?"""

        valores = (
            proveedor_actualizado["nombre_proveedor"],
            proveedor_actualizado["direccion_proveedor"],
            proveedor_actualizado["telefono_proveedor"],
            proveedor_actualizado["correo_proveedor"],
            proveedor_actualizado["nit"]
        )

        cursor.execute(consulta, valores)

        conexion.commit()
        actualizado = cursor.rowcount > 0
        if actualizado:
            return {"RESPUESTA": True, "Mensaje": "Proveedor actualizado con éxito"}
        else:
            return {"RESPUESTA": False, "Mensaje": "Proveedor no encontrado o sin cambios"}

    except Exception as ex:
        return {"RESPUESTA": False, "Mensaje": str(ex)}