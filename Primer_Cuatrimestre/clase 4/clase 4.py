# def calcular_factorial(numero: int) -> int:
#     if numero == 1:
#         return 1
    
#     return numero * calcular_factorial(numero - 1)

# calcular_factorial(5)

def calcular_factorial(numero: int) -> int:
    if numero == 1:
        devolucion =  1
    else:
        devolucion =  numero * calcular_factorial(numero - 1)

    return devolucion

calcular_factorial(5)
