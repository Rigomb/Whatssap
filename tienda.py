productos = {}
ventas_mensuales = {
    "enero": 0, "febrero": 0, "marzo": 0, "abril": 0,
    "mayo": 0, "junio": 0, "julio": 0, "agosto": 0,
    "septiembre": 0, "octubre": 0, "noviembre": 0, "diciembre": 0
}

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad actual: "))
    if nombre in productos:
        productos[nombre] += cantidad
    else:
        productos[nombre] = cantidad
    print(f"Producto '{nombre}' actualizado. Total: {productos[nombre]}")

def vender_producto():
    nombre = input("Ingrese el nombre del producto a vender: ")
    if nombre in productos:
        cantidad = int(input("Ingrese la cantidad a vender: "))
        if productos[nombre] >= cantidad:
            productos[nombre] -= cantidad
            mes = input("Ingrese el mes de la venta (en minúsculas): ")
            if mes in ventas_mensuales:
                ventas_mensuales[mes] += cantidad
                print("Venta registrada.")
            else:
                print("Mes no válido.")
        else:
            print("No hay suficiente stock.")
    else:
        print("Producto no encontrado.")

def mostrar_inventario():
    print("\n--- Inventario actual ---")
    for nombre, cantidad in productos.items():
        print(f"{nombre}: {cantidad} unidades")

def mostrar_ventas_mensuales():
    print("\n--- Ventas mensuales ---")
    for mes, total in ventas_mensuales.items():
        print(f"{mes.capitalize()}: {total} productos vendidos")

def menu_usuario():
    while True:
        print("\n--- MENÚ DE USUARIO ---")
        print("1. Agregar producto")
        print("2. Vender producto")
        print("3. Mostrar inventario")
        print("4. Mostrar ventas mensuales")
        print("5. Distribuir productos a tiendas anexas")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            vender_producto()
        elif opcion == "3":
            mostrar_inventario()
        elif opcion == "4":
            mostrar_ventas_mensuales()
        elif opcion == "5":
            print("Distribuyendo productos a tiendas anexas...")
        elif opcion == "6":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            
menu_usuario()
