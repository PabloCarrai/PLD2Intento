def salir():
    exit()


def validarEleccionMCliente(eleccion):
    if (eleccion == 1):
        print("Alta Cliente")
    elif (eleccion == 2):
        print("Baja Cliente")
    elif (eleccion == 3):
        print("Modificacion Cliente")
    elif (eleccion == 4):
        salir()


def menuFactura():
    pass


def menuProducto():
    pass


def menuCliente():
    print("""
    1) Alta Cliente
    2) Baja Cliente
    3) Modificacion Cliente
    4) Salir
    """)
    eleccion = int(input("Ingrese una opcion"))
    validarEleccionMCliente(eleccion)


def validarEleccion():
    eleccion = int(input("Elija una opcion"))
    while (eleccion < 1 or eleccion > 4):
        eleccion = int(input("Elija una opcion valida"))
    if (eleccion == 1):
        menuCliente()
    elif (eleccion == 2):
        menuProducto()
    elif (eleccion == 3):
        menuFactura()
    elif (eleccion == 4):
        salir()


def menuPrincipal():
    print("""
    1) ABM Cliente
    2) ABM Producto
    3) ABM Factura
    4) Salir
    """)
    validarEleccion()


menuPrincipal()
