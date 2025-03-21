# App-tienda-motos-la-33
Manejo de inventario y ventas

APP_TIENDA_MOTOS/
│── gui/
│   ├── main_window.py    # Interfaz principal con Tkinter
│   ├── componentes.py    # Widgets reutilizables
│── src/
│   ├── conexion.py       # Módulo de conexión a la BD
│   ├── consultas.py      # Funciones de consulta SQL
│   ├── creacion_tablas.py # Creación de la BD
│── db_tienda_motos_la33.db # Base de datos SQLite
│── main.py               # Archivo principal
│── README.md
│── LICENSE

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
