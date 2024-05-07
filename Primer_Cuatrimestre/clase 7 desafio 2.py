from package_input.input import get_int

filas = get_int("Ingrese un numero para las filas: ", "ERROR, Ingrese un numero para la filas: ", -100, 100, 3)

columnas = get_int("Ingrese un numero para las columnas: ", "ERROR, Ingrese un numero para la columnas: ", -100, 100, 3)

print(f"Su matriz es de {filas}x{columnas}")

if filas == columnas:

    matriz = [[0]* columnas for _ in range(filas)]

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = int(input(f"Ingrese un numero para la posicion {i + 1}x{j + 1}."))
            
    #-----SUMA-DE-FILAS-------------------------------------------------------------------------------------

    for i in range(len(matriz)):
        suma_filas = 0
        for j in range(len(matriz[i])):
            suma_filas += matriz[i][j]

    #-----SUMA-DIAGONAL-------------------------------------------------------------------------------------
    
    suma_diagonal_primera = 0 
    for i in range(len(matriz)):
            suma_diagonal_primera += matriz[i][i]

    #-----SUMA-DIAGONAL-INVERTIDA---------------------------------------------------------------------------

    suma_diagonal_segunda = 0
    fila_diagonal_segunda = len(matriz) - 1 # 3x3 - 1 = da a entender que son 3 filas
    for i in range(len(matriz)):
        suma_diagonal_segunda += matriz[fila_diagonal_segunda][i]
        fila_diagonal_segunda -= 1

    #-----SUMA-DE-COLUMNAS----------------------------------------------------------------------------------

    for j in range(len(matriz[0])):
        suma_columnas = 0
        for i in range(len(matriz)):
            suma_columnas += matriz[i][j]
        
    print(f"La suma de las columnas es {suma_columnas}.
        \nLa suma de las columnas es {suma_filas}.
        \nLa suma de la primer diagonal es {suma_diagonal_primera}. 
        \nLa suma de la segunda diagonal es {suma_diagonal_segunda}.")

    #-------------------------------------------------------------------------------------------------------

    formula = filas*(filas**2 + 1)/2 

    #-------------------------------------------------------------------------------------------------------

    if suma_filas and suma_columnas and suma_diagonal_primera and suma_diagonal_segunda == formula:
        print("Es una matriz de cuadrado magico")

    else:
        print("No es un cuadrado magico.")

else:
    print("No es un cuadrado magico.")