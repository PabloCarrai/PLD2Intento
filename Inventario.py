def menuCliente():
    print("""
    1) Alta Cliente
    2) Baja Cliente
    3) Modificacion Cliente
    4) Salir      
    """)
    eleccion = int(input("Ingrese una opcion"))
    validarOpcion(eleccion)


def moverseMenu(eleccion):
    if (eleccion == 1):
        menuCliente()
    elif (eleccion == 2):
        pass
    elif (eleccion == 3):
        pass
    elif (eleccion == 4):
        pass


def validarOpcion(eleccion):
    while (eleccion < 1 or eleccion > 4):
        eleccion = int(input("Ingrese una opcion Valida"))
    moverseMenu(eleccion)


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
