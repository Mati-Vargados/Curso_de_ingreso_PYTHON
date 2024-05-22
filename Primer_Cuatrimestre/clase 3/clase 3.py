
#1________________________________________________________________________________________________________________
def solicitar_int(mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int)-> int|None:
    iteraciones = 0
   
    mensaje = input(mensaje)
    mensaje = int(mensaje)
    while (mensaje < minimo or mensaje > maximo):
        iteraciones = iteraciones + 1
        if iteraciones == reintentos:
            return None #corta la funcion
        mensaje = input(mensaje_error)
        mensaje = int(mensaje)
        
    
    return mensaje
    

solicitar_int("Ingrese su altura en cm: ", "ERROR. Reingrese su altura en cm: ", 1, 230, 3)


def solicitar_float(mensaje:str, mensaje_error:str, minimo:float, maximo:float, reintentos:float)-> float|None:
    iteraciones = 0
   
    mensaje = input(mensaje)
    mensaje = float(mensaje)
    while (mensaje < minimo or mensaje > maximo):

        iteraciones = iteraciones + 1
        if iteraciones == reintentos:
            return None #corta la funcion
        mensaje = input(mensaje_error)
        mensaje = float(mensaje)
        
    
    return mensaje
    

solicitar_float("Ingrese su altura en m: ", "ERROR. Reingrese su altura en m: ", 1, 230, 3)

#2________________________________________________________________________________________________________________

def ingresar_id(mensaje:str, mensaje_error:str, longitud:int,  reintentos:int) -> str | None:
    iteraciones = 0

    mensaje = input(mensaje)
    longitud = len(mensaje)

    while longitud > 5:
        iteraciones = iteraciones + 1
        if iteraciones == reintentos:
            return None #corta la funcion
        mensaje = input(mensaje_error)
        longitud = len(mensaje)
    
    return f"Tu id es {mensaje}"

ingresar_id("Ingrese su id (sin superar 5 caracteres): ", "ERROR. Reingrese su id (sin superar 5 caracteres): ", 5, 3)





