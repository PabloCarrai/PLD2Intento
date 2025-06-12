def validarOpcion(eleccion):
    while (eleccion < 1 or eleccion > 4):
        eleccion = int(input("Ingrese una opcion Valida"))
    print(f"Opcion Valida {eleccion}")


def mostrarMenu():
    print("Bienvenido")
    print("""
    1) ABM Cliente
    2) ABM Producto
    3) ABM Factura
    4) Salir
    """)
    eleccion = int(input("Ingrese una opcion"))
    validarOpcion(eleccion)


mostrarMenu()
