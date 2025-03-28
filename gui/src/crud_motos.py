from src.conexion import conexion_bd

def guardar_moto_bd(moto):
    Moto = dict(moto)
    
    try:
        conexion, cursor = conexion_bd()  # Obtener conexión y cursor
        if not conexion or not cursor:
            print("❌ No se pudo establecer conexión con la base de datos.")
            return {"RESPUESTA": False, "Mensaje": "No se pudo conectar a la base de datos"}

        columnas = tuple(Moto.keys())
        valores = tuple(Moto.values())

        consulta = """INSERT INTO tbl_motos {campos} VALUES(?,?,?,?,?)""".format(campos=columnas)

        cursor.execute(consulta, valores)

        conexion.commit()
        creado = cursor.rowcount > 0
        if creado:
            return {"RESPUESTA": True, "Mensaje": "Moto registrada con éxito"}
        else:
            return {"RESPUESTA": False, "Mensaje": "Moto ¡NO! registrada con éxito"}
    
    except Exception as ex:
        return {"RESPUESTA": False, "Mensaje": str(ex)}

def buscar_moto_bd(ref_moto):
    try:
        conexion, cursor = conexion_bd()
        if not conexion or not cursor:
            print("❌ No se pudo establecer conexión con la base de datos.")
            return {"RESPUESTA": False, "Mensaje": "No se pudo conectar a la base de datos"}

        consulta = "SELECT * FROM tbl_motos WHERE ref_moto = ?"
        cursor.execute(consulta, (ref_moto,))
        moto = cursor.fetchone()

        if moto:
            return {"RESPUESTA": True, "Moto": moto}
        else:
            return {"RESPUESTA": False, "Mensaje": "Moto no encontrada"}

    except Exception as ex:
        return {"RESPUESTA": False, "Mensaje": str(ex)}

def eliminar_moto_bd(ref_moto):
    try:
        conexion, cursor = conexion_bd()  # Obtener conexión y cursor
        if not conexion or not cursor:
            print("❌ No se pudo establecer conexión con la base de datos.")
            return {"RESPUESTA": False, "Mensaje": "No se pudo conectar a la base de datos"}

        consulta = "DELETE FROM tbl_motos WHERE ref_moto = ?"
        cursor.execute(consulta, (ref_moto,))

        conexion.commit()
        eliminado = cursor.rowcount > 0
        if eliminado:
            return {"RESPUESTA": True, "Mensaje": "Moto eliminada con éxito"}
        else:
            return {"RESPUESTA": False, "Mensaje": "Moto no encontrada"}

    except Exception as ex:
        return {"RESPUESTA": False, "Mensaje": str(ex)}

def actualizar_moto_bd(moto_actualizada):
    try:
        conexion, cursor = conexion_bd()  # Obtener conexión y cursor
        if not conexion or not cursor:
            print("❌ No se pudo establecer conexión con la base de datos.")
            return {"RESPUESTA": False, "Mensaje": "No se pudo conectar a la base de datos"}

        consulta = """UPDATE tbl_motos 
                    SET modelo = ?, color = ?, 
                        precio = ?, cantidad_disponible = ?
                    WHERE ref_moto = ?"""

        valores = (
            moto_actualizada["modelo"],
            moto_actualizada["color"],
            moto_actualizada["precio"],
            moto_actualizada["cantidad_disponible"],
            moto_actualizada["ref_moto"]
        )

        cursor.execute(consulta, valores)

        conexion.commit()
        actualizado = cursor.rowcount > 0
        if actualizado:
            return {"RESPUESTA": True, "Mensaje": "Moto actualizada con éxito"}
        else:
            return {"RESPUESTA": False, "Mensaje": "Moto no encontrada o sin cambios"}

    except Exception as ex:
        return {"RESPUESTA": False, "Mensaje": str(ex)}
