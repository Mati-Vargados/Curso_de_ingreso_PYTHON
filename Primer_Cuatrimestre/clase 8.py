import random

#-FUNCIONES---------------------------------------------------------------------

def mostrar_matriz(matriz:list)-> None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end = "  ")
        print(" ")

def crear_legajos (matriz_vacia:list) -> list:

    legajo = random.randint(0, 1000)

    for i in range(len(matriz_vacia)):
        for j in range(len(matriz_vacia[i])):

            legajo += 1
            matriz_vacia[i][j] = legajo

    return matriz_vacia

def econtrar_numero_especifico_matriz(matriz:list, dato_ingresado:int)-> bool | None:

    encontrado = False

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == dato_ingresado:
                encontrado = True
            
    return encontrado
                
def encontrar_legajo(matriz:list)-> None:

    dato_ingresado = int(input("Ingrese un legajo: "))
    while econtrar_numero_especifico_matriz(matriz, dato_ingresado) != True:
        dato_ingresado = int(input("ERROR. Reingrese un legajo: "))
    
    print(f"Se ingreso al legajo {dato_ingresado}. ")

    return True

def validar_linea(matriz:list) -> bool:

    encontrado = False
    
    linea = int(input("Ingrese que linea quiere encontrar: "))

    while encontrado == False:

        for i in range(len(matriz)):
            if matriz[i][0] == linea:

                return True
            
            else:
                linea = int(input("Linea no encontrada, intente nuevamente: "))

    

def validar_interno(matriz:list) -> True:

    interno = int(input("Ingrese el interno de la linea previamente ingresada: "))

    encontrado = False

    while encontrado == False:
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] == interno:

                    return True
            else:
                interno = int(input("Interno no encontrada, intente nuevamente: "))
                
            
def almacenar_recaudos(matriz_coches:list, matriz_recaudo:list)-> None:
    
    for i in range(1, len(matriz_coches)):
        for j in range(1, len(matriz_coches[i])):
            matriz_recaudo[i - 1][j - 1] = int(input("Ingrese el recaudo del colectivo: "))

    mostrar_matriz(matriz_recaudo)

                      
#-MATRIZ---------------------------------------------------------------------
            #3X6                            
matriz_coches = [[98, 116, 5, 3, 1, 2],             # i = 98
                 [22, 55, 6, 23, 11, 15],           # i = 22
                 [95, 100, 10, 22, 17, 33]]         # i = 95

matriz_legajos = [[0]*5 for _ in range(3)]

            #3X5
matriz_recaudo = [[0]*5 for _ in range(3)]

#-MENU-----------------------------------------------------------------------

legajo_encontrado = False

while True:
    
    print("""
        1- Cargar planilla y el chofer se debe identificar.
        2- Mostrar la recaudación de todos los coches y líneas.
        3- Calcular y mostrar recaudación por línea.
        4- Calcular y mostrar recaudación por coche.
        5- Calcular y mostrar la recaudación total.
        6- Salir.
        """)

    seccion_menu = int(input("Ingrese la sección del menú que quieras usar: "))
    while seccion_menu != 1 and seccion_menu != 2 and seccion_menu != 3 and seccion_menu != 4 and seccion_menu != 5 and seccion_menu != 6:
        seccion_menu = int(input("ERROR. Reingrese la sección del menú que quieras usar: "))

    match seccion_menu:
        case 1:

            print("LISTA DE LOS LEGAJOS")
            mostrar_matriz(crear_legajos(matriz_legajos))
           
            print("LISTA DE LOS COCHES")
            mostrar_matriz(matriz_coches)

            if encontrar_legajo(matriz_legajos) == True:
                legajo_encontrado = True

            if validar_linea(matriz_coches) == True and validar_interno(matriz_coches) == True:

                almacenar_recaudos(matriz_coches, matriz_recaudo)

        case 2:
            if legajo_encontrado == True:
                pass
            else:
                print("No se ingreso ningun legajo (Opcion 1)")
        case 3:
            if legajo_encontrado == True:
                pass
            else:
                print("No se ingreso ningun legajo (Opcion 1)")
        case 4:
            if legajo_encontrado == True:
                pass
            else:
                print("No se ingreso ningun legajo (Opcion 1)")
        case 5:
            if legajo_encontrado == True:
                pass
            else:
                print("No se ingreso ningun legajo (Opcion 1)")
        case 6:
            print("¡Gracias por usar nuestro programa!")
            break
        
