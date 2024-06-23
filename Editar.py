from tkinter import *
from tkinter import messagebox
from Productos import Productos
from Main import admin
from Main import guardar
def abrir_Editar(pagina_Principal, surcursal_provisoria, listBoxProductos, elemento_selecionado):
    ventana_Editar = Toplevel(pagina_Principal)
    #TopLevel es un metodo que asigna una jerarquia entre las ventanas
    #En este caso lo que pasa es que le metodo 'abrir_Editar' al ser llamado en la pagina princpal, recibe como argumento
    #la propia ventana princial
    #Aca en este archivo se recibe ese argumento y es insertado en el metodo TopLevel(), asi le decimos al programa
    #que la ventana actual, esta por debajo de la principal.
    ventana_Editar.title("Editar Valores de un Producto") #Le cambio el titutlo
    ventana_Editar.focus() #Se fuerza la visualizacion de la ventana actual
    ventana_Editar.grab_set() #Se bloquea toda ventana que no sea esta (Debe usarse junto al metodo .focus)
    ventana_Editar.geometry("400x200")
    producto_seleccionado = surcursal_provisoria.productos[elemento_selecionado] #Para acortar el llamado de productos en la pagina
    def cerrar_Editar():
        print("Se ciera ventana Editar")
        ventana_Editar.destroy() #Metodo que es llamado para cerrar la ventana

    #En esta malla estructurare toda la ventana
    #Por cierto esta ventana es basicamente un copypaste

    def guardarCambios():
        print("guardar cambios")
        nombre = producto_seleccionado.get_nombre()
        id = Productos.generar_id(nombre)
        stock = producto_seleccionado.get_stock()
        precio_venta = producto_seleccionado.get_precio_venta()
        precio_compra = producto_seleccionado.get_precio_compra()
        print("values checked")
        #eliminamos el objeto y creamos uno nuevo
        #lo hago asi porque es facil y se reutiliza codigo
        surcursal_provisoria.eliminar_producto(elemento_selecionado)
        surcursal_provisoria.agregar_productos(nombre, precio_venta, precio_compra, stock)
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






    ventana_Editar.wait_window(ventana_Editar)