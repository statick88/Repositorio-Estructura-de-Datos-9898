

class Perro:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self) -> str:
        return f"{self.nombre} es un perro que tiene {self.edad} años"
    
    def moder(self):
        return f"Yo soy {self.nombre} y muerdo fuerte"
    
    def ladrar(self):
        return f"Yo soy {self.nombre} y puedo ladrar"
    

perro1 = Perro("Rocky", 3)
print(perro1)
print(perro1.edad)
print(perro1.ladrar())
