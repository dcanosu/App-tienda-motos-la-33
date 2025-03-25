from tkinter import PhotoImage, StringVar, Label, Entry, OptionMenu, Button, messagebox, simpledialog
from src.crud_clientes import guardar_cliente_bd, eliminar_cliente_bd, actualizar_cliente_bd, buscar_cliente_bd

label_fuente = "Verdana", 25, "bold"
entry_fuente = "Verdana, 20"

def formulario_gestion_clientes(ventana):
    # Variables de entrada
    id_cliente = StringVar()
    tipo_documento_cliente = StringVar()
    opciones_tipo_documento = ["Cédula de ciudadanía", "Cédula de extranjería", "Pasaporte", "Permiso Especial de Permanencia"]
    numero_documento_cliente = StringVar()
    nombre_cliente = StringVar()
    apellido_cliente = StringVar()
    direccion_cliente = StringVar()
    telefono_cliente = StringVar()
    correo_cliente = StringVar()

    # Creación de los labels para solicitar la información
    Label(ventana, text="ID Cliente:", font=label_fuente, fg="#002060", bg="white").place(x=800, y=250)
    Label(ventana, text="Tipo de Documento:", font=label_fuente, fg="#002060", bg="white").place(x=800, y=300)
    Label(ventana, text="N° documento:", font=label_fuente, fg="#002060", bg="white").place(x=800, y=350)
    Label(ventana, text="Nombre:", font=label_fuente, fg="#002060", bg="white").place(x=800, y=400)
    Label(ventana, text="Apellido:", font=label_fuente, fg="#002060", bg="white").place(x=800, y=450)
    Label(ventana, text="Dirección:", font=label_fuente, fg="#002060", bg="white").place(x=800, y=500)
    Label(ventana, text="Teléfono:", font=label_fuente, fg="#002060", bg="white").place(x=800, y=550)
    Label(ventana, text="Correo:", font=label_fuente, fg="#002060", bg="white").place(x=800, y=600)

    color_bg = "white"
    color_fg = "black"
    # Construcción de las cajas
    Entry(ventana, textvariable=id_cliente, font=entry_fuente, background=color_bg, foreground=color_fg).place(x=1015, y=250)
    tipo_documento_cliente.set(opciones_tipo_documento[0])  # Valor por defecto
    OptionMenu(ventana, tipo_documento_cliente, *opciones_tipo_documento).place(x=1100, y=310)
    Entry(ventana, textvariable=numero_documento_cliente, font=entry_fuente,background=color_bg, foreground=color_fg,).place(x=1015, y=350)
    Entry(ventana, textvariable=nombre_cliente, font=entry_fuente,background=color_bg, foreground=color_fg,).place(x=1015, y=400)
    Entry(ventana, textvariable=apellido_cliente, font=entry_fuente, background=color_bg, foreground=color_fg).place(x=1015, y=450)
    Entry(ventana, textvariable=direccion_cliente, font=entry_fuente, background=color_bg, foreground=color_fg).place(x=1015, y=500)
    Entry(ventana, textvariable=telefono_cliente, font=entry_fuente, background=color_bg, foreground=color_fg).place(x=1015, y=550)
    Entry(ventana, textvariable=correo_cliente, font=entry_fuente, background=color_bg, foreground=color_fg).place(x=1015, y=600)

    icono_guardar = PhotoImage(file="gui/iconos/guardar.png").subsample(4)
    boton_guardar = Button(ventana, image=icono_guardar, command=lambda: guardar_cliente_formulario(tipo_documento_cliente, numero_documento_cliente,nombre_cliente, apellido_cliente, direccion_cliente,telefono_cliente, correo_cliente)) # falta command="")
    boton_guardar.image = icono_guardar  # Mantener referencia
    boton_guardar.place(x=900, y=670)
    
    icono_buscar = PhotoImage(file="gui/iconos/buscar.png").subsample(4)
    boton_buscar = Button(ventana, image=icono_buscar, command=buscar_cliente_formulario)  # falta command="")
    boton_buscar.image = icono_buscar  # Mantener referencia
    boton_buscar.place(x=990, y=670)
    
    icono_eliminar = PhotoImage(file="gui/iconos/eliminar.png").subsample(4)
    boton_eliminar = Button(ventana, image=icono_eliminar, command=lambda: eliminar_cliente_formulario(numero_documento_cliente))  # falta command="")
    boton_eliminar.image = icono_eliminar  # Mantener referencia
    boton_eliminar.place(x=1090, y=670)
    
    icono_actulizar = PhotoImage(file="gui/iconos/actualizar.png").subsample(4)
    boton_actulizar = Button(ventana, image=icono_actulizar, command=lambda: actualizar_cliente_formulario(tipo_documento_cliente, numero_documento_cliente, nombre_cliente, apellido_cliente,direccion_cliente, telefono_cliente, correo_cliente))  # falta command="")
    boton_actulizar.image = icono_actulizar  # Mantener referencia
    boton_actulizar.place(x=1190, y=670)

    # Retornar variables para su uso posterior si es necesario
    return {
        "tipo_documento_cliente": tipo_documento_cliente,
        "numero_documento_cliente": numero_documento_cliente,
        "nombre_cliente": nombre_cliente,
        "apellido_cliente": apellido_cliente,
        "direccion_cliente": direccion_cliente,
        "telefono_cliente": telefono_cliente,
        "correo_cliente": correo_cliente
    }

