print ("Hola Mundo")

--------------------------------------------------------

a = int
b = int

def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    if b == 0:
        return "Error: Division por cero"
    return a / b
print("Selecciona una operación: 1. Suma 2. Resta 3. Multiplicación 4. División")
opcion = input("Ingresa el número de la operación: ")
if opcion == '1':
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    print(f"La suma es: {suma(a, b)}")
elif opcion == '2':
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    print(f"La resta es: {resta(a, b)}")
elif opcion == '3':
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    print(f"La multiplicación es: {multiplicacion(a, b)}")
elif opcion == '4':
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    print(f"La división es: {division(a, b)}")


--------------------------------------------------------

edad = int(input("ingresa tu edad: "))
if edad >= 18:
    print("Eres mayor de edad puedes votar")
else:
    print("Eres menor de edad no puedes votar")

--------------------------------------------------------

nombres = ["Rigo","Rosa","David","Angelica","Helena"]
for nombre in nombres:
    print(f"Hola, {nombre}!")

--------------------------------------------------------

numero = 1
while numero <= 5:
    print(numero)
    numero += 1

--------------------------------------------------------

def saludar(nombre):
    print(f"Hola, {nombre} Como Estas?")

usuario = input("Ingrese su nombre: ")
saludar(usuario)

--------------------------------------------------------

def calcular_promedio(calificaciones):
    if len(calificaciones) == 0:
        return 0
    suma = sum(calificaciones)
    promedio = suma / len(calificaciones)
    return promedio

notas = [3.5, 4.0, 2.8, 5.0]
prom = calcular_promedio(notas)
print(f"El promedio de las calificaciones es: {prom:.0f}")
