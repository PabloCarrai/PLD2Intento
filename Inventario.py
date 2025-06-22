#   Importamos modulo os para limpiar pantalla
import os


#   Listas necesarias para el ABM del cliente
nombres = []
apellidos = []
dnis = []
telefonos = []
direcciones = []
#   Listas necesarias para el ABM del Producto
nproductos = []
stockproductos = []
precioproductos = []
#   Lista necesarias para el ABM de la Factura
facturas = []
ffacturas = []
#   Lista con todo lo que tiene la Factura
# facturaFull = []
facturaElementos = []
facturaCompras = []
totales = []


def limpiarPantalla():
    """
    Limpiamos la pantalla dependiendo del SO
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def salir():
    """
    Funcion para salir del programa
    """
    exit()


def validarIndice(lista):
    """
    La eleccion es el indice que se usa en las listas
    Las Listas contienen los datos que trabajamos. 
    Esto es para evitar que alguien elija un indice 
    de una lista inexistente en cuanto a sus elementos
    """
    eleccion = int(input("Ingrese un id valido "))
    while (eleccion not in range(len(lista))):
        eleccion = int(input("Ingrese un id valido(existente) "))
    return eleccion


def edicionFactura():
    """
    Edicion de factura
    """
    listadoFactura(0)
    eleccion = validarIndice(facturas)
    factura = input("Codigo? ")
    ffactura = input("Fecha? ")
    facturas[eleccion] = factura
    ffacturas[eleccion] = ffactura
    print("Factura editado ")
    menuFactura()


def edicionProducto():
    """
    Edicion de producto
    """
    listadoProducto(0)
    eleccion = validarIndice(nproductos)
    nproducto = input("Nombre?  ")
    sproducto = int(input("Stock? "))
    pproducto = int(input("Precio? "))
    nproductos[eleccion] = nproducto
    stockproductos[eleccion] = sproducto
    precioproductos[eleccion] = pproducto
    print("Producto editado ")
    menuProducto()


def edicionCliente():
    """
    Edicion de cliente
    """
    listadoCliente(0)
    eleccion = validarIndice(nombres)
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


def bajaFactura():
    """
    Funcion para eliminar un Factura
    """
    #   Aca listamos producto sin ir al menu luego del listado
    listadoFactura(0)
    eleccion = validarIndice(facturas)
    del (facturas[eleccion])
    del (ffacturas[eleccion])
    menuFactura()


def bajaProducto():
    """
    Funcion para eliminar un producto
    """
    #   Aca listamos producto sin ir al menu luego del listado
    listadoProducto(0)
    eleccion = validarIndice(nproductos)
    del (nproductos[eleccion])
    del (stockproductos[eleccion])
    del (precioproductos[eleccion])
    menuProducto()


def bajaCliente():
    """
    Funcion para eliminar un cliente
    """
    #   Aca listamos cliente sin ir al menu luego del listado
    listadoCliente(0)
    eleccion = validarIndice(nombres)
    del (nombres[eleccion])
    del (apellidos[eleccion])
    del (direcciones[eleccion])
    del (dnis[eleccion])
    del (telefonos[eleccion])
    menuCliente()


def listadoCompra(valor):
    """
    Aca procedemos a mostrar las compras
    """
    print("Compras: ")
    for x in facturaElementos:
        for i in x:
            print(f"{i} ")
    for e in facturaCompras:
        for x in e:
            for i in x:
                print(i)
    for i in totales:
        print(f"Total Gastado ${i}")
    totales.clear()
    facturaElementos.clear()
    facturaCompras.clear()
    #   Aca puede suceder que no necesitemos si o si ir al menu factura
    #   Si pasamos como valor 1 vamos al menu factura, sino no
    if (valor == 1):
        menuCompra()


def listadoFactura(valor):
    """
    Aca procedemos a mostrar las facturas
    """
    print("Facturas: ")
    for x in range(len(facturas)):
        print(f"""
         Id: {x}
           Codigo: {facturas[x]}  
          Fecha: {ffacturas[x]}
        """)
    #   Aca puede suceder que no necesitemos si o si ir al menu factura
    #   Si pasamos como valor 1 vamos al menu factura, sino no
    if (valor == 1):
        menuFactura()


def listadoProducto(valor):
    """
    Aca procedemos a mostrar los productos
    """
    print("Productos: ")
    for x in range(len(nproductos)):
        print(f"""
          Id: {x}
          Nombre: {nproductos[x]}  Stock: {stockproductos[x]}
          Precio: ${precioproductos[x]}
              """)
    #   Aca puede suceder que no necesitemos si o si ir al menu producto
    #   Si pasamos como valor 1 vamos al menu producto, sino no
    if (valor == 1):
        menuProducto()


def listadoCliente(valor):
    """ 
    Aca procedemos a mostrar los clientes 
    """
    print("Clientes: ")
    for x in range(len(nombres)):
        print(f"""
          Id: {x}    
          Nombre: {nombres[x]}  Apellido: {apellidos[x]}
          Direccion: {direcciones[x]}
          DNI: {dnis[x]} Telefono: {telefonos[x]}              
              """)
    #   Aca puede suceder que no necesitemos si o si ir al menu cliente
    #   Si pasamos como valor 1 vamos al menu cliente, sino no
    if (valor == 1):
        menuCliente()


def altaCompra():
    """
    Generamos el alta de la compra
    """
    total = 0
    print("Bienvenido ")
    listadoFactura(0)
    #   Para vincular los elementos usamos su indice
    eleccionfactura = validarIndice(facturas)
    listadoCliente(0)
    eleccioncliente = validarIndice(nombres)
    #   Solo averiguamos cuantos elementos compraremos para sacar el costo
    ccompras = int(input("Cuantos productos va a elegir?    "))
    for i in range(ccompras):
        listadoProducto(0)
        eleccionproducto = validarIndice(nproductos)
        cproductos = int(input("Cuantos? "))
        productosComprados = [f"Producto: {nproductos[eleccionproducto]}",
                              f"Cantidad: {cproductos}",
                              f"Total: ${cproductos * precioproductos[eleccionproducto]}"]
        total = total + (cproductos * precioproductos[eleccionproducto])
        facturaCompras.append([productosComprados])
    datosFacturaElementos = [
        f"Codigo: {facturas[eleccionfactura]}",
        f"Fecha: {ffacturas[eleccionfactura]}",
        f"Cliente: {nombres[eleccioncliente]}",
        f"DNI: {dnis[eleccioncliente]}",
        f"Telefono: {telefonos[eleccioncliente]}",
        f"Direccion: {direcciones[eleccioncliente]}"]
    facturaElementos.append(datosFacturaElementos)
    totales.append(total)
    print("Compra Cargada")
    menuCompra()


def altaFactura():
    print("Bienvenido ")
    ccc = int(input("Cuantos factura quiere cargar? "))
    for i in range(ccc):
        #   Pedir datos de la factura a crear
        factura = input("Codigo?  ")
        ffactura = input("Fecha?  ")
        facturas.append(factura)
        ffacturas.append(ffactura)
    menuFactura()


def altaProducto():
    """ 
    Alta de producto
    """
    print("Bienvenido ")
    ccc = int(input("Cuantos productos quiere cargar? "))
    for i in range(ccc):
        nproducto = input("Nombre?  ")
        sproducto = int(input("Stock? "))
        pproducto = int(input("Precio? "))
        nproductos.append(nproducto)
        stockproductos.append(sproducto)
        precioproductos.append(pproducto)
        print("Carga Realizada ")
    menuProducto()


def altaCliente():
    """
    Generamos el alta de un cliente
    """
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


def validarEleccionMCompra(eleccion):
    """
    Validamos las opciones del menu Compra
    """
    while (eleccion < 1 or eleccion > 4):
        eleccion = int(input("Elija una opcion valida "))
    if (eleccion == 1):
        print("Alta Compra")
        altaCompra()
    elif (eleccion == 2):
        print("Listado de Compra")
        listadoCompra(1)
    elif (eleccion == 3):
        print("Volver al menu Principal")
        menuPrincipal()
    elif (eleccion == 4):
        salir()


def validarEleccionMFactura(eleccion):
    """
    Validamos las opciones del factura
    """
    while (eleccion < 1 or eleccion > 6):
        eleccion = int(input("Elija una opcion valida "))
    if (eleccion == 1):
        print("Alta Factura")
        altaFactura()
    elif (eleccion == 2):
        print("Baja Factura")
        bajaFactura()
    elif (eleccion == 3):
        print("Modificacion Factura")
        edicionFactura()
    elif (eleccion == 4):
        print("Listado de Factura")
        listadoFactura(1)
    elif (eleccion == 5):
        print("Volver al menu Principal")
        menuPrincipal()
    elif (eleccion == 6):
        salir()


def validarEleccionMProducto(eleccion):
    """
    Validamos las opciones del cliente
    """
    while (eleccion < 1 or eleccion > 6):
        eleccion = int(input("Elija una opcion valida "))
    if (eleccion == 1):
        print("Alta Producto")
        altaProducto()
    elif (eleccion == 2):
        print("Baja Producto")
        bajaProducto()
    elif (eleccion == 3):
        print("Modificacion Producto")
        edicionProducto()
    elif (eleccion == 4):
        print("Listado de Producto")
        listadoProducto(1)
    elif (eleccion == 5):
        print("Volver al menu Principal")
        menuPrincipal()
    elif (eleccion == 6):
        salir()


def validarEleccionMCliente(eleccion):
    """
    Validamos las opciones del cliente
    """
    while (eleccion < 1 or eleccion > 6):
        eleccion = int(input("Elija una opcion valida "))
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


def menuCompra():
    """
    Menu de Compra
    """
    print("""
    1) Alta Compra
    2) Visualizar Compra
    3) Volver al menu Principal
    4) Salir
    """)
    eleccion = int(input("Ingrese una opcion "))
    validarEleccionMCompra(eleccion)


def menuFactura():
    """
    Menu de Factura
    """
    print("""
    1) Alta Factura
    2) Baja Factura
    3) Modificacion Factura
    4) Listado de Factura
    5) Volver al menu Principal
    6) Salir
    """)
    eleccion = int(input("Ingrese una opcion "))
    validarEleccionMFactura(eleccion)


def menuProducto():
    """
    Menu de Productos
    """
    print("""
    1) Alta Producto
    2) Baja Producto
    3) Modificacion Producto
    4) Listado de Producto
    5) Volver al menu Principal
    6) Salir
    """)
    eleccion = int(input("Ingrese una opcion "))
    validarEleccionMProducto(eleccion)


def menuCliente():
    """
    Menu de cliente
    """
    print("""
    1) Alta Cliente
    2) Baja Cliente
    3) Modificacion Cliente
    4) Listado de Cliente
    5) Volver al menu Principal
    6) Salir
    """)
    eleccion = int(input("Ingrese una opcion "))
    validarEleccionMCliente(eleccion)


def validarEleccion():
    """
    Validamos que el usuario elija una opcion valida
    sino se la volvemos a pedir. 
    """
    eleccion = int(input("Elija una opcion "))
    while (eleccion < 1 or eleccion > 5):
        eleccion = int(input("Elija una opcion valida "))
    #   En el caso de ser una opcion valida, salimos a las opciones del menu
    if (eleccion == 1):
        menuCliente()
    elif (eleccion == 2):
        menuProducto()
    elif (eleccion == 3):
        menuFactura()
    elif (eleccion == 4):
        menuCompra()
    elif (eleccion == 5):
        salir()


def menuPrincipal():
    """
    Menu principal de la aplicacion
    """
    #   Solo limpio pantalla con la pantalla inicial
    limpiarPantalla()
    #   Usamos colores, por eso vamos con print separados
    print("Bienvenido")
    print("1) "+"\033[1;33m"+"ABM Cliente"+'\033[0;m')
    print("2) "+"\033[1;33m"+"ABM Producto"+'\033[0;m')
    print("3) "+"\033[1;33m"+"ABM Factura"+'\033[0;m')
    print("4) "+"\033[1;33m"+"Compra"+'\033[0;m')
    print("5) "+"\033[1;33m"+"Salir"+'\033[0;m')
    #   Validamos que elijan un entero entre los que van
    validarEleccion()


#   Cargamos el menu principal
menuPrincipal()
