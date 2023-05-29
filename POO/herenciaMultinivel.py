class Abuelo:
    
    def __init__(self, nombre) -> None:
        self.nombre = nombre

class Padre(Abuelo):

    def __init__(self, nombre, profesion) -> None:
        super().__init__(nombre)
        self.profesion = profesion
    
    def habilidad(self):
        return f"Yo puedo cantar"

class Hijo(Padre):
    
    def __init__(self, nombre, profesion) -> None:
        super().__init__(nombre, profesion)

Juan = Hijo("Juan", "Programador")
print(Juan.nombre)
print(Juan.habilidad())
print(Juan.profesion)