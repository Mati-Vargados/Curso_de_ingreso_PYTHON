from input import get_int

#1_______________________________________________________________________________________________________________

def sumar_naturales(numero: int) -> int:
    
    if numero == 1:
        resultado = 1
    else:
        resultado = numero + sumar_naturales(numero - 1)

    return resultado


numero = get_int("Ingrese un numero natural para sumar: ", "ERROR, reingrese el numero porfavor: ", 1, 230, 3)

print(f"La suma de los numeros naturales es: {sumar_naturales(numero)}")

#2_______________________________________________________________________________________________________________

def calcular_potencia(base: int, exponente:int) -> int:
    
    if exponente == 0:
        return 1
    
    return base * calcular_potencia(base, exponente - 1)


base = get_int("Ingrese un numero base: ", "ERROR, reingrese el numero porfavor: ", 1, 230, 3)

exponente = get_int("Ingrese un numero exponente: ", "ERROR, reingrese el numero porfavor: ", 1, 230, 3)

print(f"La porencia: {calcular_potencia(base, exponente)}")

#3_______________________________________________________________________________________________________________

def sumar_digitos(numero:int)->int:

    numero = str(numero)
    longitud = len(numero)
    numero = int(numero)

    if longitud == 1:
   #if numero < 10:
        return numero
    
    fraccion = numero % 10

    numero = numero // 10

    suma_digitos = fraccion + sumar_digitos(numero)

    return suma_digitos


numero = get_int("Ingrese un numero: ", "ERROR, reingrese el numero porfavor: ", 1, 230, 3)

print(f"La suma de los digitos es: {sumar_digitos(numero)}")