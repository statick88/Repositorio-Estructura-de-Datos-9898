#Listas

lista = []

print(type(lista))

lista = ["Ecuador", "Colombia", "Brasil"]
print(lista)

lista = ["Juan", 45, 6.5, True, ["Ecuador", "Colombia", "Brasil"], "a"]
print(lista)

#Metodos de la Lista

lista = ["Ecuador", "Colombia", "Brasil"]
lista.append("Mexico")
print(lista)

lista2 = lista.copy()
print(lista2)

lista2.clear()
print(lista2)

lista2 = lista.copy()
print(lista2.count("Colombia"))
lista2.append("Bolivia")
lista2.append("Colombia")
print(lista2.count("Colombia"))
print(lista2)

print(len(lista2))

print(lista2[4])

lista2[5] = "Peru"
print(lista2)

#Eliminar elementos de una lista

lista2.pop()
print(lista2)

lista2.remove("Brasil")
print(lista2)

lista2.reverse()
print(lista2)

lista2.sort()
print(lista2)

lista3 = ["d","B", "b", "c"]
lista3.sort()
print(lista3)

#Tuplas

tupla = ()
print(type(tupla))

"""tupla.append("Diego")
print(tupla)"""

tupla2 = ("Juan", "Pedro", "Maria", "Juan")
print(tupla2)

print(tupla2.count("Juan"))
print(tupla2.index("Maria"))
# print(tupla2.index("😒"))

print(tupla2[2])
print(tupla2[3])

lista = list(tupla2)
print(type(lista))

lista.append("Mario")
print(lista)

tupla2 = tuple(lista)
print(tupla2)

# Range

rango = range(6)
print(rango)

# Set

set = {2, 3, 4, 5,6,6}
print(set)
print(type(set))

#Diccionarios

cliente001 = {
    "Nombre":"Diego",
    "Cedula": 1104529863,
    "Celular": "099362162",
    "Correo": "dmsaavedra@espe.edu.ec"
}

print(cliente001)
print(type(cliente001))

print(cliente001["Correo"])
print(cliente001.get("Celular"))

cliente001["Nombre"] = "Juan"
print(cliente001.get("Nombre"))
print(cliente001)

print(len(cliente001))

cliente001["estadoCivil"] = "Viudo"
print(cliente001)

cliente001.popitem()
print(cliente001)

cliente001.pop("Celular")
print(cliente001)

del cliente001["Cedula"]
print(cliente001)

cliente002 = dict(cliente001)
print(cliente001)
print(cliente002)

perros = {
    "Tobby":{
    "name": "Tobby",
    "age": 6
    },
    "Leo":{
    "name": "Leo",
    "age": 1
    }
}
print(perros)

Rocky = dict(name="Rocky", age=7)
print(Rocky)

perros["Rocky"] = Rocky
print(perros)

# Boolean

nacidoVivo = True
agenteCredito = False

print(type(nacidoVivo))
print(type(agenteCredito))

print(2>5)