i = 0

# while i <= 10:
#     print(i)
#     # i = i + 1
#     i += 1

# Break

# while i <= 10:
#     print(i)
#     if i == 5:
#         break
#     i += 1

while i <= 10:
    i += 1
    if i == 5:
        continue
    print(i)

personas = ["Juan", "Pedro", "María"]

for persona in personas:
    print(persona)

persona = "Juan"

for c in persona:
    print(c)

personas = ["Juan", "Pedro", "Felipe", "Juana"]

for persona in personas:
    if persona == "Felipe":
        break
    print(persona)

personas = ["Juan", "Pedro", "Felipe", "Juana"]

for persona in personas:
    if persona == "Felipe":
        continue
    print(persona)

for x in range(10, 20, 2):
    print(x)

for x in range(10, 20, 2):
    print(x)
else:
    print("Se ha terminado la ejecución")

personas = ["Juan", "María", "Pedro", "Luis"]
edades = [5, 27, 14, 35]

for persona in personas:
    for edad in edades:
        print(persona, edad)