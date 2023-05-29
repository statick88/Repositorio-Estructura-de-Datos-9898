class Monster:
    
    def __init__(self, nombre, categoria):
        self.nombre = nombre
        self.categoria = categoria

    def __str__(self):
        return f"Soy {self.nombre} y mi categoria es {self.categoria}"
    
    def myFunc(self):
        print("Hey, soy un " + self.nombre )

mounstrito = Monster("Sullivan", "Asustador")
print(mounstrito.nombre)
print(mounstrito)
mounstrito.myFunc()