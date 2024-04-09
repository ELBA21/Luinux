class Usuario:
    def __init__(self, nombre_usuario, sucursales, password):
        self.nombre_usuario = nombre_usuario
        self.sucursales = sucursales
        self.password = password
    ## getters y setters nya
    ## leo eri pollo 2 commits
    def get_nombre_usuario(self):
        return self.nombre_usuario

    def get_sucursales(self):
        return self.sucursales
    
    def get_password(sefl):
        return self.password
        
    def set_nombre_usuario(self, nombre_usuario):
        self.nombre_usuario = nombre_usuario

    def set_sucursales(self, sucursales):
        self.sucursales = sucursales

    def set_password(self, password):
        self.password = password
    
    def crear_sucursal(self):
        print("no hay protected en piton asi que la dejare public por mientras")


