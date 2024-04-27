from package_arrays.array_generales import *


def ingresar_numeros_enteros (lista:list)-> list:
    """
    - Esta funcion nos permite ingresar numeros (mediante la funcion get_int) y asignarlas a una lista.

    - Args:
        - lista (list): Este parametro es una lista con valores X que nos permite almacenar los numeros ingresados.

    - Returns:
        - bool | None: Con la variable "lista" la funcion returna la nueva lista al sistema.
    """
    for i in range(len(lista)):
        numero = get_int("Ingrese un numero entero: ", "ERROR. Reingrese el numero por favor: ", -1000, 1000, 3)
        lista[i] = numero
    
    return lista

def calcular_positividad(numero:int) -> bool | None:
    """
    - Esta funcion calcula la positividad de un numero (si es negativo, positivo o nulo).

    - Args:
        - numero (int): Recibe como parametro un numero (predefinido) entero.

    - Returns:
        - bool | None: Con la variable "positividad" (y su valor True, False o None) devuelve la postividad de un numero.
    """
    postitividad = None

    if numero > 0:
        postitividad = True
    elif numero < 0:
        postitividad = False

    return postitividad

def contador_positivos_negativos(lista:list)-> None:
    """ 
    - Esta funcion se encarga (con ayuda de la funcion "calcular_positividad") de contar la cantidad de numeros positivos y negativos de una lista. 
          Tambien imprime (mediante un print) los valores finales (numero negativo y su posicion).

    - Args:
        lista (list): Este parametro ingresa una lista (predefinida).
    """
    contador_postivo = 0
    contador_negativo = 0
    for i in range(len(lista)):
        if calcular_positividad(lista[i]) == True:
            contador_postivo = contador_postivo + 1
        elif calcular_positividad(lista[i]) == False:
            contador_negativo = contador_negativo + 1

    print(f"Hay {contador_postivo} numeros positivos y {contador_negativo} negativos.")

def calcular_numeros_pares_impares(numero: int)-> bool:
    """
    - Esta funcion se encarga de ver si el numero ingresado es par o impar; mediante la variable "par" se le da un valor positivo o negativo (True or False) al parametro ingresado.

    Args:
        numero (int): Este parametro trae un numero (predefinido). 

    Returns:
        bool: Returna mediante la variable "par" un valor True o False.
    """
    if numero % 2 == 0:
        par = True
    else:
        par = False
    
    return par

def sumar_numeros_pares(lista:list)-> None:
    """
    - Esta funcion suma los numeros pares de la lista (con ayuda de la funcion "calcular_numeros_pares_impares") y luego imprime el valor final.

    Args:
        lista (list): Este parametro ingresa una lista (predefinida).
    """

    acumulador_numeros_pares = 0

    for i in range(len(lista)):
        if calcular_numeros_pares_impares(lista[i]) == True:
            acumulador_numeros_pares = acumulador_numeros_pares + lista[i]

    print(f"La suma de todos los numeros pares es: {acumulador_numeros_pares}")

def calcular_maximo_numeros_impares(lista:list)-> None:
    """
    - Esta funcion calcula el numero maximo de los numeros impares de una lista ingresada (con ayuda de la funcion "calcular_numeros_pares_impares").

    Args:
        lista (list): Este parametro ingresa una lista (predefinida).
    """

    for i in range(len(lista)):

        if calcular_numeros_pares_impares(lista[i]) == False:

            if i == 0 or lista[i] > numero_impar_maximo:
                numero_impar_maximo = lista[i]

    print(f"El numero impar mas grande es: {numero_impar_maximo}")

def imprimir_numeros_ingresados(lista:list)-> None:
    """
    - Esta funcion imprime los numeros ingresados de una lista con su posicion.

    Args:
        lista (list): Este parametro ingresa una lista (predefinida).
    """
    for i in range(len(lista)):
        posicion = i + 1
        print(f"En la posicion {posicion} se encuentra el numero {lista[i]}.")

def imprimir_numeros_pares(lista:list)-> None:
    """
    - Esta funcion imprime solo los numeros pares de una lista (con ayuda de la funcion "calcular_numeros_pares_impares").

    Args:
        lista (list): Este parametro ingresa una lista (predefinida).
    """
    for i in range(len(lista)):
        if calcular_numeros_pares_impares(lista[i]) == True:
            posicion = i + 1
            print(f"En la poisicion {posicion} se encontro el numero {lista[i]}.")

def imprimir_indices_impares(lista:list)-> None:
    """
    - Esta funcion imprime los numeros que estan en los indices impares de una lista (con ayuda de calcular_numeros_pares_impares).

    Args:
        lista (list): (predefinida)
    """
    for i in range(len(lista)):
        if calcular_numeros_pares_impares(i) == False:
            print(f"En el indice {i} se encontro el numero {lista[i]}.")


lista = [-1] * 10

ingreso = False

while True:
    print("""
        A- Pedir el ingreso de 10 números enteros entre -1000 y 1000. 
        B- Mostrar la cantidad de números positivos y negativos.
        C- Mostrar la sumatoria de los números pares.
        D- Informar el mayor de los números impares.
        E- Imprimir todos los números ingresados.
        F- Imprimir todos los números pares.
        G- Imprimir los números de los índices impares.  
        H- Salir.
          """)
    letra = input("Ingrese una selecccion: ")
    letra = letra.upper()
    
    while letra != "A" and letra != "B" and letra != "C" and letra != "D" and letra != "E" and letra != "F" and letra != "G" and letra != "H":
        letra = input("ERROR. Ingrese una selecccion valida: ")
        letra = letra.upper()
        
    match letra:
        case "A":
            ingresar_numeros_enteros(lista)
            ingreso = True
        case "B":
            if ingreso == True:
                contador_positivos_negativos(lista)
            else:
                print("Error, primero debe ingresar los datos (opcion A).")
        case "C":
            sumar_numeros_pares(lista)
        case "D":
            calcular_maximo_numeros_impares(lista)
        case "E":
            imprimir_numeros_ingresados(lista)
        case "F":
            imprimir_numeros_pares(lista)
        case "G":
            if ingreso == True:
                imprimir_indices_impares(lista)
            
        case "H":
            print("¡Gracias por usar nuestro sistema!")
            break