from tkinter import Label, Tk, Toplevel, Button
from PIL import Image, ImageTk
from src.formulario_clientes import formulario_gestion_clientes
from src.formulario_empleados import formulario_gestion_empleados
from src.formulario_motos import formulario_gestion_motos
from src.formulario_proveedor import formulario_gestion_proveedor
from src.formulario_facturacion import formulario_gestion_venta

# Configuración general estilos
fuente = ("Verdana", 20, "bold")
fuente_titulos = ("Copperplate", 40, "bold")
fuente_botones = ("Verdana", 16, "bold")
color_fondo = "#CC0000"

# Construir la ventana principal
ventana = Tk()
ventana.state("zoomed") # Crear ventana full screen
ventana.title("TIENDA DE MOTOS LA 33")
ventana.resizable(True, True)
ventana.configure(background="#FFFFFF")

Label(bg=color_fondo, width="550", height="6").pack()
#Label(text="Tienda de motos la 33", font=fuente_titulos, bg="#e31010", fg="white", width="550", height="3").pack()
Label(text="Tienda de motos la 33", font=fuente_titulos, bg=color_fondo, fg="white").place(x=500,y=20)
#label_fuente = ("Verdana", 14, "bold")
Label(ventana, text="Menú principal", justify="center", font=fuente, foreground="white",background=color_fondo).place(x=115,y=45)

# Abrir la imagen
imagen_pil = Image.open("gui/iconos/main.jpg")

# Redimensionar la imagen (ajusta el tamaño según lo que necesites)
nuevo_ancho = 1920
nuevo_alto = 1080
imagen_pil = imagen_pil.resize((nuevo_ancho, nuevo_alto), Image.LANCZOS)  # Usar LANCZOS para mejor calidad

# Convertir a formato Tkinter
imagen_tk = ImageTk.PhotoImage(imagen_pil)

# Crear y mostrar el Label con la imagen
label = Label(ventana, image=imagen_tk)
label.image = imagen_tk  # Evita que Python la elimine por el recolector de basura
label.pack()

def cargar_imagen(ruta, ancho, alto):
    imagen_pil = Image.open(ruta).resize((ancho, alto), Image.LANCZOS)
    return ImageTk.PhotoImage(imagen_pil)

def crear_ventana(titulo):
    """Crea una ventana secundaria con el mismo diseño base."""
    nueva_ventana = Toplevel(ventana)
    nueva_ventana.after(10, lambda: nueva_ventana.state("zoomed"))
    nueva_ventana.title(titulo)
    nueva_ventana.configure(background="#FFFFFF")

    # Encabezado
    Label(nueva_ventana,bg=color_fondo, width="550", height="6").pack()
    Label(nueva_ventana, text="Tienda de motos la 33", font=fuente_titulos, bg=color_fondo, fg="white").place(x=550,y=20)
    Label(nueva_ventana, text=titulo, justify="center", font=fuente, foreground="white",background=color_fondo).place(x=115,y=45)
    
    return nueva_ventana

def ventana_gestion_clientes():
    nueva_ventana = crear_ventana("Gestión de clientes")
    imagen_gestion = cargar_imagen("gui/iconos/gestion_clientes.jpg",700,600)
    
    # Mostrar la imagen en la ventana
    label_img = Label(nueva_ventana, image=imagen_gestion)
    label_img.image = imagen_gestion  # Mantener referencia
    #label_img.pack()
    label_img.place(x=30, y=150)

    formulario_gestion_clientes(nueva_ventana)
    nueva_ventana.after(10, lambda: nueva_ventana.state("zoomed"))
    boton_formulario = Button(nueva_ventana, text="Información de Clientes", font=("Verdana", "25", "bold"),bg="white", fg="#002060",width="30")
    boton_formulario.place(x=800, y=150)

def ventana_gestion_proveedor():
    nueva_ventana = crear_ventana("Gestión de proveedores") 
    imagen_gestion = cargar_imagen("gui/iconos/proveedores2.jpg",700,600)
    
    # Mostrar la imagen en la ventana
    label_img = Label(nueva_ventana, image=imagen_gestion)
    label_img.image = imagen_gestion  # Mantener referencia
    #label_img.pack()
    label_img.place(x=30, y=150)
    
    formulario_gestion_proveedor(nueva_ventana)
    nueva_ventana.after(10, lambda: nueva_ventana.state("zoomed"))
    boton_formulario = Button(nueva_ventana, text="Información de Proveedores", font=("Verdana", "25", "bold"),bg="white", fg="#002060",width="30")
    boton_formulario.place(x=800, y=150)
    
