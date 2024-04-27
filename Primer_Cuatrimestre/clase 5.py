#Escribir una función que recibe una lista de enteros, la misma calculará y devolverá el promedio de todos los números.

lista = [1, 2, 4, 4]


def promedio_numero(lista: list)-> int:
    """
    - Esta funcion recibe una lista de enteros, la misma calculará y devolverá el promedio de todos los números.
    - Usa como parametros:
        - lista: list
    - Retorna el promedio de los numeros ingresados 
    """
    numeros_listas = 0

    for i in range(len(lista)):
        numeros_listas = numeros_listas + lista[i] 
    
    promedio = numeros_listas / len(lista)

    return promedio


#Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.

def promedio_numero_positivo(lista: list)-> int:

    """
    - Esta funcion recibe una lista de enteros, la misma calculará y devolverá el promedio de todos los números positivos.
    - Usa como parametros:
        - lista: list
    - Retorna el promedio de los numeros postivos ingresados.
    """
    numeros_positivos = 0
    contador_numero_postivo = 0

    for i in range(len(lista)):
    
        numeros_listas = lista[i]

        if numeros_listas > 0:
            numeros_positivos = numeros_positivos + lista[i] 
            contador_numero_postivo = contador_numero_postivo + 1

    if contador_numero_postivo != 0:
        promedio_numero_positivo = numeros_positivos / contador_numero_postivo
    else:
        promedio_numero_positivo = 0

    return promedio_numero_positivo 

print(promedio_numero_positivo(lista))

#Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.

def multimplicacion_lista(lista: list)-> int:

    """
    - Esta funcion calcula y retorna el producto de todos los elementos de la lista que recibe como parámetro.
    - Usa como parametros:
        - lista: list
    - Retorna el producto de todos los elementos.
    """
    producto_numero_lista = 1

    for i in range(len(lista)):
        producto_numero_lista = producto_numero_lista * lista[i] 
    
    
    return producto_numero_lista


#Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.

def maximo_posicion(lista:list)-> int:
    """
    - Esta funcion recibe como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.
    
    - El parametro es lista:list y viene predefinida

    - Returna la posicion del valor maximo encontrado.
    """
    for i in range(len(lista)):
    
        if i == 0 or lista[i] > numero_maximo:
            numero_maximo = lista[i]
            posicion_numero_maximo = i

    return f"El numero mas grande es el {numero_maximo} y su posicion es {posicion_numero_maximo + 1}"


#Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.


def encontrar_varios_maximos(lista:list)-> None: #No devuelve nada
    """
    - Esta funcion recibe como parámetros una lista de enteros y muestre la/las posiciones (mediante un print) en donde se encuentra el valor máximo hallado.

    - Los parametros son:
        - lista: list (una lista predefinida)
    
    - No tiene un retorno (retorno = None).
    """
    for i in range(len(lista)):
    
        if i == 0 or lista[i] > numero_maximo:
            numero_maximo = lista[i]
    
    for i in range(len(lista)):
        
        if numero_maximo == lista[i]:
            posicion = i + 1
            print(f"El numero maximo es {numero_maximo} y se encontro en la posicion {posicion}")

encontrar_varios_maximos(lista)


# Escribe una función llamada reemplazar_nombres que reciba como parámetros una lista de nombres, un nombre a reemplazar y su correspondiente reemplazo. 
# La función debe reemplazar cada ocurrencia del nombre a reemplazar en la lista con su correspondiente reemplazo y luego retornar la cantidad total de reemplazos realizados.

lista_nombres = ["Mati", "Juan", "Thiago", "Santi"]

def reemplazar_nombres(lista_nombres: list, buscar: str, reemplazar: str)-> int:
    """
    - Esta funcion recibe como parámetros una lista de nombres, un nombre a reemplazar y su correspondiente reemplazo.

    - Los parametros son: (todas vienen predefinidas)
        - lista_nombres: list 
        - buscar: str
        - reemplazar: str
    
    - Returna el contador de cambios (con la variable contador_cambios)
    """
    contador_cambios = 0

    for i in range(len(lista_nombres)):

        if lista_nombres[i] == buscar:
            lista_nombres[i] = reemplazar
            contador_cambios = contador_cambios + 1
    
    return contador_cambios
            

reemplazar_nombres(lista_nombres, "Thiago", "Ben10")