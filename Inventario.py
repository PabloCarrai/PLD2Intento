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
facturaFull = []


def salir():
    exit()


def edicionCompra():
    """
    Edicion Compra. 
    Solo editamos el stock del producto a comprar
    Pero lo hacemos como cargar de nuevo el listado
    """
    listadoCompra(0)
    eleccion = int(input("Ingrese un id valido "))
    listadoFactura(0)
    eleccionfactura = int(input("Elija un id valido "))
    listadoCliente(0)
    eleccioncliente = int(input("Elija un id valido "))
    listadoProducto(0)
    eleccionproducto = int(input("Elija un id valido "))
    cproductos = int(input("Cantidad de producto a comprar "))
    compra = [
        f"Codigo: {facturas[eleccionfactura]}",
        f"Fecha: {ffacturas[eleccionfactura]}",
        f"Cliente: {nombres[eleccioncliente]}",
        f"DNI: {dnis[eleccioncliente]}",
        f"Telefono: {telefonos[eleccioncliente]}",
        f"Direccion: {direcciones[eleccioncliente]}",
        f"Producto: {nproductos[eleccionproducto]}",
        f"Cantidad: {cproductos}",
        f"Total: ${cproductos * precioproductos[eleccionproducto]}"]
    facturaFull[eleccion] = compra
    print("Compra Cargada")
    menuCompra()

    pass


def edicionFactura():
    """
    Edicion de factura
    """
    listadoFactura(0)
    eleccion = int(input("Ingrese un id valido "))
    factura = input("Codigo?")
    ffactura = input("Fecha?")
    facturas[eleccion] = factura
    ffacturas[eleccion] = ffactura
    print("Factura editado ")
    menuFactura()


def edicionProducto():
    """
    Edicion de producto
    """
    listadoProducto(0)
    eleccion = int(input("Ingrese un id valido "))
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


def bajaCompra():
    """
    Funcion para eliminar un Compra
    """
    #   Aca listamos producto sin ir al menu luego del listado
    listadoCompra(0)
    eleccion = int(input("Ingrese un id valido "))
    del (facturaFull[eleccion])
    print("Compra eliminada")
    menuCompra()


def bajaFactura():
    """
    Funcion para eliminar un Factura
    """
    #   Aca listamos producto sin ir al menu luego del listado
    listadoFactura(0)
    eleccion = int(input("Ingrese un id valido "))
    del (facturas[eleccion])
    del (ffacturas[eleccion])
    menuFactura()


def bajaProducto():
    """
    Funcion para eliminar un producto
    """
    #   Aca listamos producto sin ir al menu luego del listado
    listadoProducto(0)
    eleccion = int(input("Ingrese un id valido "))
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
    eleccion = int(input("Ingrese un id valido "))
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
    for x in range(len(facturaFull)):
        print(f"""
        id:{x} 
         {facturaFull[x]}
           
        """)
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
    print("Bienvenido ")
    listadoFactura(0)
    eleccionfactura = int(input("Elija un id valido "))
    listadoCliente(0)
    eleccioncliente = int(input("Elija un id valido "))
    listadoProducto(0)
    eleccionproducto = int(input("Elija un id valido "))
    cproductos = int(input("Cantidad de producto a comprar "))
    compra = [
        f"Codigo: {facturas[eleccionfactura]}",
        f"Fecha: {ffacturas[eleccionfactura]}",
        f"Cliente: {nombres[eleccioncliente]}",
        f"DNI: {dnis[eleccioncliente]}",
        f"Telefono: {telefonos[eleccioncliente]}",
        f"Direccion: {direcciones[eleccioncliente]}",
        f"Producto: {nproductos[eleccionproducto]}",
        f"Cantidad: {cproductos}",
        f"Total: ${cproductos * precioproductos[eleccionproducto]}"]
    facturaFull.append(compra)
    print("Compra Cargada")
    menuCompra()


def altaFactura():
    print("Bienvenido ")
    ccc = int(input("Cuantos factura quiere cargar? "))
    for i in range(ccc):
        #   Pedir datos de la factura a crear
        factura = input("Codigo?")
        ffactura = input("Fecha?")
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
    while (eleccion < 1 or eleccion > 6):
        eleccion = int(input("Elija una opcion valida "))
    if (eleccion == 1):
        print("Alta Compra")
        altaCompra()
    elif (eleccion == 2):
        print("Baja Compra")
        bajaCompra()
    elif (eleccion == 3):
        print("Modificacion Compra")
        edicionCompra()
    elif (eleccion == 4):
        print("Listado de Compra")
        listadoCompra(1)
    elif (eleccion == 5):
        print("Volver al menu Principal")
        menuPrincipal()
    elif (eleccion == 6):
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
    2) Baja Compra
    3) Modificacion Compra
    4) Listado de Compra
    5) Volver al menu Principal
    6) Salir
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
    Este es el menu de cliente del ABM
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
    print("""
    1) ABM Cliente
    2) ABM Producto
    3) ABM Factura
    4) Compra
    5) Salir
    """)
    validarEleccion()


#   Cargamos el menu principal
menuPrincipal()
