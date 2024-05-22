

def validate_number(numero: int | float, mensaje_error: str, minimo: int, maximo: int, reintentos: int, tipo_de_dato: str) -> int | float | None:
    
    iteraciones = 0

    while (numero < minimo or numero > maximo):

        iteraciones = iteraciones + 1

        if iteraciones == reintentos:
            return None #corta la funcion
        
        numero = input(mensaje_error)

        if tipo_de_dato == "int":
            numero = int(numero)
        else:
            numero = float(numero)
    
    return numero




def validate_length(cadena):

    pass