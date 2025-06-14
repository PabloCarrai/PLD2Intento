nombres = []
apellidos = []
dnis = []
telefonos = []
direcciones = []


def salir():
    exit()


def edicionCliente():
    listadoCliente(0)
    eleccion = int(input("Ingrese un id valido "))
    nombre = input("Nombre?  ")
    apellido = input("Apellido? ")
    dni = input("DNI? ")
    telefono = input("Telefono? ")
    direccion = input("Direccion? ")
    nombres[eleccion] = nombre
    apellidos[eleccion] = apellido
    direcciones[eleccion] = dni
    dnis[eleccion] = telefono
    telefonos[eleccion] = direccion
    print("Cliente editado ")
    menuCliente()


def bajaCliente():
    listadoCliente(0)
    eleccion = int(input("Ingrese un id valido "))
    del (nombres[eleccion])
    del (apellidos[eleccion])
    del (direcciones[eleccion])
    del (dnis[eleccion])
    del (telefonos[eleccion])
    menuCliente()


def listadoCliente(valor):
    print("Clientes: ")
    for x in range(len(nombres)):
        print(f"""
          Id: {x}    
          Nombre: {nombres[x]}  Apellido: {apellidos[x]}
          Direccion: {direcciones[x]}
          DNI: {dnis[x]} Telefono: {telefonos[x]}              
              """)
    if (valor == 1):
        menuCliente()


def altaCliente():
    print("Bienvenido ")
    ccc = int(input("Cuantos clientes quiere cargar? "))
    for i in range(ccc):
        nombre = input("Nombre?  ")
        apellido = input("Apellido? ")
        dni = input("DNI? ")
        telefono = input("Telefono? ")
        direccion = input("Direccion? ")
        nombres.append(nombre)
        apellidos.append(apellido)
        dnis.append(dni)
        telefonos.append(telefono)
        direcciones.append(direccion)
        print("Carga Realizada ")
        menuCliente()


def validarEleccionMCliente(eleccion):
    while (eleccion < 1 or eleccion > 6):
        eleccion = int(input("Elija una opcion valida"))
    if (eleccion == 1):
        print("Alta Cliente")
        altaCliente()
    elif (eleccion == 2):
        print("Baja Cliente")
        bajaCliente()
    elif (eleccion == 3):
        print("Modificacion Cliente")
        edicionCliente()
    elif (eleccion == 4):
        print("Listado de Cliente")
        listadoCliente(1)
    elif (eleccion == 5):
        print("Volver al menu Principal")
        menuPrincipal()
    elif (eleccion == 6):
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
    4) Listado de Cliente
    5) Volver al menu Principal
    6) Salir
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
