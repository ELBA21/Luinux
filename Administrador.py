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

    def cambiar_nombre_usuario(self, nuevo_nombre, antiguo_nombre):
        if nuevo_nombre in self.usuarios:
            print("Es el mismo nombre que ya existe")
        else:
            self.usuarios[nuevo_nombre] = self.usuarios.pop(antiguo_nombre)
            self.usuarios[nuevo_nombre].set_nombre(nuevo_nombre)
    
    def to_dict(self):
        return {
            "usuarios": {usuario.get_nombre_usuario(): usuario.to_dict() for usuario in self.usuarios.values()}
        }
