from tkinter import PhotoImage, StringVar, Label, Entry, OptionMenu, Button, messagebox, simpledialog
from src.crud_empleados import guardar_empleado_bd, eliminar_empleado_bd, actualizar_empleado_bd, buscar_empleado_bd

label_fuente = "Verdana", 25, "bold"
entry_fuente = "Verdana, 20"

def formulario_gestion_empleados(ventana):
    # Variables de entrada
    id_empleado = StringVar()
    tipo_documento_empleado = StringVar()
    opciones_tipo_documento = ["Cédula de ciudadanía", "Cédula de extranjería", "Pasaporte", "Permiso Especial de Permanencia"]
    numero_documento_empleado = StringVar()
    nombre_empleado = StringVar()
    apellido_empleado = StringVar()
    cargo_empleado = StringVar()
    opciones_tipo_cargo = ["Coordinador", "Auxiliar", "Vendedor", "Cajero"]
    direccion_empleado = StringVar()
    telefono_empleado = StringVar()
    correo_empleado = StringVar()

    # Creación de los labels para solicitar la información
    Label(ventana, text="ID Empleado:", font=label_fuente, fg="#002060", bg="white").place(x=800, y=250)
    Label(ventana, text="Tipo de Documento:", font=label_fuente, fg="#002060", bg="white").place(x=800, y=300)
    Label(ventana, text="N° documento:", font=label_fuente, fg="#002060", bg="white").place(x=800, y=350)
    Label(ventana, text="Nombre:", font=label_fuente, fg="#002060", bg="white").place(x=800, y=400)
    Label(ventana, text="Apellido:", font=label_fuente, fg="#002060", bg="white").place(x=800, y=450)
    Label(ventana, text="Cargo:", font=label_fuente, fg="#002060", bg="white").place(x=800, y=500)
    Label(ventana, text="Dirección:", font=label_fuente, fg="#002060", bg="white").place(x=800, y=550)
    Label(ventana, text="Teléfono:", font=label_fuente, fg="#002060", bg="white").place(x=800, y=600)
    Label(ventana, text="Correo:", font=label_fuente, fg="#002060", bg="white").place(x=800, y=650)

    color_bg = "white"
    color_fg = "black"
    # Construcción de las cajas
    Entry(ventana, textvariable=id_empleado, font=entry_fuente, background=color_bg, foreground=color_fg).place(x=1015, y=250)
    tipo_documento_empleado.set(opciones_tipo_documento[0])  # Valor por defecto
    OptionMenu(ventana, tipo_documento_empleado, *opciones_tipo_documento).place(x=1100, y=310)
    Entry(ventana, textvariable=numero_documento_empleado, font=entry_fuente,background=color_bg, foreground=color_fg,).place(x=1015, y=350)
    Entry(ventana, textvariable=nombre_empleado, font=entry_fuente,background=color_bg, foreground=color_fg,).place(x=1015, y=400)
    Entry(ventana, textvariable=apellido_empleado, font=entry_fuente, background=color_bg, foreground=color_fg).place(x=1015, y=450)
    cargo_empleado.set(opciones_tipo_cargo[0])  # Valor por defecto
    OptionMenu(ventana, cargo_empleado, *opciones_tipo_cargo).place(x=1100, y=510)
    Entry(ventana, textvariable=direccion_empleado, font=entry_fuente, background=color_bg, foreground=color_fg).place(x=1015, y=550)
    Entry(ventana, textvariable=telefono_empleado, font=entry_fuente, background=color_bg, foreground=color_fg).place(x=1015, y=600)
    Entry(ventana, textvariable=correo_empleado, font=entry_fuente, background=color_bg, foreground=color_fg).place(x=1015, y=650)

    icono_guardar = PhotoImage(file="gui/iconos/guardar.png").subsample(4)
    boton_guardar = Button(ventana, image=icono_guardar, command=lambda: guardar_empleado_formulario(tipo_documento_empleado, numero_documento_empleado,nombre_empleado, apellido_empleado, cargo_empleado, direccion_empleado,telefono_empleado, correo_empleado))
    boton_guardar.image = icono_guardar  # Mantener referencia
    boton_guardar.place(x=900, y=720)
    
    icono_buscar = PhotoImage(file="gui/iconos/buscar.png").subsample(4)
    boton_buscar = Button(ventana, image=icono_buscar, command=lambda: buscar_empleado_formulario(id_empleado, tipo_documento_empleado, numero_documento_empleado, nombre_empleado, apellido_empleado, cargo_empleado, direccion_empleado, telefono_empleado, correo_empleado))
    boton_buscar.image = icono_buscar  # Mantener referencia
    boton_buscar.place(x=990, y=720)
    
    icono_eliminar = PhotoImage(file="gui/iconos/eliminar.png").subsample(4)
    boton_eliminar = Button(ventana, image=icono_eliminar, command=lambda: eliminar_empleado_formulario(numero_documento_empleado))
    boton_eliminar.image = icono_eliminar  # Mantener referencia
    boton_eliminar.place(x=1090, y=720)
    
    icono_actulizar = PhotoImage(file="gui/iconos/actualizar.png").subsample(4)
    boton_actulizar = Button(ventana, image=icono_actulizar, command=lambda: actualizar_empleado_formulario(tipo_documento_empleado, numero_documento_empleado, nombre_empleado, apellido_empleado, cargo_empleado, direccion_empleado, telefono_empleado, correo_empleado))
    boton_actulizar.image = icono_actulizar  # Mantener referencia
    boton_actulizar.place(x=1190, y=720)

    # Retornar variables para su uso posterior si es necesario
    return {
        "tipo_documento_empleado": tipo_documento_empleado,
        "numero_documento_empleado": numero_documento_empleado,
        "nombre_empleado": nombre_empleado,
        "apellido_empleado": apellido_empleado,
        "direccion_empleado": direccion_empleado,
        "telefono_empleado": telefono_empleado,
        "correo_empleado": correo_empleado
    }