def ventana_gestion_empleados():
    nueva_ventana = crear_ventana("Gestión de empleados")
    imagen_gestion = cargar_imagen("gui/iconos/empleados.jpg",700,600)
    
    # Mostrar la imagen en la ventana
    label_img = Label(nueva_ventana, image=imagen_gestion)
    label_img.image = imagen_gestion  # Mantener referencia
    #label_img.pack()
    label_img.place(x=30, y=150)
    
    formulario_gestion_empleados(nueva_ventana)
    nueva_ventana.after(10, lambda: nueva_ventana.state("zoomed"))
    boton_formulario = Button(nueva_ventana, text="Información de Empleados", font=("Verdana", "25", "bold"),bg="white", fg="#002060",width="30")
    boton_formulario.place(x=800, y=150)

def ventana_gestion_motos():
    nueva_ventana = crear_ventana("Gestión de motos")
    imagen_gestion = cargar_imagen("gui/iconos/gestion_motos.jpg",700,600)
    
    # Mostrar la imagen en la ventana
    label_img = Label(nueva_ventana, image=imagen_gestion)
    label_img.image = imagen_gestion  # Mantener referencia
    #label_img.pack()
    label_img.place(x=30, y=150)
    
    formulario_gestion_motos(nueva_ventana)
    nueva_ventana.after(10, lambda: nueva_ventana.state("zoomed"))
    boton_formulario = Button(nueva_ventana, text="Información de Motos", font=("Verdana", "25", "bold"),bg="white", fg="#002060",width="30")
    boton_formulario.place(x=800, y=150)

def ventana_facturacion():
    nueva_ventana = crear_ventana("Facturación")
    imagen_gestion = cargar_imagen("gui/iconos/facturacion.jpg",700,600)
    
    # Mostrar la imagen en la ventana
    label_img = Label(nueva_ventana, image=imagen_gestion)
    label_img.image = imagen_gestion  # Mantener referencia
    #label_img.pack()
    label_img.place(x=30, y=150)
    
    formulario_gestion_venta(nueva_ventana)
    nueva_ventana.after(10, lambda: nueva_ventana.state("zoomed"))
    boton_formulario = Button(nueva_ventana, text="Información de Ventas", font=("Verdana", "25", "bold"),bg="white", fg="#002060",width="30")
    boton_formulario.place(x=800, y=150)

# Versión violenta
"""# Botón para abrir la ventana de registro de clientes
boton_registro = Button(ventana, text="Gestión de clientes", font=fuente_botones,bg="white", fg="#002060",width="15",command=ventana_gestion_clientes)
boton_registro.place(x=100, y=80)

# Botón para abrir la ventana de registro de clientes
boton_registro = Button(ventana, text="Gesitón de proveedores", font=fuente_botones,bg="white", fg="#002060",width="18",command=ventana_gestion_proveedor)
boton_registro.place(x=340, y=80)

# Botón para abrir la ventana de registro de clientes
boton_registro = Button(ventana, text="Gestion de empleados", font=fuente_botones,bg="white", fg="#002060",width="17",command=ventana_gestion_empleados)
boton_registro.place(x=600, y=80)

# Botón para abrir la ventana de motos
boton_registro = Button(ventana, text="Gestión de motos", font=fuente_botones,bg="white", fg="#002060",width="15",command=ventana_gestion_motos)
boton_registro.place(x=860, y=80)

# Botón para abrir las facturas
boton_registro = Button(ventana, text="Facturación", font=fuente_botones,bg="white", fg="#002060",width="15",command=ventana_facturacion)
boton_registro.place(x=1100, y=80)"""

# Versión optimizada
botones = [
    ("Gestión de clientes", ventana_gestion_clientes, "15", 100),
    ("Gestión de proveedores", ventana_gestion_proveedor, "18", 340),
    ("Gestión de empleados", ventana_gestion_empleados, "17", 600),
    ("Gestión de motos", ventana_gestion_motos, "15", 860),
    ("Facturación", ventana_facturacion, "15", 1100),
]
for texto, comando, ancho, eje_x in botones:
    Button(ventana, text=texto, font=fuente_botones, bg="white",fg="#002060", width=ancho, command=comando).place(x=eje_x,y=80)

# Siempre siempre tiene que ir al final del código de la ventana
ventana.mainloop()