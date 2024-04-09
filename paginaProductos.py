from tkinter import *
class testeoProducto:
    def __init__(self, nombre, id, precio, stock):
        self.nombre = nombre
        self.id = id
        self.precio = precio
        self.stock = stock
def cargarProductos():
        arrayDeTesteo = [
            testeoProducto("Ramen: Rojo","01",790,4),
            testeoProducto("Ramen: Naranja","02",790,2),
            testeoProducto("Ramen: Verde","03",790,1),
            testeoProducto("Ramen: Negro","04",790,0),
            testeoProducto("Redbull","51",2000,2),
            testeoProducto("Pepsi","52",1700,4),
            testeoProducto("Kem Extreme","531",1700,1),
            testeoProducto("Kem","53",1500,3)
        ]
        return arrayDeTesteo
    
#===================== Crear la ventana principal
ventana = Tk()
ventana.title("Lista de Productos")
#====================================

#=======================Elementos extra
mallaPrincipal = Frame(ventana, bd=2,relief="ridge")
mallaPrincipal.pack(padx=1, pady=1)
lista = Listbox(mallaPrincipal, width=50, height=10)
lista.pack(padx=10, pady=10)
LabelInformacion = Label(mallaPrincipal,text="Informacion del Producto")
LabelInformacion.pack(padx=5)

labelNombre = Label(mallaPrincipal, text="Nombre del Producto:")
labelNombre.pack(anchor=W)
labelId = Label(mallaPrincipal, text="Id Del Producto")
labelId.pack(anchor=W)
labelPrecio = Label(mallaPrincipal, text="Precio del Producto")
labelPrecio.pack(anchor=W)
labelCantidad = Label(mallaPrincipal, text="Cantidad del Producto")
labelCantidad.pack(anchor=W)

#============================================

listaDeProductos = cargarProductos()
#=============================================
def SelecProducto(event):
        i =lista.curselection()[0]
        producto = listaDeProductos[i]
        print(f"Nombre {producto.nombre}, Id: {producto.id} Precio: {producto.precio}, Stock: {producto.stock} ")
        labelNombre.config(text=f"Nombre: {producto.nombre}")
        labelId.config(text=f"Nombre: {producto.id}")
        labelPrecio.config(text=f"Nombre: {producto.precio}")
        labelCantidad.config(text=f"Nombre: {producto.stock}")

#===========================================
for producto in listaDeProductos:
      lista.insert(END, producto.nombre)

lista.bind("<<ListboxSelect>>", SelecProducto)

 
ventana.mainloop()
