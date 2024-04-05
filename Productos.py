class Productos:
    def __init__(self, nombre, id, precio):
        self.nombre = nombre
        self.id = id
        self.precio = precio
    
    #Getters
    def __get_nombre__(self):
        return self.nombre

    def __get_id__(self):
        return self.id

    def __get_precio__(self):
        return self.precio
    
    #Setters
    def __set_nombre__(self, nombre):
        self.nombre = nombre

    def __set_id__(self, id):
        self.id = id

    def __set_precio__(self, precio):
        self.precio = precio     