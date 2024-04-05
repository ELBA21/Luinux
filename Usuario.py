class Usuario:
    def __init__(self, nombre_usuario, sucursales, password):
        self.nombre_usuario = nombre_usuario
        self.sucursales = sucursales
        self.password = password
    ## getters y setters nya
    ## leo eri pollo 2 commits
    def __get_nombre_usuario__(self):
        return self.nombre_usuario

    def __get_sucursales__(self):
        return self.sucursales
    ## no voy a haceer un getter pa la password porque no suena seguro
    def __set_nombre_usuario__(self, nombre_usuario):
        self.nombre_usuario = nombre_usuario

    def __set_sucursales__(self, sucursales):
        self.sucursales = sucursales

    def __set_password__(self, password):
        self.password = password
    
    def crear_sucursal(self):
        print("no hay protected en piton asi que la dejare public por mientras")

