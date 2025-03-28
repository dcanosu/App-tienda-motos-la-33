from tkinter import PhotoImage, StringVar, Label, Entry, Button, messagebox, simpledialog, CENTER, NO, END, E, ttk
from src.crud_facturacion import guardar_venta_bd, eliminar_venta_bd, actualizar_venta_bd, buscar_venta_bd, listar_detalles_ventas_empleado_db

label_fuente = "Verdana", 25, "bold"
entry_fuente = "Verdana, 20"

def formulario_gestion_venta(ventana):
    # Variables de entrada
    id_venta = StringVar()
    id_cliente = StringVar()
    id_empleado = StringVar()
    fecha_venta = StringVar()
    total_venta = StringVar()

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
    boton_guardar = Button(ventana, image=icono_guardar, command=lambda: guardar_venta_formulario(id_cliente, id_empleado, fecha_venta, total_venta))
    boton_guardar.image = icono_guardar  # Mantener referencia
    boton_guardar.place(x=900, y=670)
    
    icono_buscar = PhotoImage(file="gui/iconos/buscar.png").subsample(4)
    boton_buscar = Button(ventana, image=icono_buscar, command=lambda: buscar_venta_formulario(id_venta, id_cliente, id_empleado, fecha_venta, total_venta))
    boton_buscar.image = icono_buscar  # Mantener referencia
    boton_buscar.place(x=990, y=670)
    
    icono_eliminar = PhotoImage(file="gui/iconos/eliminar.png").subsample(4)
    boton_eliminar = Button(ventana, image=icono_eliminar, command=lambda: eliminar_venta_formulario(id_venta))
    boton_eliminar.image = icono_eliminar  # Mantener referencia
    boton_eliminar.place(x=1100, y=670)
    
    icono_actulizar = PhotoImage(file="gui/iconos/actualizar.png").subsample(4)
    boton_actulizar = Button(ventana, image=icono_actulizar, command=lambda: actualizar_venta_formulario(id_cliente, id_empleado, fecha_venta, total_venta))
    boton_actulizar.image = icono_actulizar  # Mantener referencia
    boton_actulizar.place(x=1190, y=670)

    # Retornar variables para su uso posterior
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

def actualizar_venta_formulario(id_cliente,id_empleado,fecha_venta,total_venta):
    """ Actualiza los datos de un proveedor existente en la base de datos """
    if  id_cliente.get() and id_empleado.get() and fecha_venta.get() and total_venta.get():
        venta_actualizada = {
            "id_cliente": id_cliente.get(),
            "id_empleado": id_empleado.get(),
            "fecha_venta": fecha_venta.get(),
            "total_venta": total_venta.get(),
        }

        print("Venta actualizada con éxito:", venta_actualizada)
        respuesta = actualizar_venta_bd(venta_actualizada)
        messagebox.showinfo("Actualizar Venta", respuesta)
    
    else:
        messagebox.showwarning("Error", "⚠️ Todos los campos obligatorios deben estar llenos.")

def buscar_venta_formulario(id_venta, id_cliente, id_empleado, fecha_venta, total_venta):
    id_de_venta = simpledialog.askstring("Buscar Venta", "Ingrese el número del ID venta:")
    
    if id_de_venta:
        resultado = buscar_venta_bd(id_de_venta)
        
        if resultado["RESPUESTA"]:
            venta = resultado["Venta"]
            id_venta.set(venta[0])
            id_cliente.set(venta[1])
            id_empleado.set(venta[2])
            fecha_venta.set(venta[3])
            #total_venta.set(venta[4])
            # Formatear el total con separador de miles
            total_formateado = "{:,.0f}".format(venta[4])
            total_venta.set(total_formateado)  # Mostrarlo en el Entry con format
        else:
            messagebox.showwarning("No Encontrado", resultado["Mensaje"])
    else:
        messagebox.showwarning("Cancelado", "Búsqueda cancelada por el usuario")

def mostrar_detalles_ventas_empleado(ventana):

    # Aplicar estilo a los encabezados
    style = ttk.Style()
    style.theme_use("clam")  # tema compatible con fondo en encabezados
    style.configure("Treeview.Heading", font=("Verdana", 11, "bold"), background="#002060", foreground="white")

    tabla = ttk.Treeview(ventana)
    tabla.place(x=80, y=230)

    # Definir columnas
    tabla["columns"] = ("ID Empleado", "Nombre", "Apellido", "Cargo", "Total Ventas")
    
    # Configurar el ancho y alineación de las columnas
    tabla.column("#0", width=0, stretch=NO)
    tabla.column("ID Empleado", width=100, anchor=CENTER)
    tabla.column("Nombre", width=150, anchor=CENTER)
    tabla.column("Apellido", width=150, anchor=CENTER)
    tabla.column("Cargo", width=100, anchor=CENTER)
    tabla.column("Total Ventas", width=100, anchor=E) # Alinear a la derecha (E) para números
    
    # Configurar encabezados
    tabla.heading("#0", text="")
    tabla.heading("ID Empleado", text="ID Empleado")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Apellido", text="Apellido")
    tabla.heading("Cargo", text="Cargo")
    tabla.heading("Total Ventas", text="Total Ventas")
    
    # Definir colores alternos en las filas
    tabla.tag_configure("even", background="#b4c6e7")  # Gris claro
    tabla.tag_configure("odd", background="#d9e1f2")  # Blanco

    def llenar_tabla():
        tabla.delete(*tabla.get_children()) # Limpiar tabla antes de cargar nuevos datos
        respuesta = listar_detalles_ventas_empleado_db()
        empleados = respuesta.get("Empleados", [])
        
        for i, empleado in enumerate(empleados):
            total_ventas = empleado.get("Total Ventas", 0)  # Si es None, usa 0
            
            # Formatear número con separador de miles
            total_ventas = "{:,.0f}".format(total_ventas) if total_ventas is not None else "0"

            # Alternar colores en las filas
            tag = "even" if i % 2 == 0 else "odd"

            tabla.insert("", END, values=(
                empleado["ID Empleado"], 
                empleado["Nombre"], 
                empleado["Apellido"], 
                empleado["Cargo"], 
                total_ventas  # Valor formateado con comas
            ), tags=(tag,))
    llenar_tabla()
    return tabla
        
"""        for empleado in empleados:
            total_ventas = empleado.get("Total Ventas", 0)  # Si es None, usa 0
            
            # Convertir a número y formatear con separador de miles
            total_ventas = "{:,.0f}".format(total_ventas) if total_ventas is not None else "0"
            
            tabla.insert("", END, values=(
                empleado["ID Empleado"], 
                empleado["Nombre"], 
                empleado["Apellido"], 
                empleado["Cargo"], 
                #empleado["Total Ventas"]
                total_ventas # Valor formateado con comas
            ))
    
    llenar_tabla()
    return tabla"""
