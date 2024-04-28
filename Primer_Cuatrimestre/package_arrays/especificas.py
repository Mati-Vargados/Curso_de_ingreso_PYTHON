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

#------------------------------------------------------------------------------------------------------------------------------------------------------------

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

#------------------------------------------------------------------------------------------------------------------------------------------------------------
