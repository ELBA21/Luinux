from tkinter import *
from tkinter import messagebox
from Productos import Productos
from Main import admin
from Main import guardar

def abrir_Editar(pagina_Principal, surcursal_provisoria, listBoxProductos, elemento_selecionado):
    ventana_Editar = Toplevel(pagina_Principal)
    ventana_Editar.title("Editar Valores de un Producto")
    ventana_Editar.focus()
    ventana_Editar.grab_set()
    ventana_Editar.geometry("400x200")
    producto_seleccionado = surcursal_provisoria.productos[elemento_selecionado]
    #surcursal_provisoria.agregar_productos(1, 1, 1, 1, True)
    def cerrar_Editar():
        print("Se ciera ventana Editar")
        ventana_Editar.destroy()

    def guardarCambios():
        print("guardar cambios")
        nombre = textBoxNombre.get()
        id = Productos.generar_id(nombre)
        stock = textBoxCantidad.get()
        precio_venta = textBoxPrecioVenta.get()
        precio_compra = textBoxPrecioCompra.get()
        print("values checked")
        surcursal_provisoria.eliminar_producto(elemento_selecionado)
        surcursal_provisoria.agregar_productos(nombre, precio_venta, precio_compra, stock, True)
        surcursal_provisoria.print_productos()
        guardar(admin)
        cerrar_Editar()

    mallaPrincipal = Frame(ventana_Editar, bd=4)
    mallaPrincipal.pack()

    # Agregar Nombre
    labelNombre = Label(mallaPrincipal, text="Nombre:")
    labelNombre.grid(row=0, column=0)
    textBoxNombre = Entry(mallaPrincipal, borderwidth=1, relief="solid")
    textBoxNombre.grid(row=1, column=0)
    textBoxNombre.insert(0, producto_seleccionado.get_nombre())

    # Cantidad
    labelCantidad = Label(mallaPrincipal, text="Cantidad:")
    labelCantidad.grid(row=0, column=1)
    textBoxCantidad = Entry(mallaPrincipal, borderwidth=1, relief="solid")
    textBoxCantidad.grid(row=1, column=1)
    textBoxCantidad.insert(0, producto_seleccionado.get_stock())

    # Precio Compra
    labelPrecioCompra = Label(mallaPrincipal, text="Precio Compra:")
    labelPrecioCompra.grid(row=2, column=0)
    textBoxPrecioCompra = Entry(mallaPrincipal, borderwidth=1, relief="solid")
    textBoxPrecioCompra.grid(row=3, column=0)
    textBoxPrecioCompra.insert(0, producto_seleccionado.get_precio_compra())

    # Precio Venta
    labelPrecioVenta = Label(mallaPrincipal, text="Precio Venta:")
    labelPrecioVenta.grid(row=2, column=1)
    textBoxPrecioVenta = Entry(mallaPrincipal, borderwidth=1, relief="solid")
    textBoxPrecioVenta.grid(row=3, column=1)
    textBoxPrecioVenta.insert(0, producto_seleccionado.get_precio_venta())

    malla_botones = Frame(ventana_Editar, bd=8)
    malla_botones.pack()
    botonAgregar = Button(malla_botones, text="Aceptar", command=guardarCambios, bg="lightgrey", borderwidth=1, relief="solid")
    botonAgregar.grid(row=0, column=0, padx=15)
    botonCerrar = Button(malla_botones, text="Cerrar", command=cerrar_Editar, bg="lightgrey", borderwidth=1, relief="solid")
    botonCerrar.grid(row=0, column=1)

    # Vincula la tecla Enter al botón "Aceptar"
    ventana_Editar.bind('<Return>', lambda event: botonAgregar.invoke())

    ventana_Editar.wait_window(ventana_Editar)
