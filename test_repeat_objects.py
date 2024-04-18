from Sucursal import Sucursal
from Productos import Productos

surcursal_provisoria = Sucursal("pene")

surcursal_provisoria.agregar_productos("pepsi",1000, 1000, 20)
surcursal_provisoria.get_productos(0).set_autoid()

surcursal_provisoria.agregar_productos("pepsi",1500, 1500, 80)
surcursal_provisoria.get_productos(0).set_autoid()

surcursal_provisoria.agregar_productos("ramen",1000, 1000, 20)
surcursal_provisoria.get_productos(1).set_autoid()

print(surcursal_provisoria.get_productos(0).get_nombre())
print(surcursal_provisoria.get_productos(0).get_precio_venta())
print(surcursal_provisoria.get_productos(1).get_nombre())
print(surcursal_provisoria.get_productos(1).get_precio_venta())
