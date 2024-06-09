from tkinter import *

def abrirAgregar(principalProductos, surcursal_provisoria, listBoxProductos):   
    agregar = Toplevel(principalProductos)
    agregar.title("Agregar producto")
    agregar.focus()
    agregar.grab_set()
    agregar.geometry("400x200")

    def cerrarAgregar():
        agregar.destroy()
    
    #====================Creo una malla para organizar los temas
    mallaPrincipal = Frame(agregar, bd=4)
    mallaPrincipal.pack()
    #=============================================================
        #La distribucion deberia ser asi
        #Nombre-Cantidad 
        #Compra-Venta
    #Agregar Nombre
    labelNombre = Label(mallaPrincipal,text="Nombre:")
    labelNombre.grid(row=0,column=0)
    textBoxNombre = Entry(mallaPrincipal, borderwidth=1, relief="solid")
    textBoxNombre.grid(row=1, column=0)

    #Cantidad
    labelCantidad = Label(mallaPrincipal, text="Cantidad:")
    labelCantidad.grid(row=0,column=1)
    textBoxCantidad = Entry(mallaPrincipal, borderwidth=1, relief="solid")
    textBoxCantidad.grid(row=1, column=1)

    #Agrebar Precio Compra
    labelPrecioCompra = Label(mallaPrincipal, text="Precio Compra:")
    labelPrecioCompra.grid(row=2, column=0)
    textBoxPrecioCompra = Entry(mallaPrincipal, borderwidth=1, relief="solid")
    textBoxPrecioCompra.grid(row=3, column=0)

    #Agregar Precio Venta
    labelPrecioVenta = Label(mallaPrincipal, text="Precio Venta:")
    labelPrecioVenta.grid(row=2,column=1)
    textBoxPrecioVenta = Entry(mallaPrincipal, borderwidth=1, relief="solid")
    textBoxPrecioVenta.grid(row=3, column=1)


    def agregarProductos():
        print("Boton Agregar")
        agregar.grab_release()
        nombre = textBoxNombre.get()
        cantidad = int(textBoxCantidad.get())
        precioCompra = int(textBoxPrecioCompra.get())
        precioVenta = int(textBoxPrecioVenta.get())
        surcursal_provisoria.agregar_productos(nombre, precioVenta, precioCompra, cantidad)
        cerrarAgregar()
    malla_botones = Frame(agregar, bd=8)
    malla_botones.pack()
    botonAgregar = Button(malla_botones, text="Aceptar", command=agregarProductos, bg= "lightgrey", borderwidth=1, relief="solid")
    botonAgregar.grid(row=0,column=0, padx=15)
    botonCerrar = Button(malla_botones, text= "Cerrar", command=cerrarAgregar, bg= "lightgrey", borderwidth=1, relief="solid")
    botonCerrar.grid(row=0,column=1)
    #==============



    #=================================
        #AAAAAAAAAAAAAAAA



    
    agregar.wait_window(agregar)  