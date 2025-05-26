# Inicialización de listas
nombres = []
promedios = []
estados = []

# Ingreso de la cantidad de estudiantes
cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))

# Bucle principal para cada estudiante
for i in range(cantidad_estudiantes):
    print(f"\nEstudiante #{i + 1}")
    nombre = input("Ingrese el nombre del estudiante: ")
    nombres.append(nombre)

    # Ingreso de notas
    cantidad_notas = int(input(f"Ingrese cuántas notas desea ingresar para {nombre}: "))
    suma_notas = 0

    for j in range(cantidad_notas):
        nota = float(input(f"Ingrese la nota #{j + 1}: "))
        suma_notas += nota

    # Cálculo del promedio
    promedio = suma_notas / cantidad_notas
    promedios.append(promedio)

    # Determinación de estado
    if promedio >= 3.0:
        estado = "Aprobado"
    else:
        estado = "Reprobado"
    estados.append(estado)

# Mostrar resultados finales
print("\n--- RESULTADOS FINALES ---")
for i in range(cantidad_estudiantes):
    print(f"{nombres[i]} - Promedio: {promedios[i]:.2f} - Estado: {estados[i]}")
