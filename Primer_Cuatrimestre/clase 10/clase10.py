"""
Crear una función que reciba por parámetro una cadena y un caracter.
La función deberá contar cuántas veces aparece dicho caracter en la cadena y retornar ese valor.
"""
def contador_caracter(cadena:str, carcater:str)-> int: 

    contador_caracter = 0

    for i in range(len(cadena)):
        if cadena[i] == carcater:
            contador_caracter += 1

    return contador_caracter

print(contador_caracter("tres tristes tigres comen trigo en un trigal", "t"))

"""
Crear una función que reciba una cadena y un caracter. 
La función deberá devolver el índice en el que se encuentre la primera incidencia de dicho caracter,
o -1 en caso de que no esté.
"""

def devolucion_caracter_encontrado(cadena:str, carcater:str) -> int:

    indice = -1

    for i in range(len(cadena)):
        if cadena[i] == carcater:
            indice =  i
            break

    return indice
        

print(devolucion_caracter_encontrado("HOLA", "L"))

"""
Crear una función que reciba una cadena y retorne la misma pero al reverso.
Ej:Si recibe la cadena “hola”, deberá retornar “aloh”.
"""

def devolver_cadena_inversa(cadena:str) -> str:

    cadena_reverso = ""

    i = len(cadena) - 1 

    while i > - 1:
        cadena_reverso += cadena[i]
        i -= 1

    return cadena_reverso

print(devolver_cadena_inversa("hola"))

"""
Crear una función que reciba como parámetro una cadena y suprima los caracteres repetidos.
Ej: Si recibe como parámetro la cadena “Hooola” debe devolver “Hola”.
"""
def suprimir_numeros_repetidos(cadena:str)-> str:
    cadena_suprimida = ""
    for i in range(len(cadena)- 1):

        if cadena[i] == cadena[i + 1]:
            cadena_suprimida += ""
        else:
            cadena_suprimida += cadena[i]

    cadena_suprimida += cadena[i + 1]

    return cadena_suprimida     

print(suprimir_numeros_repetidos("Holaaaaaa"))

"""
Crear una función que reciba una cadena por parámetro y suprima las vocales de la misma.
Ej: Si recibe como parámetro la cadena “Hola” debe devolver “Hl”.
"""
def detectar_vocales(letra:str)->bool:
    vocal = False
    letra = letra.upper()
    if (letra != "A" and 
        letra != "E" and 
        letra != "I" and 
        letra != "O" and 
        letra != "U"):
        vocal = True
    return vocal

def quitar_vocales_cadenas(cadena:str)-> str:

    cadena_sin_vocales = ""

    for i in range(len(cadena)):

        vocal = detectar_vocales(cadena[i])

        if vocal == False:
            cadena_sin_vocales += ""
        else:
            cadena_sin_vocales += cadena[i]

    return cadena_sin_vocales     

print(quitar_vocales_cadenas("pedro pedro pedro pedro pe"))

"""
Crear una función para contar cuántas veces aparece una subcadena dentro de una cadena.
Ej: Si recibe la cadena “El pan del panadero” y la subcadena “pan” deberá retornar el valor 2.
"""
def contador_subcadena(cadena:str, subcadena:str)-> int:
    
    contador_subcadena = 0               #slice
    for i in range(len(cadena)):
        if cadena [i: len(subcadena) + i] == subcadena:
            contador_subcadena += 1
    
    return contador_subcadena

print(contador_subcadena("pedro pedro pedro pedro pe", "pe"))