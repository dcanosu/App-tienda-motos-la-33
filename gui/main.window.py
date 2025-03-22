from tkinter import Label, Tk, Toplevel, Button
from PIL import Image, ImageTk

# Construir la ventana principal
ventana = Tk()
ventana.state("zoomed") # Crear ventana full screen
ventana.title("TIENDA DE MOTOS LA 33")
ventana.resizable(True, True)
ventana.configure(background="#FFFFFF")

########################### GUI #########################
fuente = ("Verdana", 20, "bold")
fuente_titulos = ("Verdana", 25, "bold")
fuente_botones = ("Verdana", 16, "bold")
color_fondo = "#CC0000"

Label(bg=color_fondo, width="550", height="6").pack()
#Label(text="Tienda de motos la 33", font=fuente_titulos, bg="#e31010", fg="white", width="550", height="3").pack()
Label(text="Tienda de motos la 33", font=fuente_titulos, bg=color_fondo, fg="white").place(x=550,y=20)
#label_fuente = ("Verdana", 14, "bold")
Label(ventana, text="Menú principal", justify="center", font=fuente, foreground="white",background=color_fondo).place(x=115,y=45)

# Abrir la imagen
imagen_pil = Image.open("gui/iconos/AfricaTwin-4.jpg")

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

def crear_ventana(titulo):
    """Crea una ventana secundaria con el mismo diseño base."""
    nueva_ventana = Toplevel(ventana)
    #nueva_ventana.state("zoomed")  # Full screen
    nueva_ventana.after(10, lambda: nueva_ventana.state("zoomed"))
    nueva_ventana.title(titulo)
    nueva_ventana.configure(background="#FFFFFF")

    # Encabezado
    Label(nueva_ventana,bg=color_fondo, width="550", height="6").pack()
    Label(nueva_ventana, text="Tienda de motos la 33", font=fuente_titulos, bg=color_fondo, fg="white").place(x=550,y=20)
    Label(nueva_ventana, text=titulo, justify="center", font=fuente, foreground="white",background=color_fondo).place(x=115,y=45)
    
    return nueva_ventana

def ventana_gestion_clientes():
    """Abre la ventana de registro de clientes con el diseño predefinido."""
    crear_ventana("Gestión de clientes")

def ventana_gestion_proveedor():
    """Abre la ventana de registro de clientes con el diseño predefinido."""
    crear_ventana("Gestión de proveedores")
    
def ventana_gestion_empleados():
    """Abre la ventana de registro de clientes con el diseño predefinido."""
    crear_ventana("Gestión de empleados")

def ventana_gestion_motos():
    """Abre la ventana de registro de clientes con el diseño predefinido."""
    crear_ventana("Gestión de motos")

def ventana_facturacion():
    """Abre la ventana de registro de clientes con el diseño predefinido."""
    crear_ventana("Facturación")

# Veriión violenta
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
    ("Gestión de proveedores", ventana_gestion_clientes, "18", 340),
    ("Gestión de empleados", ventana_gestion_clientes, "17", 600),
    ("Gestión de motos", ventana_gestion_clientes, "15", 860),
    ("Facturación", ventana_gestion_clientes, "15", 1100),
]
for texto, comando, ancho, eje_x in botones:
    Button(ventana, text=texto, font=fuente_botones, bg="white",fg="#002060", width=ancho, command=comando).place(x=eje_x,y=80)

"""
Label(ventana, text="DNI: ", justify="center", font=label_fuente, foreground="#002060",bg="white").place(x=100,y=130)
Label(ventana, text="Nombre: ", justify="left", font=label_fuente, foreground="#002060",background="#FFFFFF").place(x=100,y=160)
Label(ventana, text="Apellido: ", justify="center", font=label_fuente, foreground="#002060",background="#FFFFFF").place(x=100,y=190)
Label(ventana, text="Correo: ", justify="center", font=label_fuente, foreground="#002060",background="#FFFFFF").place(x=100,y=220)
Label(ventana, text="Celular: ", justify="center", font=label_fuente, foreground="#002060",background="#FFFFFF").place(x=100,y=250)
Label(ventana, text="Genero: ", justify="center", font=label_fuente, foreground="#002060",background="#FFFFFF").place(x=100,y=280)
#Label(ventana, text="Id_producto: ", justify="center", font="label_fuente, foreground="#002060",background="#FFFFFF").place(x=1000,y=100)

########################### INPUT #########################
# Son los campos donde el usuario ingresa el text
#id_cliente = StringVar()
dni_cliente = StringVar()
nombre_cliente = StringVar()
apellido_cliente = StringVar()
email_cliente = StringVar()
movil_cliente = StringVar()
genero_cliente = StringVar()
opciones_genero = ["Masculino", "Femenino", "No binario", "Transgénero", "Género fluido", "Agénero", "Otro"]


### Contrucción de las cajas ###
#e_id_cliente = ttk.Entry(textvariable=dni_cliente, width=25)
#e_id_cliente.place(x=300, y=130)

e_dni_cliente = ttk.Entry(textvariable=dni_cliente, width=25)
e_dni_cliente.place(x=300, y=130)

e_nombre_cliente = ttk.Entry(textvariable=nombre_cliente, width=25)
e_nombre_cliente.place(x=300, y=160)

e_apellido_cliente = ttk.Entry(textvariable=apellido_cliente, show="*",width=25)
e_apellido_cliente.place(x=300, y=190)

e_email_cliente = ttk.Entry(textvariable=email_cliente, width=35)
e_email_cliente.place(x=300, y=220)

e_movil_cliente = ttk.Entry(textvariable=movil_cliente, width=15)
e_movil_cliente.place(x=300, y=250)

e_genero_cliente = ttk.Combobox(textvariable=genero_cliente, foreground="white",values=opciones_genero, width=15)
e_genero_cliente.place(x=300, y=280)
#e_genero_cliente.current(0)"""



"""### Iconos###
icono_guardar = PhotoImage(file="iconos/ICONOP.png").subsample(2)
#icono_guardar = icono_guardar.subsample(2)
boton_guardar = Button(ventana, image=icono_guardar, command=agregar, bd=0, highlightthickness=5)
boton_guardar.place(x=300, y=350)

icono_eliminar = PhotoImage(file="iconos/eliminar.png").subsample(14)
boton_eliminar = Button(ventana, text="Eliminar",image=icono_eliminar, command=eliminar)
boton_eliminar.place(x=350, y=350)"""

# Siempre siempre tiene que ir al final del código de la ventana
ventana.mainloop()