from Productos import Productos
from tkinter import *

class Sucursal:
    def __init__(self, nombre, ventana_sucursal):
        self.productos = []
        self.nombre = nombre
        self.ventana_sucursal = ventana_sucursal

    def get_nombre(self, nombre):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def agregar_productos(self, nombre_producto, precio_venta, precio_compra, stock_producto):
        x = False
        def confirm_ppp():
            confirm_ppp_w = Toplevel(self.ventana_sucursal)
            confirm_ppp_w.title("Confirmacion PPP")
            confirm_ppp_w.geometry("400x200") # me gustaria usar 480x240 pero este es el standard de este programa
            confirm_ppp_w.grab_set()

            ppp_label = Label(confirm_ppp_w, text="¿Usar PPP?")
            ppp_label.pack()

            ppp_button_grid = Frame(confirm_ppp_w, bd=16)
            ppp_button_grid.pack()
            b = None
            def confirm(a):
                nonlocal b
                b = a
                print(b)
                confirm_ppp_w.destroy()
                return b

            ppp_button_yes = Button(ppp_button_grid, text="Si", command=lambda: confirm(True))
            ppp_button_yes.grid(row=0, column=0)
            ppp_button_no = Button(ppp_button_grid, text="No", command=lambda: confirm(False))
            ppp_button_no.grid(row=0, column=1)
            
            confirm_ppp_w.wait_window(confirm_ppp_w)
            return b

        for producto in self.productos: #este for es para que no se cree un segundo objeto con el mismo nombre 
            print(producto.get_nombre() + " obj")
            if producto.get_nombre() == nombre_producto:
                if (producto.get_precio_venta() != precio_compra or producto.get_precio_venta() != precio_venta):
                    print("Promedio precio ponderado")
                    selection = confirm_ppp()
                    if selection:
                        precio_final = ((producto.get_stock()*producto.get_precio_venta())+(stock_producto*precio_compra))/(producto.get_stock()+stock_producto)
                        producto.set_precio_venta(int(precio_final))
                    else:
                        producto.set_precio_venta(precio_venta)
                precio_compra_final = ((producto.get_stock()*producto.get_precio_compra())+(stock_producto*precio_compra))/(producto.get_stock()+stock_producto)
                producto.actualizar_stock(stock_producto)
                x = True # si x es verdadera no se creara un objeto y se aplicara la funcion del precio
            break
        if x == False: # si x sigue siendo false se creara un objeto
            globals()[str(nombre_producto) + "_objeto"] = Productos(nombre_producto, None, precio_venta, precio_compra, stock_producto)
            globals()[str(nombre_producto) + "_objeto"].set_autoid
            self.productos.append(globals()[str(nombre_producto) + "_objeto"])
            

    def get_productos(self, value):
        return self.productos[value]

    def eliminar_productos(self, value):
        self.productos.pop(value)

    def get_tamano(self): #retorna el tamano de la lista
        return len(self.productos)