primerNumero = input("Ingrese el primer número: ")

try:
    primero = int(primerNumero)
except:
    primero = "Cadena"

if primero == "Cadena":
    print("El valor ingresado no es un entero")
    exit()

segundoNumero = input("Ingrese el segundo número: ")

try:
    segundo = int(segundoNumero)
except:
    segundo = "Cadena"

if segundo == "Cadena":
    print("El valor ingresado no es un entero")
    exit()

simbolo = input("Ingrese la operacion: ")

if simbolo == "+":
    print("Suma: ", primero + segundo)
elif simbolo == "-":
    print("Resta: ", primero - segundo)
elif simbolo == "*":
    print("Multiplicacion: ", primero * segundo)
elif simbolo == "/":
    print("Division: ", primero / segundo)
else:
    print("El simbolo ingresado no es valido")