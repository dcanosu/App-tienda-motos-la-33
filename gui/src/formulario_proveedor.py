from tkinter import PhotoImage, StringVar, Label, Entry, Button, messagebox, simpledialog
from src.crud_proveedores import guardar_proveedor_bd, eliminar_proveedor_bd, actualizar_proveedor_bd, buscar_proveedor_bd

label_fuente = "Verdana", 25, "bold"
entry_fuente = "Verdana, 20"

def formulario_gestion_proveedor(ventana):
    # Variables de entrada
    id_proveedor = StringVar()
    nit = StringVar()
    nombre_proveedor = StringVar()
    direccion_proveedor = StringVar()
    telefono_proveedor = StringVar()
    correo_proveedor = StringVar()

    # Creación de los labels para solicitar la información
    Label(ventana, text="ID Proveedor:", font=label_fuente, fg="#002060", bg="white").place(x=800, y=250)
    Label(ventana, text="NIT:", font=label_fuente, fg="#002060", bg="white").place(x=800, y=300)
    Label(ventana, text="Nombre proveedor:", font=label_fuente, fg="#002060", bg="white").place(x=800, y=350)
    Label(ventana, text="Dirección proveedor:", font=label_fuente, fg="#002060", bg="white").place(x=800, y=400)
    Label(ventana, text="Teléfono proveedor:", font=label_fuente, fg="#002060", bg="white").place(x=800, y=450)
    Label(ventana, text="Correo proveedor:", font=label_fuente, fg="#002060", bg="white").place(x=800, y=500)

    color_bg = "white"
    color_fg = "black"
    # Construcción de las cajas
    Entry(ventana, textvariable=id_proveedor, font=entry_fuente, background=color_bg, foreground=color_fg).place(x=1100, y=250)
    Entry(ventana, textvariable=nit, font=entry_fuente,background=color_bg, foreground=color_fg,).place(x=1100, y=300)
    Entry(ventana, textvariable=nombre_proveedor, font=entry_fuente,background=color_bg, foreground=color_fg,).place(x=1100, y=350)
    Entry(ventana, textvariable=direccion_proveedor, font=entry_fuente, background=color_bg, foreground=color_fg).place(x=1100, y=400)
    Entry(ventana, textvariable=telefono_proveedor, font=entry_fuente, background=color_bg, foreground=color_fg).place(x=1100, y=450)
    Entry(ventana, textvariable=correo_proveedor, font=entry_fuente, background=color_bg, foreground=color_fg).place(x=1100, y=500)

    icono_guardar = PhotoImage(file="gui/iconos/guardar.png").subsample(4)
    boton_guardar = Button(ventana, image=icono_guardar, command=lambda: guardar_proveedor_formulario(nit, nombre_proveedor, direccion_proveedor,telefono_proveedor, correo_proveedor)) # falta command="")
    boton_guardar.image = icono_guardar  # Mantener referencia
    boton_guardar.place(x=900, y=670)
    
    icono_buscar = PhotoImage(file="gui/iconos/buscar.png").subsample(4)
    boton_buscar = Button(ventana, image=icono_buscar, command=buscar_proveedor_formulario)  # falta command="")
    boton_buscar.image = icono_buscar  # Mantener referencia
    boton_buscar.place(x=990, y=670)
    
    icono_eliminar = PhotoImage(file="gui/iconos/eliminar.png").subsample(4)
    boton_eliminar = Button(ventana, image=icono_eliminar, command=lambda: eliminar_proveedor_formulario(nit))  # falta command="")
    boton_eliminar.image = icono_eliminar  # Mantener referencia
    boton_eliminar.place(x=1100, y=670)
    
    icono_actulizar = PhotoImage(file="gui/iconos/actualizar.png").subsample(4)
    boton_actulizar = Button(ventana, image=icono_actulizar, command=lambda: actualizar_proveedor_formulario(nit, nombre_proveedor, direccion_proveedor, telefono_proveedor, correo_proveedor))  # falta command="")
    boton_actulizar.image = icono_actulizar  # Mantener referencia
    boton_actulizar.place(x=1190, y=670)

    # Retornar variables para su uso posterior si es necesario
    return {
        "nit": nit,
        "nombre_proveedor": nombre_proveedor,
        "direccion_proveedor": direccion_proveedor,
        "telefono_proveedor": telefono_proveedor,
        "correo_proveedor": correo_proveedor
    }


def guardar_proveedor_formulario(nit, nombre_proveedor, direccion_proveedor, telefono_proveedor, correo_proveedor):
    if nit.get() and nombre_proveedor.get() and direccion_proveedor.get() and telefono_proveedor.get() and correo_proveedor.get():
        proveedor = {
            "nit": nit.get(),
            "nombre_proveedor": nombre_proveedor.get(),
            "direccion_proveedor": direccion_proveedor.get(),
            "telefono_proveedor": telefono_proveedor.get(),
            "correo_proveedor": correo_proveedor.get(),
        }

        print("Proveedor agregado con éxito:", proveedor)
        respuesta = guardar_proveedor_bd(proveedor)
        messagebox.showinfo("Registro de Proveedor", respuesta)

    else:
        messagebox.showwarning("Error", "⚠️ Todos los campos obligatorios deben estar llenos.")

def eliminar_proveedor_formulario(nit):
    """ Elimina un proveedor de la base de datos basado en su número de documento """
    if nit.get():
        respuesta = eliminar_proveedor_bd(nit.get())
        messagebox.showinfo("Eliminar Proveedor", respuesta)
    else:
        messagebox.showwarning("Error", "⚠️ Debes ingresar un número de documento para eliminar un proveedor.")

def actualizar_proveedor_formulario(nit, nombre_proveedor, direccion_proveedor, telefono_proveedor, correo_proveedor):
    """ Actualiza los datos de un proveedor existente en la base de datos """
    if  nit.get() and nombre_proveedor.get() and direccion_proveedor.get() and telefono_proveedor.get() and correo_proveedor.get():
        proveedor_actualizado = {
            "nit": nit.get(),
            "nombre_proveedor": nombre_proveedor.get(),
            "direccion_proveedor": direccion_proveedor.get(),
            "telefono_proveedor": telefono_proveedor.get(),
            "correo_proveedor": correo_proveedor.get(),
        }

        print("Proveedor actualizado con éxito:", proveedor_actualizado)
        respuesta = actualizar_proveedor_bd(proveedor_actualizado)
        messagebox.showinfo("Actualizar Proveedor", respuesta)
    
    else:
        messagebox.showwarning("Error", "⚠️ Todos los campos obligatorios deben estar llenos.")

def buscar_proveedor_formulario():
    """ Abre un cuadro de diálogo para pedir el número de documento y busca el proveedor """
    nit = simpledialog.askstring("Buscar Proveedor", "Ingrese el número del NIT:")
    
    if nit:
        resultado = buscar_proveedor_bd(nit)
        
        if resultado["RESPUESTA"]:
            proveedor = resultado["Cliente"]
            mensaje = f"Proveedor encontrado:\n\nID proveedor: {proveedor[0]}\nNit: {proveedor[1]}\nNombre proveedor: {proveedor[2]}\nDirección proveedor: {proveedor[3]}\nTelefono: {proveedor[4]}\nCorreo: {proveedor[5]}"
            messagebox.showinfo("Proveedor Encontrado", mensaje)
        else:
            messagebox.showwarning("No Encontrado", resultado["Mensaje"])
    else:
        messagebox.showwarning("Cancelado", "Búsqueda cancelada por el usuario")