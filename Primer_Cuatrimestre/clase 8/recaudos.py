from package_input.input import get_int
from validaciones_de_líneas_y_coches import *


def almacenar_recaudos(matriz_colectivo:list, matriz_recaudo:list)-> None:

    linea = get_int("Ingrese a que linea quiere ingresar LINEA 1, LINEA 2, LINEA 3: ", "Numero invalido, intente nuevamente: ", 1, 3, 3)

    linea = linea - 1

    interno = get_int("Ingrese su numero de interno: ", "Numero invalido, intente nuevamente: ", 1, 9999, 3)
    
    if validar_linea(matriz_colectivo, linea) == True and validar_interno(matriz_colectivo, interno) == True:

        for i in range(len(matriz_colectivo)): 
            for j in range(len(matriz_colectivo[i])):
                if matriz_colectivo[linea][j] == interno:
                    matriz_recaudo[linea][j] += get_int("Ingrese el recaudo: ", "ERROR, Reingrese el reacudo: ", 0, 1000000, 3)

                    return matriz_recaudo

    print(f"ERROR. NO SE ENCONTRO EL INTERNO {interno} EN LA LINEA {linea + 1}")      
                
    

def mostrar_recaudacion_coche(matriz_recaudo:list, matriz_colectivo: list )-> None:

    for i in range(len(matriz_recaudo)):
        for j in range(len(matriz_recaudo[i])):
            coche = matriz_colectivo[i][j]
            
            print(f"El coche {coche} de la linea {i + 1} tuvo una recaudacion de: {matriz_recaudo[i][j]}")

def mostrar_recaudacion_total(matriz_recaudo:list)-> None:

    recaudacion_total = 0
    
    for i in range(len(matriz_recaudo)):
        for j in range(len(matriz_recaudo[i])):
                    
            recaudacion_total += matriz_recaudo [i][j]
    
    print(f"La recaudacion total de todas las lineas y coches es de ${recaudacion_total}")