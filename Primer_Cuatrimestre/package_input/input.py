from validate import validate_number

def get_int(mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int) -> int | None:

    numero = input(mensaje)
    numero = int(numero)
    numero = validate_number(numero, mensaje_error, minimo, maximo, reintentos, "int")

    return numero 




def get_float() -> float:

    numero = input("Ingrese un numero flotante")
    numero = float(numero)

    return numero




def get_str() -> str:

    cadena = input("Ingrese un id (menor a 5 caracteres): ")

    return cadena

