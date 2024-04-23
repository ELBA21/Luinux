from tkinter import *

def abrirAgregar(principalProductos, surcursal_provisoria, listBoxProductos):   
    agregar = Toplevel(principalProductos)
    agregar.title("Agregar Producto")
    agregar.focus()
    agregar.geometry("400x200")

    def cerrarAgregar():
        agregar.destroy()
    




    #====================Creo una malla para organizar los temas
    mallaPrincipal = Frame(agregar, bd=2)
    mallaPrincipal.grid(row=0,column=0)
    #=============================================================
        #La distribucion deberia ser asi
        #Nombre-Cantidad
        #Compra-Venta
    #Agregar Nombre
    labelNombre = Label(mallaPrincipal,text="Nombre:")
    labelNombre.grid(row=0,column=0)
    textBoxNombre = Entry(mallaPrincipal)
    textBoxNombre.grid(row=1, column=0)

    #Cantidad
    labelCantidad = Label(mallaPrincipal, text="Cantidad:")
    labelCantidad.grid(row=0,column=1)
    textBoxCantidad = Entry(mallaPrincipal)
    textBoxCantidad.grid(row=1, column=1)

    #Agrebar Precio Compra
    labelPrecioCompra = Label(mallaPrincipal, text="Precio Compra:")
    labelPrecioCompra.grid(row=2, column=0)
    textBoxPrecioCompra = Entry(mallaPrincipal)
    textBoxPrecioCompra.grid(row=3, column=0)

    #Agregar Precio Venta
    labelPrecioVenta = Label(mallaPrincipal, text="Precio Venta")
    labelPrecioVenta.grid(row=2,column=1)
    textBoxPrecioVenta = Entry(mallaPrincipal)
    textBoxPrecioVenta.grid(row=3, column=1)


    def agregarProductos():
        print("Boton Agregar")
        nombre = textBoxNombre.get()
        cantidad = int(textBoxCantidad.get())
        precioCompra = int(textBoxPrecioCompra.get())
        precioVenta = int(textBoxPrecioVenta.get())
        testcant = surcursal_provisoria.get_tamano()
        surcursal_provisoria.agregar_productos(nombre, precioVenta, precioCompra, cantidad)
        if testcant < surcursal_provisoria.get_tamano(): #verifica que no se agregue un objeto dos veces a la lista
            surcursal_provisoria.get_productos(surcursal_provisoria.get_tamano()-1).set_autoid()
            listBoxProductos.insert(END, nombre)
        cerrarAgregar()
    botonAgregar = Button(mallaPrincipal, text="Aceptar", command=agregarProductos)
    botonAgregar.grid(row=5,column=5)
    botonCerrar = Button(mallaPrincipal, text= "Cerrar", command=cerrarAgregar)
    botonCerrar.grid(row=5,column=4)
    #==============



    #=================================
        #AAAAAAAAAAAAAAAA



    
    agregar.wait_window(agregar)  