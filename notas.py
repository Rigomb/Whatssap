nombres = []
promedios = []
estados = []

cantidad_estudiantes = int(input("Ingrese el Numero de estudiantes: "));

for i in range(cantidad_estudiantes):
    print(f"\nEstudiante #{i + 1}")
    nombre = input("Ingrese el nombre del estudiante: ")
    nombres.append(nombre)

    cantidad_notas = int(input(f"Ingrese cuántas notas desea ingresar para {nombre}: "))
    suma_notas = 0

    for j in range(cantidad_notas):
        nota = float(input(f"Ingrese la nota #{j + 1}: "))
        suma_notas += nota

    promedio = suma_notas / cantidad_notas
    promedios.append(promedio)

    if promedio >= 3.0:
        estado = "Aprobado"
    else:
        estado = "Reprobado"
    estados.append(estado)

print("\n--- RESULTADOS FINALES ---")
for i in range(cantidad_estudiantes):
    print(f"{nombres[i]} - Promedio: {promedios[i]:.2f} - Estado: {estados[i]}")