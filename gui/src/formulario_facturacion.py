from tkinter import PhotoImage, StringVar, Label, Entry, Button, messagebox, simpledialog, CENTER, NO, END, ttk
from src.crud_facturacion import guardar_venta_bd, eliminar_venta_bd, actualizar_venta_bd, buscar_venta_bd, listar_detalles_ventas_empleado_db

label_fuente = "Verdana", 25, "bold"
entry_fuente = "Verdana, 20"

def formulario_gestion_venta(ventana):
    # Variables de entrada
    id_cliente = StringVar()
    id_empleado = StringVar()
    fecha_venta = StringVar()
    total_venta = StringVar()
    id_venta = StringVar()


    # Creación de los labels para solicitar la información
    Label(ventana, text="ID Venta:", font=label_fuente, fg="#002060", bg="white").place(x=800, y=250)
    Label(ventana, text="ID Cliente:", font=label_fuente, fg="#002060", bg="white").place(x=800, y=300)
    Label(ventana, text="ID Empleado:", font=label_fuente, fg="#002060", bg="white").place(x=800, y=350)
    Label(ventana, text="Fecha Venta:", font=label_fuente, fg="#002060", bg="white").place(x=800, y=400)
    Label(ventana, text="Total Venta:", font=label_fuente, fg="#002060", bg="white").place(x=800, y=450)
    

    color_bg = "white"
    color_fg = "black"
    # Construcción de las cajas
    Entry(ventana, textvariable=id_venta, font=entry_fuente, background=color_bg, foreground=color_fg).place(x=1100, y=250)
    Entry(ventana, textvariable=id_cliente, font=entry_fuente, background=color_bg, foreground=color_fg).place(x=1100, y=300)
    Entry(ventana, textvariable=id_empleado, font=entry_fuente,background=color_bg, foreground=color_fg,).place(x=1100, y=350)
    Entry(ventana, textvariable=fecha_venta, font=entry_fuente,background=color_bg, foreground=color_fg,).place(x=1100, y=400)
    Entry(ventana, textvariable=total_venta, font=entry_fuente, background=color_bg, foreground=color_fg).place(x=1100, y=450)
    
    icono_guardar = PhotoImage(file="gui/iconos/guardar.png").subsample(4)
    boton_guardar = Button(ventana, image=icono_guardar, command=lambda: guardar_venta_formulario(id_cliente, id_empleado, fecha_venta, total_venta)) # falta command="")
    boton_guardar.image = icono_guardar  # Mantener referencia
    boton_guardar.place(x=900, y=670)
    
    icono_buscar = PhotoImage(file="gui/iconos/buscar.png").subsample(4)
    boton_buscar = Button(ventana, image=icono_buscar, command=buscar_venta_formulario)  # falta command="")
    boton_buscar.image = icono_buscar  # Mantener referencia
    boton_buscar.place(x=990, y=670)
    
    icono_eliminar = PhotoImage(file="gui/iconos/eliminar.png").subsample(4)
    boton_eliminar = Button(ventana, image=icono_eliminar, command=lambda: eliminar_venta_formulario(id_venta))  # falta command="")
    boton_eliminar.image = icono_eliminar  # Mantener referencia
    boton_eliminar.place(x=1100, y=670)
    
    icono_actulizar = PhotoImage(file="gui/iconos/actualizar.png").subsample(4)
    boton_actulizar = Button(ventana, image=icono_actulizar, command=lambda: actualizar_venta_formulario(id_cliente, id_empleado, fecha_venta, total_venta))  # falta command="")
    boton_actulizar.image = icono_actulizar  # Mantener referencia
    boton_actulizar.place(x=1190, y=670)

    # Retornar variables para su uso posterior si es necesario
    return {
        "id_venta": id_venta,
        "id_cliente": id_cliente,
        "id_empleado": id_empleado,
        "total_venta": total_venta,
        "fecha_venta": fecha_venta
    }


