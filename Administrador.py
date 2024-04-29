class Administrador:
    def __init__(self):
        self.usuarios = {}

    def registrarUsuario(self, usuario):
        self.usuarios[usuario.nombre_usuario] = usuario

    def eliminarUsuario(self, usuario):
        del self.usuarios[usuario.nombre_usuario]

    def mostrarUsuarios(self):
        for _, usuario in self.usuarios.items():
            print("Usuario: "+ usuario.nombre_usuario + ", contraseña: " + usuario.password)
