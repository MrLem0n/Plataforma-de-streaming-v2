class contenido():
    def __init__(self,id,nombre,descripcion,tipo,duracion,categoria,popularidad):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.tipo = tipo
        self.duracion = duracion
        self.categoria = categoria
        self.popularidad = popularidad
    
    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.descripcion} - {self.tipo} - {self.duracion} - {self.categoria} - {self.popularidad}"

class Pelicula(contenido):
    def __init__(self,id,nombre,descripcion,tipo,duracion,categoria,popularidad):
        super().__init__(id,nombre,descripcion,tipo,duracion,categoria,popularidad)
    
    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.descripcion} - {self.tipo} - {self.duracion} - {self.categoria} - {self.popularidad}"

class Serie(contenido):
    def __init__(self,id,nombre,descripcion,tipo,duracion,categoria,popularidad):
        super().__init__(id,nombre,descripcion,tipo,duracion,categoria,popularidad)
    
    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.descripcion} - {self.tipo} - {self.duracion} - {self.categoria} - {self.popularidad}"

class Usuario():
    def __init__(self,id,nombre,email,contraseña,historial):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.contraseña = contraseña
        self.historial = historial
    
    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.email} - {self.contraseña} - {self.historial}"

    def ver_historial(self):
        for contenido in self.historial:
            print(contenido)