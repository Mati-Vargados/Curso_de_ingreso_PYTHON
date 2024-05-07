from package_input.input import get_int
import random

"""
Una empresa de colectivos tiene 3 líneas de 5 coches cada una. En total tiene 15 choferes (cada uno con un legajo distinto generado aleatoriamente).
Nos piden desarrollar un software que presente el siguiente menú  de usuarios:
 
Menú:

Cargar planilla. El chofer se debe identificar (el legajo debe existir dentro de una matriz de legajos). 

Si el chofer existe cargará la recaudación del viaje indicando línea y coche (no necesariamente un chofer está asignado a una única línea y coche), 
estos datos deben estar validados. Un chofer puede cargar más de una recaudación por día (para distintas líneas y distintos coches). 
Cada coche de cada línea puede tener varias recaudaciones diarias.
Mostrar la recaudación de todos los coches y líneas.

Calcular y mostrar recaudación por línea.

Calcular y mostrarla recaudación total.

Salir
Todo el desarrollo tiene que estar modularizado: ingreso de datos, validaciones de líneas y coches, generación y verificación de existencia de legajo, cálculos, etc.
"""
#________________________________________________________________________________________
#FUNCIONES

def mostrar_matriz(matriz:list)-> None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f'{matriz[i][j]: 4}', end='')

        print("")

def crear_legajos (matriz_vacia:list) -> list:

    legajo = random.randint(1, 1000)

    for i in range(len(matriz_vacia)):
        for j in range(len(matriz_vacia[i])):

            legajo += 1

            matriz_vacia[i][j] = legajo


    return matriz_vacia


def validar_legajo(matriz:list) -> bool:

    numero = get_int("Ingrese el numero de legajo: ", "ERROR. Reingrese el numero de legajo: " , 1, 1016, 3)

    for i in range(len(matriz)):
            for j in range(len(matriz[i])):

                if numero == matriz[i][j]:

                    return True
                
                else:

                    return False
                

def validar_linea(matriz:list) -> bool:
    
    linea = get_int("Ingrese su numero de linea: ", "Numero invalido, intente nuevamente: ", 1, 9999, 3)

    for i in range(len(matriz)):
        if matriz[i][0] == linea:

            return True
        
    print("________________________________")
    return False
    

def validar_interno(matriz:list, interno:int) -> bool:
    
    

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == interno:

                return True
        
    print("________________________________")
    return False

def almacenar_recaudos(matriz_colectivo:list, matriz_recaudo:list)-> None:

    interno = get_int("Ingrese su numero de interno: ", "Numero invalido, intente nuevamente: ", 1, 9999, 3)
    
    if validar_linea(matriz_colectivo) == True and validar_interno(matriz_colectivo, interno) == True:

        for i in range(len(matriz_colectivo)):
            for j in range(len(matriz_colectivo[i])):
                if matriz_colectivo[i][j] == interno:
                    matriz_recaudo[i-1][j-1] = get_int("Ingrese el recaudo que gusto: ", "ERROR, Reingrese el reacudo: ", 1, 10000, 3)
                    
        mostrar_matriz(matriz_recaudo)
        return matriz_recaudo




#________________________________________________________________________________________
#MATRICES 

matriz_choferes = [[0]* 5 for _ in range(3)]

matriz_colectivo = [[100, 14, 21, 32, 423, 543],
                    [23, 147, 24, 38, 4, 512],
                    [33, 12, 28, 36, 456, 53]]

matriz_recaudo = [[0]*5 for _ in range(3)]

while True: 

    menu = print("""
        A)Cargar planilla         
        B)Mostrar la recaudación de todos los coches y líneas.
        C)Calcular y mostrar recaudación por línea.
        D)Calcular y mostrar recaudación por coche.
        E)Calcular y mostrar la recaudación total.
        F)Salir""")

    bandera_validar = False

    while True:
        opcion = input("Elegir una de estas opciones: ")

        match opcion:
            case "A": 
                
                print("\nLegajos")
                crear_legajos(matriz_choferes)
                mostrar_matriz(matriz_choferes)
                
                print("\nLineas e internos de colectivos")
                mostrar_matriz(matriz_colectivo)

                while validar_legajo(matriz_choferes) == False:
                    print("")

                # while validar_linea(matriz_colectivo) == False:
                #     print("")
                
                # while validar_interno(matriz_colectivo) == False:
                #     print("")

                almacenar_recaudos(matriz_colectivo, matriz_recaudo)
                
                
                

            case "B":

                if bandera_validar == True :
                    
                    pass
                else:
                    print("Ingrese opcion A")
                
            case "C":

                if bandera_validar == True :
                    
                    pass
                else:
                    print("Ingrese opcion A")
                
            case "D":

                if bandera_validar == True :
                    
                    pass
                else:
                    print("Ingrese opcion A")
                
            case "E":

                if bandera_validar == True :
                    
                    pass
                else:
                    print("Ingrese opcion A")

            case "F":
                
                break
                        
                        
            case _:
                error = input("Error: ingrese una opción válida: ")
    