def guardar_cliente_formulario(tipo_documento_cliente, numero_documento_cliente, nombre_cliente, apellido_cliente, direccion_cliente, telefono_cliente, correo_cliente):
    if tipo_documento_cliente.get() and numero_documento_cliente.get() and nombre_cliente.get() and apellido_cliente.get() and correo_cliente.get():
        cliente = {
            "tipo_documento_cliente": tipo_documento_cliente.get(),
            "numero_documento_cliente": numero_documento_cliente.get(),
            "nombre_cliente": nombre_cliente.get(),
            "apellido_cliente": apellido_cliente.get(),
            "direccion_cliente": direccion_cliente.get(),
            "telefono_cliente": telefono_cliente.get(),
            "correo_cliente": correo_cliente.get(),
        }

        print("Cliente agregado con éxito:", cliente)
        respuesta = guardar_cliente_bd(cliente)
        messagebox.showinfo("Registro de Cliente", respuesta)

    else:
        messagebox.showwarning("Error", "⚠️ Todos los campos obligatorios deben estar llenos.")

def eliminar_cliente_formulario(numero_documento_cliente):
    """ Elimina un cliente de la base de datos basado en su número de documento """
    if numero_documento_cliente.get():
        respuesta = eliminar_cliente_bd(numero_documento_cliente.get())
        messagebox.showinfo("Eliminar Cliente", respuesta)
    else:
        messagebox.showwarning("Error", "⚠️ Debes ingresar un número de documento para eliminar un cliente.")

def actualizar_cliente_formulario(tipo_documento_cliente, numero_documento_cliente, nombre_cliente, apellido_cliente, direccion_cliente, telefono_cliente, correo_cliente):
    """ Actualiza los datos de un cliente existente en la base de datos """
    if tipo_documento_cliente.get() and numero_documento_cliente.get() and nombre_cliente.get() and apellido_cliente.get() and correo_cliente.get():
        cliente_actualizado = {
            "tipo_documento_cliente": tipo_documento_cliente.get(),
            "numero_documento_cliente": numero_documento_cliente.get(),
            "nombre_cliente": nombre_cliente.get(),
            "apellido_cliente": apellido_cliente.get(),
            "direccion_cliente": direccion_cliente.get(),
            "telefono_cliente": telefono_cliente.get(),
            "correo_cliente": correo_cliente.get(),
        }

        print("Cliente actualizado con éxito:", cliente_actualizado)
        respuesta = actualizar_cliente_bd(cliente_actualizado)
        messagebox.showinfo("Actualizar Cliente", respuesta)
    
    else:
        messagebox.showwarning("Error", "⚠️ Todos los campos obligatorios deben estar llenos.")

def buscar_cliente_formulario():
    """ Abre un cuadro de diálogo para pedir el número de documento y busca el cliente """
    numero_documento = simpledialog.askstring("Buscar Cliente", "Ingrese el número de documento:")
    
    if numero_documento:
        resultado = buscar_cliente_bd(numero_documento)
        
        if resultado["RESPUESTA"]:
            cliente = resultado["Cliente"]
            mensaje = f"Cliente encontrado:\n\nID: {cliente[0]}\nDocumento: {cliente[1]}\nNombre: {cliente[2]} {cliente[3]}\nCorreo: {cliente[6]}"
            messagebox.showinfo("Cliente Encontrado", mensaje)
        else:
            messagebox.showwarning("No Encontrado", resultado["Mensaje"])
    else:
        messagebox.showwarning("Cancelado", "Búsqueda cancelada por el usuario")


def formulario_gestion_empleados(ventana):
    pass

def formulario_gestion_motos(ventana):
    pass
