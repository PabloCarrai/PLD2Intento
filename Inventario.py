"""

Hay un error que no logre resolver. 
En ciertas ocasiones cuando elegia una opcion invalida. 
Se repetia el menu y dejaba de responder a una opcion valida. 
Asi que ahora cuando me equivoco con una opcion invalido. 
Termino el programa.     
    
"""
nombres = []
apellidos = []
dnis = []
direcciones = []


def adonde(menu):
    if (menu == 1):
        menuPrincipal()
    elif (menu == 2):
        abm()


def listarElemento():
    for x in range(len(nombres)):
        print(f"""

    ID: {x} 
    Nombre: {nombres[x]} Apellido: {apellidos[x]}
    DNI: {dnis[x]} Direccion: {direcciones[x]}
              
              """)
    menuPrincipal()


def cargarElemento():
    nombre = input("Ingrese Nombre ")
    apellido = input("Ingrese Apellido ")
    dni = input("Ingrese DNI ")
    direccion = input("Ingrese Direccion ")
    nombres.append(nombre)
    apellidos.append(apellido)
    dnis.append(dni)
    direcciones.append(direccion)
    menuPrincipal()


def editarElemento():
    listarElemento()
    eleccion = int(input("Ingrese id del cliente a editar  "))


def menu(eleccion):
    print(f"""
          
          1) Cargar {eleccion}
          2) Listar {eleccion} 
          3) Editar {eleccion}
          4) Borrar {eleccion}
          5) Volver
          
          
          """)
    elegir = int(input("Ingrese su eleccion "))
    while (elegir < 1 or elegir > 5):
        print("Elija una opcion valida ")
        elegir = int(input("Ingrese su eleccion "))
    if (elegir == 1):
        cargarElemento()
    elif (elegir == 2):
        listarElemento()
    elif (elegir == 3):
        editarElemento()
    elif (elegir == 4):
        pass
    elif (elegir == 5):
        menuPrincipal()


def salir():
    print("Hasta la proxima")
    exit()


def opcionesValidas(eleccion):
    while (eleccion > 4 or eleccion < 1):
        print("Elija una opcion valida")
        salir()
    if (eleccion == 4):
        salir()
    else:
        abm(eleccion)


def abm(eleccion):
    resultado = ""
    if (eleccion == 1):
        resultado = "Cliente"
        menu(resultado)
    elif (eleccion == 2):
        resultado = "Producto"
        menu(resultado)
    elif (eleccion == 3):
        resultado = "Factura"
        menu(resultado)


def menuPrincipal():
    print("Bienvenido al menu Principal")
    print("""
          
         1) ABM Cliente
         2) ABM Producto
         3) ABM Factura
         4) Salir 
          
          
          
          """)
    eleccion = int(input("Ingrese una opcion:  "))
    opcionesValidas(eleccion)


adonde(1)
