from class_boligrafo import Boligrafo

lapicera_1 = False
lapicera_2 = False

while True:

    print("""
    A - Ingresar lapicera 1
    B - Ingresar lapicera 2
    C - Escribir 
    D - Recargar lapicera
    E - Salir
    """)
    
    
    opciones = input("Ingrese una de las opciones: ").upper()

    while (opciones != "A" and 
           opciones != "B" and 
           opciones != "C" and 
           opciones != "D" and
           opciones != "E"):
        opciones = input("ERROR. Reingrese una de las opciones: ").upper()

    match opciones:
        case "A":
            print("__LAPICERA_1__")

            grosura = input("Ingrese el tipo de grosura (grueso o fino): ").lower()
            while grosura != "grueso" and grosura != "fino":
                grosura = input("ERROR. Reingrese el tipo de grosura (grueso o fino): ").lower()

            color = input("Ingrese el color rojo o azul: ").lower()
            while color != "rojo" and color != "azul":
                color = input("ERROR. Reingrese el color rojo o azul: ").lower()

            pen_1 = Boligrafo(grosura, color)
            # Se instancia en la clase boligrafo y se pasa como parametros los atributos grosura / color
            lapicera_1 = True

        case "B":
            print("__LAPICERA_2__")

            grosura = input("Ingrese el tipo de grosura (grueso o fino): ").lower()
            while grosura != "grueso" and grosura != "fino":
                grosura = input("ERROR. Reingrese el tipo de grosura (grueso o fino): ").lower()

            color = input("Ingrese el color rojo o azul: ").lower()
            while grosura != "rojo" and grosura != "azul":
                color = input("ERROR. Reingrese el color rojo o azul: ").lower()

            pen_2 = Boligrafo(grosura, color)

            lapicera_2 = True

        case "C":

            tipo_lapicera = int(input("Ingrese a que lapicera quiere ingresar (1 o 2): "))
            while (tipo_lapicera != 1 and 
                   tipo_lapicera != 2):
                tipo_lapicera = int(input("ERROR. Reingrese a que lapicera quiere ingresar (1 o 2): "))

            if tipo_lapicera == 1 and lapicera_1 == True:
                texto = input("Ingrese el texto que querew escribir: ")
                print(pen_1.escribir(texto))

            elif tipo_lapicera == 2 and lapicera_2 == True:
                texto = input("Ingrese el texto que querew escribir: ")
                print(pen_2.escribir(texto))
                
            else:
                print(f"No se ingreso la lapicera {tipo_lapicera}")

        case "D":

            tipo_lapicera = int(input("Ingrese a que lapicera quiere ingresar (1 o 2): "))
            while (tipo_lapicera != 1 and 
                   tipo_lapicera != 2):
                tipo_lapicera = int(input("ERROR. Reingrese a que lapicera quiere ingresar (1 o 2): "))

            if tipo_lapicera == 1 and lapicera_1 == True:
                recarga = int(input("Ingrese cuanta tinta queres recagar: "))
                print(pen_1.recargar(recarga))
                opcion = "´A´"

            elif tipo_lapicera == 2 and lapicera_2 == True:
                recarga = int(input("Ingrese cuanta tinta queres recagar: "))
                print(pen_2.recargar(recarga))
                opcion = "´B´"
            else:
                print(f"No se ingreso la lapicera {tipo_lapicera}")

        case "E":
            print("¡Gracias por usar nuestro sistema!")
            breakopcion = "´A´"


    


    


    