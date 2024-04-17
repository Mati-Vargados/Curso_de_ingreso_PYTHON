from input import get_int

def sumar_naturales(numero: int) -> int:
    
    if numero == 1:
        resultado = 1
    else:
        resultado = numero + sumar_naturales(numero - 1)

    return resultado


numero = get_int("Ingrese un numero natural para sumar: ", "ERROR, reingrese el numero porfavor: ", 1, 230, 3)

print(f"La suma de los numeros naturales es: {sumar_naturales(numero)}")


def calcular_potencia(base: int, exponente:int) -> int:
    
    if exponente == 0:
        return 1
    
    return base * calcular_potencia(base, exponente - 1)


base = get_int("Ingrese un numero base: ", "ERROR, reingrese el numero porfavor: ", 1, 230, 3)

exponente = get_int("Ingrese un numero exponente: ", "ERROR, reingrese el numero porfavor: ", 1, 230, 3)

print(f"La porencia: {calcular_potencia(base, exponente)}")