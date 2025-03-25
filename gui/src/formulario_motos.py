from tkinter import DoubleVar, PhotoImage, StringVar, Label, Entry, Button, messagebox, simpledialog
from src.crud_motos import guardar_moto_bd, eliminar_moto_bd, actualizar_moto_bd, buscar_moto_bd

label_fuente = "Verdana", 25, "bold"
entry_fuente = "Verdana, 20"

def formulario_gestion_motos(ventana):
    # Variables de entrada
    id_moto = StringVar()
    ref_moto = StringVar()
    modelo = StringVar()
    color = StringVar()
    precio = DoubleVar()
    cantidad_disponible = StringVar()

    # Creación de los labels para solicitar la información
    Label(ventana, text="ID moto:", font=label_fuente, fg="#002060", bg="white").place(x=800, y=250)
    Label(ventana, text="Referencia moto:", font=label_fuente, fg="#002060", bg="white").place(x=800, y=300)
    Label(ventana, text="Modelo:", font=label_fuente, fg="#002060", bg="white").place(x=800, y=350)
    Label(ventana, text="Color:", font=label_fuente, fg="#002060", bg="white").place(x=800, y=400)
    Label(ventana, text="Precio $:", font=label_fuente, fg="#002060", bg="white").place(x=800, y=450)
    Label(ventana, text="Cantidad disponible:", font=label_fuente, fg="#002060", bg="white").place(x=800, y=500)

    color_bg = "white"
    color_fg = "black"
    # Construcción de las cajas
    Entry(ventana, textvariable=id_moto, font=entry_fuente, background=color_bg, foreground=color_fg).place(x=1100, y=250)
    Entry(ventana, textvariable=ref_moto, font=entry_fuente,background=color_bg, foreground=color_fg,).place(x=1100, y=300)
    Entry(ventana, textvariable=modelo, font=entry_fuente,background=color_bg, foreground=color_fg,).place(x=1100, y=350)
    Entry(ventana, textvariable=color, font=entry_fuente, background=color_bg, foreground=color_fg).place(x=1100, y=400)
    Entry(ventana, textvariable=precio, font=entry_fuente, background=color_bg, foreground=color_fg).place(x=1100, y=450)
    Entry(ventana, textvariable=cantidad_disponible, font=entry_fuente, background=color_bg, foreground=color_fg).place(x=1100, y=500)

    icono_guardar = PhotoImage(file="gui/iconos/guardar.png").subsample(4)
    boton_guardar = Button(ventana, image=icono_guardar, command=lambda: guardar_moto_formulario(ref_moto, modelo, color,precio, cantidad_disponible)) # falta command="")
    boton_guardar.image = icono_guardar  # Mantener referencia
    boton_guardar.place(x=900, y=670)
    
    icono_buscar = PhotoImage(file="gui/iconos/buscar.png").subsample(4)
    boton_buscar = Button(ventana, image=icono_buscar, command=buscar_moto_formulario)  # falta command="")
    boton_buscar.image = icono_buscar  # Mantener referencia
    boton_buscar.place(x=990, y=670)
    
    icono_eliminar = PhotoImage(file="gui/iconos/eliminar.png").subsample(4)
    boton_eliminar = Button(ventana, image=icono_eliminar, command=lambda: eliminar_moto_formulario(ref_moto))  # falta command="")
    boton_eliminar.image = icono_eliminar  # Mantener referencia
    boton_eliminar.place(x=1100, y=670)
    
    icono_actulizar = PhotoImage(file="gui/iconos/actualizar.png").subsample(4)
    boton_actulizar = Button(ventana, image=icono_actulizar, command=lambda: actualizar_moto_formulario(ref_moto, modelo, color, precio, cantidad_disponible))  # falta command="")
    boton_actulizar.image = icono_actulizar  # Mantener referencia
    boton_actulizar.place(x=1190, y=670)

    # Retornar variables para su uso posterior si es necesario
    return {
        "ref_moto": ref_moto,
        "modelo": modelo,
        "color": color,
        "precio": precio,
        "cantidad_disponible": cantidad_disponible
    }


def guardar_moto_formulario(ref_moto, modelo, color, precio, cantidad_disponible):
    if ref_moto.get() and modelo.get() and color.get() and precio.get() and cantidad_disponible.get():
        moto = {
            "ref_moto": ref_moto.get(),
            "modelo": modelo.get(),
            "color": color.get(),
            "precio": precio.get(),
            "cantidad_disponible": cantidad_disponible.get(),
        }

        print("Moto agregada con éxito:", moto)
        respuesta = guardar_moto_bd(moto)
        messagebox.showinfo("Registro de Moto", respuesta)

    else:
        messagebox.showwarning("Error", "⚠️ Todos los campos obligatorios deben estar llenos.")

def eliminar_moto_formulario(ref_moto):
    """ Elimina un moto de la base de datos basado en su id """
    if ref_moto.get():
        respuesta = eliminar_moto_bd(ref_moto.get())
        messagebox.showinfo("Eliminar Moto", respuesta)
    else:
        messagebox.showwarning("Error", "⚠️ Debes ingresar un número de documento para eliminar un moto.")

def actualizar_moto_formulario(ref_moto, modelo, color, precio, cantidad_disponible):
    """ Actualiza los datos de un moto existente en la base de datos """
    if  ref_moto.get() and modelo.get() and color.get() and precio.get() and cantidad_disponible.get():
        moto_actualizado = {
            "ref_moto": ref_moto.get(),
            "modelo": modelo.get(),
            "color": color.get(),
            "precio": precio.get(),
            "cantidad_disponible": cantidad_disponible.get(),
        }

        print("Moto actualizado con éxito:", moto_actualizado)
        respuesta = actualizar_moto_bd(moto_actualizado)
        messagebox.showinfo("Actualizar Moto", respuesta)
    
    else:
        messagebox.showwarning("Error", "⚠️ Todos los campos obligatorios deben estar llenos.")

def buscar_moto_formulario():
    """ Abre un cuadro de diálogo para pedir el número de documento y busca el moto """
    ref_moto = simpledialog.askstring("Buscar Moto", "Ingrese el número del ref_moto:")
    
    if ref_moto:
        resultado = buscar_moto_bd(ref_moto)
        
        if resultado["RESPUESTA"]:
            moto = resultado["Cliente"]
            mensaje = f"Moto encontrado:\n\nID moto: {moto[0]}\nref_moto: {moto[1]}\nNombre moto: {moto[2]}\nDirección moto: {moto[3]}\nTelefono: {moto[4]}\nCorreo: {moto[5]}"
            messagebox.showinfo("Moto Encontrado", mensaje)
        else:
            messagebox.showwarning("No Encontrado", resultado["Mensaje"])
    else:
        messagebox.showwarning("Cancelado", "Búsqueda cancelada por el usuario")