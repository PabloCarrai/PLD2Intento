def salir():
    print("Hasta la proxima")
    exit()


def opcionesValidas(eleccion):
    while (eleccion>4 or eleccion<1):
        print("Elija una opcion valida")
        menuPrincipal()
    if (eleccion==4):
        salir()
    else:
        abm(eleccion)


def menuSecundario(resultado):
    print(resultado)
    

def abm(eleccion):
    resultado=""
    if (eleccion==1):
        resultado="cliente"
    elif(eleccion==2):
        resultado="producto"
    elif(eleccion==3):
        resultado="factura"
    menuSecundario(resultado)


def menuPrincipal():
    print("Bienvenido al menu Principal")
    print("""
          
         1) ABM Cliente
         2) ABM Producto
         3) ABM Factura
         4) Salir 
          
          
          
          """)
    eleccion=int(input("Ingrese una opcion:  "))
    opcionesValidas(eleccion)
          


menuPrincipal()    