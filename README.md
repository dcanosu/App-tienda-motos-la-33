# App Tienda de Motos la 33
Este es un proyecto de interfaz gráfica desarrollado en Python utilizando Tkinter. La aplicación gestiona la visualización de información sobre una tienda de motos.

## Características
- **Interfaz gráfica con Tkinter**
- **Ventana principal con menú**
- **Manejo de ventanas secundarias**
- **Logo y pie de página en todas las ventanas**

## Requisitos
Asegúrate de tener instaladas las siguientes dependencias antes de ejecutar el proyecto:

```sh
pip install pillow
```

## Estructura del Proyecto
```
📂 tienda_motos
├── LICENSE
├── README.md
├── bd_tienda_motos-Entidad relacion ER.V1.jpg
├── bd_tienda_motos-MER.jpg
├── db_tienda_motos_la33.db
├── db_tienda_motos_la33.db.png
├── gui
│   ├── iconos
│   │   ├── ADV_GRIS.jpg
│   │   ├── actualizar.png
│   │   ├── buscar.png
│   │   ├── eliminar.png
│   │   ├── empleados.jpg
│   │   ├── facturacion.jpg
│   │   ├── gestion_clientes.jpg
│   │   ├── gestion_motos.jpg
│   │   ├── guardar.png
│   │   ├── logo.jpg
│   │   ├── main.jpg
│   │   ├── main2.jpg
│   │   ├── new-background-motos-honda.jpg
│   │   ├── proveedor.jpg
│   │   └── proveedores2.jpg
│   ├── main_window.py
│   └── src
│       ├── __init__.py
│       ├── conexion.py # Módulo de conexión a la BD
│       ├── consultas.py
│       ├── creacion_tablas.py
│       ├── crud_clientes.py
│       ├── crud_empleados.py
│       ├── crud_facturacion.py
│       ├── crud_motos.py
│       ├── crud_proveedores.py
│       ├── formulario_clientes.py
│       ├── formulario_empleados.py
│       ├── formulario_facturacion.py
│       ├── formulario_motos.py
│       └── formulario_proveedor.py
├── image.png
└── main.py
 
```

## Instalación y Ejecución
1. Clona el repositorio:

```sh
git clone https://github.com/dcanosu/App-tienda-motos-la-33.git
```

2. Accede al directorio del proyecto:
```sh
cd tienda-motos
```

3. Ejecuta la aplicación:
```sh
python gui/src/main_window.py
```

## Uso
- Al ejecutar la aplicación, se abrirá la ventana principal con el logo y el menú.
- Puedes navegar entre las diferentes secciones de la aplicación.
- En todas las ventanas, se mostrará el logo y el pie de página con la información de derechos reservados.

## Capturas de Pantalla
- **Menú principal**
![alt text](image.png)

## Autor
Desarrollado por Daniel Cano Suarez y Mateo Agudelo Restrepo.

## Licencia
Este proyecto está bajo la licencia Apache-2.0 license.