def guardar_empleado_formulario(tipo_documento_empleado, numero_documento_empleado, nombre_empleado, apellido_empleado, cargo_empleado, direccion_empleado, telefono_empleado, correo_empleado):
    if tipo_documento_empleado.get() and numero_documento_empleado.get() and nombre_empleado.get() and apellido_empleado.get() and cargo_empleado.get() and correo_empleado.get():
        cliente = {
            "tipo_documento_empleado": tipo_documento_empleado.get(),
            "numero_documento_empleado": numero_documento_empleado.get(),
            "nombre_empleado": nombre_empleado.get(),
            "apellido_empleado": apellido_empleado.get(),
            "cargo_empleado":cargo_empleado.get(),
            "direccion_empleado": direccion_empleado.get(),
            "telefono_empleado": telefono_empleado.get(),
            "correo_empleado": correo_empleado.get(),
        }

        print("✅ Cliente agregado con éxito:", cliente)
        respuesta = guardar_empleado_bd(cliente)
        messagebox.showinfo("✅ Registro de Cliente", respuesta)

    else:
        messagebox.showwarning("Error", "⚠️ Todos los campos obligatorios deben estar llenos.")

def eliminar_empleado_formulario(numero_documento_empleado):
    """ Elimina un cliente de la base de datos basado en su número de documento """
    if numero_documento_empleado.get():
        respuesta = eliminar_empleado_bd(numero_documento_empleado.get())
        messagebox.showinfo("Eliminar Cliente", respuesta)
    else:
        messagebox.showwarning("Error", "⚠️ Debes ingresar un número de documento para eliminar un cliente.")

def actualizar_empleado_formulario(tipo_documento_empleado, numero_documento_empleado, nombre_empleado, apellido_empleado, cargo_empleado, direccion_empleado, telefono_empleado, correo_empleado):
    """ Actualiza los datos de un cliente existente en la base de datos """
    if tipo_documento_empleado.get() and numero_documento_empleado.get() and nombre_empleado.get() and apellido_empleado.get() and cargo_empleado.get() and correo_empleado.get():
        cliente_actualizado = {
            "tipo_documento_empleado": tipo_documento_empleado.get(),
            "numero_documento_empleado": numero_documento_empleado.get(),
            "nombre_empleado": nombre_empleado.get(),
            "apellido_empleado": apellido_empleado.get(),
            "cargo_empleado":cargo_empleado.get(),
            "direccion_empleado": direccion_empleado.get(),
            "telefono_empleado": telefono_empleado.get(),
            "correo_empleado": correo_empleado.get(),
        }

        print("Cliente actualizado con éxito:", cliente_actualizado)
        respuesta = actualizar_empleado_bd(cliente_actualizado)
        messagebox.showinfo("Actualizar Cliente", respuesta)
    
    else:
        messagebox.showwarning("Error", "⚠️ Todos los campos obligatorios deben estar llenos.")

def buscar_empleado_formulario(id_empleado, tipo_documento_empleado, numero_documento_empleado, nombre_empleado, apellido_empleado, cargo_empleado, direccion_empleado, telefono_empleado, correo_empleado):
    """ Busca un cliente y llena los campos de entrada con sus datos """
    numero_documento = simpledialog.askstring("Buscar Empleado", "Ingrese el número de documento:")
    
    if numero_documento:
        resultado = buscar_empleado_bd(numero_documento)
        
        if resultado["RESPUESTA"]:
            empleado = resultado["Empleado"]
            #print("Datos obtenidos:", empleado)  # Para verificar los datos obtenidos
            # Llenar los campos con la información del cliente
            id_empleado.set(empleado[0])
            tipo_documento_empleado.set(empleado[1])  # Tipo de documento
            numero_documento_empleado.set(empleado[2])  # Número de documento
            nombre_empleado.set(empleado[3])  # Nombre
            apellido_empleado.set(empleado[4])  # Apellido
            cargo_empleado.set(empleado[5])     # Cargo
            direccion_empleado.set(empleado[6])  # Dirección
            telefono_empleado.set(empleado[7])  # Teléfono
            correo_empleado.set(empleado[8])  # Correo
        else:
            messagebox.showwarning("No Encontrado", resultado["Mensaje"])
    else:
        messagebox.showwarning("Cancelado", "Búsqueda cancelada por el usuario")


