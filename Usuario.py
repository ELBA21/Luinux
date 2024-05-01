from Sucursal import Sucursal
class Usuario:
    def __init__(self, nombre_usuario, password):
        self.nombre_usuario = nombre_usuario
        self.sucursales = {}
        self.password = password

    def get_nombre_usuario(self):
        return self.nombre_usuario

    def get_sucursal(self, nombre):
        return self.sucursales[nombre]
    
    def get_password(self):
        return self.password
    
    def set_nombre(self, nombre):
        self.nombre_usuario = nombre

    def set_password(self, password): 
        self.password = password
    
    def crear_sucursal(self, nombre):
        if nombre in self.sucursales:
            print("Ya existe una sucursal con ese nombre")
        else:
            self.sucursales[nombre] = Sucursal(nombre)

    def eliminar_sucursal(self, nombre):
        if nombre in self.sucursales:
            del self.sucursales[nombre]
        else:
            print("No existe ese, chaval")

    def cambiar_nombre_sucursal(self, nuevo_nombre, antiguo_nombre):
        if nuevo_nombre in self.sucursales:
            print("Nombre ya registrado")
        else:
            self.sucursales[nuevo_nombre] = self.sucursales.pop(antiguo_nombre)
            self.sucursales[nuevo_nombre].set_nombre(nuevo_nombre)

    def to_dict(self):
        return {
            "nombre_usuario": self.nombre_usuario,
            "password": self.password,
            "sucursales": {sucursal.get_nombre(): sucursal.to_dict() for sucursal in self.sucursales.values()}
        }