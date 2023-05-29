class Padre:

    def __init__(self, nombre) -> None:
        self.nombre = nombre

class Hijo(Padre):

    def __init__(self, nombre, profesion) -> None:
        super().__init__(nombre)
        self.profesion = profesion

Jorge = Hijo("Jorge", "Albañil")
Maria = Hijo("Maria", "Modista")

