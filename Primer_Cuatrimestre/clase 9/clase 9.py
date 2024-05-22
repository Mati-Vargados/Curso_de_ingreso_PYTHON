def mostrar_matriz(matriz:list)-> None:
    for i in range(len(matriz)):
            print(matriz[i], end=' ')
    print("")

def bubble_sort(lista:list)-> None:

    for i in range(len(lista)): 
        for j in range(len(lista)-1 - i): 
            if lista[j] > lista [j + 1]:  
                auxiliar = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = auxiliar

    mostrar_matriz(lista)

numeros = [10, 2 , 3, 8, 1]
mostrar_matriz(numeros)
bubble_sort(numeros)