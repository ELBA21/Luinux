from tkinter import *
from Productos import Productos
from Sucursal import Sucursal

test_sucursal = Sucursal(1)
test_sucursal.set_nombre("leo pollo")
nombre1 = input()
precio1 = input()
print("\n")
test_sucursal.agregar_productos(nombre1, precio1, 69)
print(test_sucursal.get_productos(0).get_nombre())
print(test_sucursal.get_productos(0).get_precio())
test_sucursal.get_productos(0).set_autoid()
print(test_sucursal.get_productos(0).get_id())

#print(globals()[str(nombre) + "_objeto"].get_nombre())
#print(globals()[str(nombre) + "_objeto"].get_precio())
#print(globals()[str(nombre) + "_objeto"].get_id())