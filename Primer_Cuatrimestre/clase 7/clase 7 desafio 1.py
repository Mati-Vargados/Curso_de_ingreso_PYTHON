from package_input.input import get_int

def mostrar_matriz(matriz:list)-> None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print("")

#_______________________________________________________________________________________   

filas_a = get_int("Ingrese la cantidad de filas para la matriz A: ", "ERROR, ingrese un valor valido: ", 1, 100, 3)

columnas_a = get_int("Ingrese la cantidad de columnas para la matriz A: ", "ERROR, ingrese un valor valido: ", 1, 100, 3)

print(f"La matriz ´A´ va a ser de {filas_a}x{columnas_a}")

#_______________________________________________________________________________________    

filas_b = get_int("Ingrese la cantidad de filas para la matriz B: ", "ERROR, ingrese un valor valido: ", 1, 100, 3)

columnas_b = get_int("Ingrese la cantidad de columnas para la matriz B: ", "ERROR, ingrese un valor valido: ", 1, 100, 3)

print(f"La matriz ´B´ va a ser de {filas_b}x{columnas_b}")

#_____________________________________________________________________________________  
 
if columnas_a == filas_b:

    matriz_a = [[0] * columnas_a for _ in range(filas_a)]

    for i in range(len(matriz_a)):
        for j in range(len(matriz_a[i])):
            matriz_a[i][j] = int(input(f"Ingrese un numero en {i + 1} x {j + 1} para la matriz A: "))

    mostrar_matriz(matriz_a)

#_____________________________________________________________________________________  
 
    matriz_b = [[0] * columnas_b for _ in range(filas_a)]

    for i in range(len(matriz_b)):
        for j in range(len(matriz_b[i])):
            matriz_b[i][j] = int(input(f"Ingrese un numero en {i + 1} x {j + 1} para la matriz B: "))

    mostrar_matriz(matriz_b)

#_____________________________________________________________________________________  

    print(f"Su resultado va a ser de {filas_a}x{filas_b}")

    matriz_resultado = [[0] * filas_a for _ in range(columnas_b)]

    for i in range(len(matriz_a)):
        for j in range(len(matriz_b[0])):
            for k in range(len(matriz_a)):
                matriz_resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]

    print("Resultado: ")
    mostrar_matriz(matriz_resultado)

else:
    print("La columnas de A y las filas de B no son iguales. LA CUENTA NO SE PUEDEHACER")
    
#_____________________________________________________________________________________   


