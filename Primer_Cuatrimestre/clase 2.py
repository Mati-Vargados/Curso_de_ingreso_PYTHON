#1- Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
#2- Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
#3- Crear una función que le solicite al usuario el ingreso de una cadena y la retorna. 
#4- Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables (que reciban el mensaje de pedido de datos por parámetro). Agregar validaciones.
#5- Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.
#6- Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.
#7- Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.
#8- Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.

#1______________________________________________________________________________________________

def numero_entero()-> int:

    """
    - Le solisitara al usuario que ingrese un numero entero (int).

    - No acepta parametros.

    - Devuelve el numero ingresado (con la variable "numero_1").

    """

    numero_1 = input("Ingrese el numero entero: ")
    numero_1 = int(numero_1)
    
    return numero_1

#2______________________________________________________________________________________________

def numero_flotante()-> float:

    """
    - Le solisitara un numero flotante (float) al usuario.

    - No acepta parametros.

    - Devuelve el numero ingresado (con la variable "numero_2").
    
    """

    numero_2 = input("Ingrese el numero flotante: ")
    numero_2 = float(numero_2)

    return numero_2

#3______________________________________________________________________________________________

def cadena()-> str:
    """
    - Se le pedira al usuario que ingrese un texto (str).

    - No acepta parametros.

    - Devuelve el texto ingresado (con la variable "texto_ingresar").
    
    """

    texto_ingresar = input("Ingrese un texto: ")

    return texto_ingresar

#4______________________________________________________________________________________________

def numero_entero_edad(mensaje_edad:str, rango_1:int, rango_2:int)-> int: 
    """

    - El mensaje sirve para avisar al que inicie el programa cuando tiene que ingresar su edad y los rangos
    son para ver los limites aproximado de una edad. Esta funcion sirve para validar la edad.

    - Se aceptan 3 parametros:
        - mensaje edad:str
        - rango_1:int
        - rango_2:int
    - Devuelve la edad validada (con la variable "numero_1").

    """
    numero_1 = input(mensaje_edad)
    numero_1 = int(numero_1)
    while numero_1 < rango_1 or numero_1 > rango_2:
        numero_1 = input(mensaje_edad)
        numero_1 = int(numero_1)

    return numero_1

mensaje_edad = "Ingrese su edad Por favor: "
edad = numero_entero_edad(mensaje_edad, 1, 115)

def numero_entero_altura(mensaje_altura:str, rango_1:float, rango_2:float)-> float:
    """
    - Esta funcion marca la altura que ingrese una persona, partiendo de la base sobre posibles alturas realistas.

    - Acepta 3 parametros:
        - mensaje_altura:str
        - rango_1:int
        - rango_2:int

    - Devuelve la altura validada (con la variable "numero_1").
    """
    numero_1 = input(mensaje_altura)
    numero_1 = float(numero_1)
    while numero_1 < rango_1 or numero_1 > rango_2:
        numero_1 = input(mensaje_altura)
        numero_1 = float(numero_1)

    return numero_1

mensaje_altura = "Ingrese su altura Por favor: "
altura = numero_entero_altura(mensaje_altura, 0.1, 2.5)


def cadena_marca(mensaje_marca:str, marca_1:str, marca_2:str, marca_3:str)-> str:
    """
    - Esta funcion sirve para confirmar que tipo la marca de tu celular.

    - Acepta 3 parametros ricibidos por la variable "mensaje_marca":
        - mensaje_marca:str
        - marca_1:str
        - marca_2:str
        - marca_3:str

    - Devuelve la validacion de la marca seleccionada (usando la variable "marca").
    """

    marca = input(mensaje_marca)
    marca = marca.capitalize()
    while marca != marca_1 and marca != marca_2 and marca != marca_3:
        marca = input(mensaje_marca)
        marca = marca.capitalize()

    return marca

mensaje_marca = "Ingrese su marca de celular (Iphone, Samsung o Motorola): "
marca = cadena_marca(mensaje_marca, "Iphone", "Samsung", "Motorola")

#5______________________________________________________________________________________________

def calcular_area_circulo(radio:float)-> float:
    """
    - Sivre para informar sobre el area de un circulo.

    - Usa un solo parametro:
        - radio:float

    - Devuelve el area calculada (con la variable "area").
    """
    pi = 3.14
    area = pi * (radio * radio)

    return area 

radio = input("Ingrese el radio del circulo: ")
radio = float(radio)
area = calcular_area_circulo(radio)

#6______________________________________________________________________________________________

def par_impar() -> None:
    """
    - Sirve para indicar si el numero ingresado es par o impar.
    
    - No se ingreso ningun parametro.

    - No retorna nada.
    """
    numero_1 = input("Ingrese el numero par o impar: ")
    numero_1 = int(numero_1)

    if numero_1 % 2 == 0:
        mensaje = "Es par"
    else:
        mensaje = "Es impar"
    
    print(mensaje)

par_impar()

#7______________________________________________________________________________________________

def maximo_numeros()-> float:
    """
    - Se ingresan 3 numeros y de esos numeros se guarda el mas alto.

    - No se ingreso ningun parametro.

    - Se retorna el numero mas grande ingresado (usando la variable "numero_maximo").
    """
    for i in range(3):

        numero = input("Torneo numero maximo ")
        numero = float(numero)

        if i == 0 or numero > numero_maximo:
            numero_maximo = numero

    return numero_maximo 

maximo_numeros()

#8______________________________________________________________________________________________

def calcular_potencia_numero(numero_1:float, numero_2:float)-> float:
    """
    - Sirve para calcular la potencia de un numero ingresado el numero que lo eleve.

    - Hay 2 parametros que son recibidos por "numero_1" y "numero_2":
        - numero_1:float
        - numero_2:float

    - Devuelve la potencia del numero (con la variable "potencia_numero")
    """
    potencia_numero = numero_1 ** numero_2

    return potencia_numero

numero_1 = input("Ingrese el primer numero: ")
numero_1 = float(numero_1)

numero_2 = input("Ingrese la potencia para el numero anterior: ")
numero_2 = float(numero_2)

potencia_numero = calcular_potencia_numero(numero_1, numero_2)



