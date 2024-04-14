from tkinter import *
from Productos import Productos
from Sucursal import Sucursal
##Cosas temporales
surcursal_provisoria = Sucursal(1)
surcursal_provisoria.productos = []
print("Cuantos productos quieres agregar?")
cant = int(input())
for i in range(cant):
       testnombre=input()
       testprecio=int(input())
       testcant=int(input())
       surcursal_provisoria.agregar_productos(testnombre,testprecio,testcant)




def testeoDeBotones():
       print("HOLA ESTOY SIENDO TESTEADO :3 NYA")

    
#===================== Crear la ventana principal
ventana = Tk()
ventana.title("Lista de Productos")
#====================================

#=======================Malla para organizar
mallaPrincipal = Frame(ventana, bd=2,relief="ridge")
mallaPrincipal.grid(row=0,column=0)
#=============================================================


                #==========================Elementos de la malla
                #=======================================

#================ListBox=====
listBoxProductos = Listbox(mallaPrincipal, width=50, height=10)
listBoxProductos.grid(row=0, column=0)
#==========================



#==============================Botones
mallaDeBotones = Frame(mallaPrincipal, bd=2, relief="ridge")
mallaDeBotones.grid(row=1, column=0)
botonAgregar = Button(mallaDeBotones, text="Agregar")
botonAgregar.grid(row=0,column=0)
botonEditar = Button(mallaDeBotones, text="Editar")
botonEditar.grid(row=0, column=1)
BotonEliminar = Button(mallaDeBotones, text="Eliminar")
BotonEliminar.grid(row=0, column=2)
#=======================================

#===================Labels De Informacion
mallaDeLabels = Frame(mallaPrincipal, bd=2, relief="ridge")
mallaDeLabels.grid(row=2, column=0)

LabelInformacion = Label(mallaDeLabels,text="Informacion del Producto")
LabelInformacion.grid(row=5, column=0)
labelNombre = Label(mallaDeLabels, text="Nombre del Producto:")
labelNombre.grid(row=6, column=0, padx=100)
labelId = Label(mallaDeLabels, text="Id Del Producto")
labelId.grid(row=7, column=0)
labelPrecio = Label(mallaDeLabels, text="Precio del Producto")
labelPrecio.grid(row=8, column=0)
labelCantidad = Label(mallaDeLabels, text="Cantidad del Producto")
labelCantidad.grid(row=9, column=0)

#============================================



#=============================================

def SelecProducto(event):
        i =listBoxProductos.curselection()[0]
        producto = surcursal_provisoria.productos[i]
        print(f"Nombre {producto.nombre}, Id: {producto.id} Precio: {producto.precio}, Stock: {producto.stock} ")
        labelNombre.config(text=f"Nombre del Producto: {producto.nombre}")
        labelId.config(text=f"Id del Producto: {producto.id}")
        labelPrecio.config(text=f"Precio del Producto: {producto.precio}")
        labelCantidad.config(text=f"Stock del Producto: {producto.stock}")

#===========================================
for producto in surcursal_provisoria.productos:
      listBoxProductos.insert(END, producto.nombre)

listBoxProductos.bind("<<ListboxSelect>>", SelecProducto)

 
ventana.mainloop()
