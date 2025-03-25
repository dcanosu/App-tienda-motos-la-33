import time
from gui.src.creacion_tablas import crear_tablas, crear_tablas_relacionales

if __name__ == "__main__":
    crear_tablas()
    time.sleep(5) # Espera para evitar sobrecargar la BD
    crear_tablas_relacionales()