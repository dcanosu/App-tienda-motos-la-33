import sqlite3 as db

def consultar_empleados():
    conexion = db.connect("db_tienda_motos_la33.db")
    cursor = conexion.cursor()

    # Consulta de datos
    cursor.execute("SELECT * FROM tbl_empleados")
    empleados = cursor.fetchall()  # Obtener todos los registros

    conexion.close()

    # Mostrar los resultados
    if empleados:
        for empleado in empleados:
            print(empleado)
    else:
        print("No hay empleados registradas.")

# Ejecutar la consulta
consultar_empleados()


"""
1️⃣ fetchall() → Obtener todos los resultados
📌 Este método devuelve todas las filas de la consulta en una lista de tuplas.
Cuándo usarlo: Cuando necesitas recuperar todos los registros de una tabla.

cursor.execute("SELECT * FROM ventas")
ventas = cursor.fetchall()  # Obtiene TODAS las filas

for venta in ventas:
    print(venta)


2️⃣ fetchone() → Obtener una sola fila
📌 Devuelve solo la primera fila de la consulta como una tupla.
Cuándo usarlo: Cuando solo esperas un resultado o solo necesitas uno.

cursor.execute("SELECT * FROM ventas")
venta = cursor.fetchone()  # Obtiene SOLO la primera fila
print(venta)


3️⃣ fetchmany(n) → Obtener n filas
📌 Devuelve una lista con hasta n filas de la consulta.
Cuándo usarlo: Cuando quieres limitar la cantidad de resultados.

cursor.execute("SELECT * FROM ventas")
ventas = cursor.fetchmany(2)  # Obtiene máximo 2 filas

for venta in ventas:
    print(venta)

"""