from src.conexion import conexion_bd

def guardar_cliente_bd(client):
    Cliente = dict(client)
    
    try:
        conexion, cursor = conexion_bd()  # Obtener conexion y cursor
        if not conexion or not cursor:
            print("❌ No se pudo establecer conexión con la base de datos.")
            return

        columnas = tuple(Cliente.keys())
        valores = tuple(Cliente.values())

        consulta = """INSERT INTO tbl_clientes {campos} VALUES(?,?,?,?,?,?,?)""".format(campos=columnas)
        cursor.execute(consulta,valores)
        conexion.commit()
        creado = cursor.rowcount>0
        if creado:
            return {"RESPUESTA": True,"Mensaje": "Cliente creado con éxito"}
        else:
            return{"RESPUESTA": False,"Mensaje": "Cliente !NO! creado con éxito"}
    
    except Exception as ex:
        return{"RESPUESTA": False,"Mensaje":str(ex)}

def buscar_cliente_bd(numero_documento):
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

def eliminar_cliente_bd(numero_documento):
    try:
        conexion, cursor = conexion_bd()  # Obtener conexión y cursor
        if not conexion or not cursor:
            print("❌ No se pudo establecer conexión con la base de datos.")
            return {"RESPUESTA": False, "Mensaje": "No se pudo conectar a la base de datos"}

        consulta = "DELETE FROM tbl_clientes WHERE numero_documento_cliente = ?"
        cursor.execute(consulta, (numero_documento,))

        conexion.commit()
        eliminado = cursor.rowcount > 0
        if eliminado:
            return {"RESPUESTA": True, "Mensaje": "Cliente eliminado con éxito"}
        else:
            return {"RESPUESTA": False, "Mensaje": "Cliente no encontrado"}

    except Exception as ex:
        return {"RESPUESTA": False, "Mensaje": str(ex)}

def actualizar_cliente_bd(cliente_actualizado):
    try:
        conexion, cursor = conexion_bd()  # Obtener conexión y cursor
        if not conexion or not cursor:
            print("❌ No se pudo establecer conexión con la base de datos.")
            return {"RESPUESTA": False, "Mensaje": "No se pudo conectar a la base de datos"}

        consulta = """UPDATE tbl_clientes 
                    SET tipo_documento_cliente = ?, nombre_cliente = ?, apellido_cliente = ?, 
                        direccion_cliente = ?, telefono_cliente = ?, correo_cliente = ?
                    WHERE numero_documento_cliente = ?"""

        valores = (
            cliente_actualizado["tipo_documento_cliente"],
            cliente_actualizado["nombre_cliente"],
            cliente_actualizado["apellido_cliente"],
            cliente_actualizado["direccion_cliente"],
            cliente_actualizado["telefono_cliente"],
            cliente_actualizado["correo_cliente"],
            cliente_actualizado["numero_documento_cliente"]
        )

        cursor.execute(consulta, valores)

        conexion.commit()
        actualizado = cursor.rowcount > 0
        if actualizado:
            return {"RESPUESTA": True, "Mensaje": "Cliente actualizado con éxito"}
        else:
            return {"RESPUESTA": False, "Mensaje": "Cliente no encontrado o sin cambios"}

    except Exception as ex:
        return {"RESPUESTA": False, "Mensaje": str(ex)}