matriz = [[1, 2, 3], 
          [4, 5, 6],
          [7, 8, 9]]

#                |
#matriz = vacia  v
matriz = [[0] * 3 for _ in range(4)]

def mostrar_matriz(matriz:list) -> None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print("")

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = int(input(f"Ingrese un numero en {i + 1} x {j + 1}: "))

mostrar_matriz(matriz)

#------------------------------------------------------------------------------------

matriz = [[1, 2, 3], 
          [4, 5, 6],
          [7, 8, 9]]

def mostrar_columna(matriz:list)-> None:
    for j in range(len(matriz[0])):
        print(f"Columna {j + 1}")
        for i in range(len(matriz)):
            print(matriz[i][j])

#------------------------------------------------------------------------------------
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = matriz[i][j] * 5


#------------------------------------------------------------------------------------
matriz = [[1, 2, 3], 
          [4, 5, 6],
          [7, 8, 9],
          [10, 11, 12]]

matriz_auxiliar = [[10, 20, 30], 
                   [40, 50, 60],
                   [70, 80, 90]]    

matriz_resultado_suma = [[0] * 3 for _ in range(3)]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz_resultado_suma = matriz[i][j] + matriz_auxiliar[i][j]

mostrar_matriz(matriz_resultado_suma)


