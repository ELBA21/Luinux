from tkinter import *
from Productos import Productos
from Sucursal import Sucursal
import Agregar
import Editar
##Cosas temporales


#===================== Crear la ventana principal
root = Tk()
root.geometry("480x480")
root.title("Lista de Productos")
#====================================

surcursal_provisoria = Sucursal(1)
surcursal_provisoria.productos = {}

#=========================Metodo para botones
def abrirAgregar():
       Agregar.abrirAgregar(root, surcursal_provisoria, listBoxProductos) #Insertamos las clases a llamar en los metodos
                                                                             #Asi evitamos importaciones circulares
def abrir_Editar():
       Editar.abrir_Editar(root, surcursal_provisoria, listBoxProductos, elemento_selecionado)

def elemento_selecionado():
       if listBoxProductos.curselection():
              i = listBoxProductos.curselection()[0]
              return i
       else:
              return -1
def eliminar_Producto():
       if listBoxProductos.curselection():
              i = listBoxProductos.curselection()[0]
              surcursal_provisoria.eliminar_producto(i)
              listBoxProductos.delete(i)


#=======================Malla para organizar
frame_0 = Frame(root)
frame_0.pack()
frame_listbox = Frame(root)
frame_listbox.pack(pady=(50,10))
frame_botones = Frame(root)
frame_botones.pack()
frame_1 = Frame(root)
frame_1.pack()
#=============================================================


                #==========================Elementos de la malla
                #=======================================

lbl_iniciar = Label(frame_0, text="PRODUCTOS", font="Helvetica 15")
lbl_iniciar.pack(pady=(70,0))
#================ListBox=====
listBoxProductos = Listbox(frame_listbox, width=50, height=10, borderwidth=1, relief="solid")
listBoxProductos.pack()
#==========================



#==============================Botones
mallaDeBotones = Frame(frame_botones, bd=2)
mallaDeBotones.grid(row=1, column=0)
botonAgregar = Button(mallaDeBotones, text="Agregar", command=abrirAgregar, bg= "lightgrey", borderwidth=1, relief="solid")
botonAgregar.grid(row=0,column=0, padx=4)
botonEditar = Button(mallaDeBotones, text="Editar", command= abrir_Editar, bg= "lightgrey", borderwidth=1, relief="solid")
botonEditar.grid(row=0, column=1, padx=4)
BotonEliminar = Button(mallaDeBotones, text="Eliminar", command= eliminar_Producto, bg= "lightgrey", borderwidth=1, relief="solid")
BotonEliminar.grid(row=0, column=2, padx=4)
BotonVender = Button(mallaDeBotones, text="Vender", bg= "lightgrey", borderwidth=1, relief="solid")
BotonVender.grid(row=0, column=3, padx=4)

#=======================================

#===================Labels De Informacion
mallaDeLabels = Frame(frame_1, borderwidth=1, relief="solid")
mallaDeLabels.grid(row=2, column=0, pady=10)

LabelInformacion = Label(mallaDeLabels,text="Información del Producto:")
LabelInformacion.grid(row=5, column=0)
labelNombre = Label(mallaDeLabels, text="Nombre del Producto:")
labelNombre.grid(row=6, column=0, padx=100)
labelId = Label(mallaDeLabels, text="ID del Producto")
labelId.grid(row=7, column=0)
labelPrecio = Label(mallaDeLabels, text="Precio del Producto:")
labelPrecio.grid(row=8, column=0)
labelCantidad = Label(mallaDeLabels, text="Cantidad del Producto:")
labelCantidad.grid(row=9, column=0)

#============================================



#=============================================



def SelecProducto(event):
       boolvar = listBoxProductos.curselection()
       if boolvar:
              i =listBoxProductos.curselection()[0]
              producto = surcursal_provisoria.get_producto(i)
              print(f"Nombre {producto.nombre}, Id: {producto.id} Precio: {producto.precio_venta}, Stock: {producto.stock} ")
              labelNombre.config(text=f"Nombre del Producto: {producto.nombre}")
              labelId.config(text=f"Id del Producto: {producto.id}")
              labelPrecio.config(text=f"Precio del Producto: {producto.precio_venta}")
              labelCantidad.config(text=f"Stock del Producto: {producto.stock}")
       else:
              print("No hay nada seleccionado")

surcursal_provisoria.productos[0] = Productos("Producto 1", 555, 10.0, 5.0, 100)
surcursal_provisoria.productos[1] = Productos("Producto 2", 2, 20.0, 10.0, 50)
surcursal_provisoria.productos[2] = Productos("Producto 3", 3, 30.0, 15.0, 200)

#===========================================
for key, producto in surcursal_provisoria.productos.items():
      listBoxProductos.insert(END, producto.nombre)

listBoxProductos.bind("<<ListboxSelect>>", SelecProducto)

 
root.mainloop()
