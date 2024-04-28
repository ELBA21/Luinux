from tkinter import *
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

    def cerrar_Editar():
        ventana_Editar.destroy() #Metodo que es llamado para cerrar la ventana

    #En esta malla estructurare toda la ventana
    #Por cierto esta ventana es basicamente un copypaste
    

    def guardarCambios(elemento_selecionado):
        nombre = textBoxNombre.get()
        cantidad = int(textBoxCantidad.get())
        precioCompra = int(textBoxPrecioCompra.get())
        precioVenta = int(textBoxPrecioVenta.get())
        surcursal_provisoria.productos[elemento_selecionado].nombre = nombre
        surcursal_provisoria.productos[elemento_selecionado].cantidad = cantidad
        surcursal_provisoria.productos[elemento_selecionado].precio_Compra = precioCompra
        surcursal_provisoria.productos[elemento_selecionado].precio_Venta = precioVenta

    mallaPrincipal = Frame(ventana_Editar, bd=2)
    mallaPrincipal.grid(row=0, column=0)


        #Quiero que la estructura sea algo como
        #LabelNombre    - LabelCantidad
        #TextBoxNombre  - TextBoxCantidad
        #LabelPrecioC   - LabelPrecioV
        #TextBoxPrecioC - TextBoxPrecioV
    #Nombre
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


    mallaBotones = Frame(mallaPrincipal)
    mallaBotones.grid(row=4, column=3)

    boton_Salir = Button(mallaBotones, text="Salir", command=cerrar_Editar)
    boton_Salir.grid(row=0,column=0)
    boton_Aceptar = Button(mallaBotones, text="Aceptar", command=lambda : guardarCambios(elemento_selecionado()))
    boton_Aceptar.grid(row=0, column=1)
    








    ventana_Editar.wait_window(ventana_Editar)