def guardar_venta_formulario(id_cliente,id_empleado,fecha_venta,total_venta):
    if id_cliente.get() and id_empleado.get() and fecha_venta.get() and total_venta.get():
        venta = {
            "id_cliente": id_cliente.get(),
            "id_empleado": id_empleado.get(),
            "fecha_venta": fecha_venta.get(),
            "total_venta": total_venta.get(),
        }

        print("Venta agregada con éxito:", venta)
        respuesta = guardar_venta_bd(venta)
        messagebox.showinfo("Registro de Venta", respuesta)

    else:
        messagebox.showwarning("Error", "⚠️ Todos los campos obligatorios deben estar llenos.")

def eliminar_venta_formulario(id_venta):
    if id_venta.get():
        respuesta = eliminar_venta_bd(id_venta.get())
        messagebox.showinfo("Eliminar Venta", respuesta)
    else:
        messagebox.showwarning("Error", "⚠️ Debes ingresar un ID de venta para eliminar una venta.")

def actualizar_venta_formulario(id_cliente,id_empleado,fecha_venta,total_venta, id_venta):
    """ Actualiza los datos de un proveedor existente en la base de datos """
    if  id_cliente.get() and id_empleado.get() and fecha_venta.get() and total_venta.get() and id_venta.get():
        venta_actualizada = {
            "id_cliente": id_cliente.get(),
            "id_empleado": id_empleado.get(),
            "fecha_venta": fecha_venta.get(),
            "valor_venta": total_venta.get(),
            "id_venta": id_venta.get(),
        }

        print("Venta actualizada con éxito:", venta_actualizada)
        respuesta = actualizar_venta_bd(venta_actualizada)
        messagebox.showinfo("Actualizar Venta", respuesta)
    
    else:
        messagebox.showwarning("Error", "⚠️ Todos los campos obligatorios deben estar llenos.")

def buscar_venta_formulario():
    """ Abre un cuadro de diálogo para pedir el número de documento y busca el proveedor """
    id_venta = simpledialog.askstring("Buscar Venta", "Ingrese el número del ID venta:")
    
    if id_venta:
        resultado = buscar_venta_bd(id_venta)
        
        if resultado["RESPUESTA"]:
            venta = resultado["Venta"]
            mensaje = f"Venta encontrada:\n\nID Cliente: {venta[0]}\nID Empleado: {venta[1]}\nFecha venta: {venta[2]}\nValor venta: {venta[3]}\nID venta: {venta[4]}"
            messagebox.showinfo("Venta Encontrada", mensaje)
        else:
            messagebox.showwarning("No Encontrado", resultado["Mensaje"])
    else:
        messagebox.showwarning("Cancelado", "Búsqueda cancelada por el usuario")

def mostrar_detalles_ventas_empleado(ventana):
    fuente_lista = ("Verdana", 14)
    Label(ventana, text="Detalles de Ventas por Empleado", justify="center", font=fuente_lista, 
          foreground="white", background="red").place(x=120, y=150)

    tabla = ttk.Treeview(ventana)
    tabla.place(x=90, y=220)

    tabla["columns"] = ("ID Empleado", "Nombre", "Apellido", "Cargo", "Total Ventas")
    
    tabla.column("#0", width=0, stretch=NO)
    tabla.column("ID Empleado", width=80, anchor=CENTER)
    tabla.column("Nombre", width=150, anchor=CENTER)
    tabla.column("Apellido", width=150, anchor=CENTER)
    tabla.column("Cargo", width=100, anchor=CENTER)
    tabla.column("Total Ventas", width=100, anchor=CENTER)
    
    tabla.heading("#0", text="")
    tabla.heading("ID Empleado", text="ID Empleado")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Apellido", text="Apellido")
    tabla.heading("Cargo", text="Cargo")
    tabla.heading("Total Ventas", text="Total Ventas")

    def llenar_tabla():
        tabla.delete(*tabla.get_children())
        respuesta = listar_detalles_ventas_empleado_db()
        empleados = respuesta.get("Empleados", [])
        
        for empleado in empleados:
            tabla.insert("", END, values=(
                empleado["ID Empleado"], 
                empleado["Nombre"], 
                empleado["Apellido"], 
                empleado["Cargo"], 
                empleado["Total Ventas"]
            ))
    
    llenar_tabla()
    return tabla
