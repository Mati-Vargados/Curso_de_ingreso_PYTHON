from informacion import lista_personajes

def stark_normalizar_datos(lista_personajes:list)-> bool:
    """Esta funcion analiza si hay un dato numerico tipo str y si lo hay lo cambia a int o float dependiendo el dato que pida.

    Args:
        lista_personajes (list): Recibe como parametro una lista llena de diccionarios.

    Returns:
        bool: Dependendiendo de si hubieron cambios en la lista por la funcion returna true | false.
    """
    valor_de_la_funcion = False

    for i in range(len(lista_personajes)):

        if type(lista_personajes[i]["altura"]) != float:

            lista_personajes[i]["altura"] = float(lista_personajes[i]["altura"])
            valor_de_la_funcion = True

        if type(lista_personajes[i]["peso"]) != float:

            lista_personajes[i]["peso"] = float(lista_personajes[i]["peso"])
            valor_de_la_funcion = True

        if type(lista_personajes[i]["fuerza"]) != int:

            lista_personajes[i]["fuerza"] = int(lista_personajes[i]["fuerza"])
            valor_de_la_funcion = True

    return valor_de_la_funcion


def obtener_dato(diccionario:dict, clave:str)-> None:

    retorno = diccionario[clave]

    if diccionario[clave] == "":
        retorno = False

    return retorno

def obtener_nombre(diccionario:dict)-> str | bool:

    retorno = "Nombre: " + diccionario.get("nombre", "")

    if diccionario.get("nombre") == None or diccionario["nombre"] == "" :
        retorno = False

    return retorno


def obtener_nombre_y_dato(diccionario:dict, clave:str)-> str:

    valor_clave = diccionario.get(clave)

    nombre = obtener_nombre(diccionario)

    retorno = f"{nombre} | {clave}: {valor_clave}"     

    if diccionario.get(clave) == None or diccionario[clave] == "" or nombre == False:
        retorno = False
    
    return retorno

print(obtener_nombre_y_dato(lista_personajes[0], "fuerza"))


def obtener_maximo(lista:list, clave:str):

    if lista != [] and (clave == int or clave == float):
        pass