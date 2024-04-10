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
    - Le solisitara al usuario que ingrese un numero entero (int)

    - No acepta parametros

    - Devuelve el numero ingresado

    """

    numero_1 = input("Ingrese el numero entero: ")
    numero_1 = int(numero_1)
    
    return numero_1

#2______________________________________________________________________________________________

def numero_flotante()-> float:

    """
    - Le solisitara un numero flotante (float) al usuario

    - No acepta parametros

    - Devuelve el numero ingresado
    
    """

    numero_2 = input("Ingrese el numero flotante: ")
    numero_2 = float(numero_2)

    return numero_2

#3______________________________________________________________________________________________

def cadena()-> str:
    """
    - Se le pedira al usuario que ingrese un texto (str)

    - No acepta parametros

    - Devuelve el texto ingresado
    
    """

    texto_ingresar = input("Ingrese un texto: ")

    return texto_ingresar

#4______________________________________________________________________________________________

def numero_entero_edad(mensaje_edad:str, rango_1:int, rango_2:int)-> int:
    """

    - El mensaje sirve para avisar al que inicie el programa cuando tiene que ingresar su edad y los rangos
    son para ver los limites aproximado de una edad. Esta funcion sirve para validar la edad.

    - Se aceptan 3 parametros (1 para la edad y otros dos para marcar los rangos de las edades)

    - Devuelve la edad validada

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

    - Acepta 3 parametros (Una sirve para avisar al que ejecute el programa cuando y donde tiene que ingresar su altura)
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

    texto_ingresar = input(mensaje_marca)
    texto_ingresar = texto_ingresar.capitalize()
    while texto_ingresar != marca_1 and texto_ingresar != marca_2 and texto_ingresar != marca_3:
        texto_ingresar = input(mensaje_marca)
        texto_ingresar = texto_ingresar.capitalize()

    return texto_ingresar

mensaje_marca = "Ingrese su marca de celular (Iphone, Samsung o Motorola): "
marca = cadena_marca(mensaje_marca, "Iphone", "Samsung", "Motorola")

#5______________________________________________________________________________________________

def area_circulo(radio:int)-> int:

    radio = input("Ingrese el radio del circulo: ")
    radio = int(radio)
    area = 3.14 * (radio * radio)

    return area 

mensaje_radio = "Ingrese el radio del circulo: "
area = area_circulo(mensaje_radio)

#6______________________________________________________________________________________________

def par_impar()-> int:

    numero_1 = input("Ingrese el numero par o impar: ")
    numero_1 = int(numero_1)

    if numero_1 % 2 == 0:
        print("Es par")
    else:
        print("Es impar")

par_impar()

#7______________________________________________________________________________________________

def maximo_numeros()-> float:

    for i in range(3):

        numero = input("Torneo numero maximo ")
        numero = float(numero)

        if i == 0 or numero > numero_maximo:
            numero_maximo = numero

    return numero_maximo 

maximo_numeros()

#8______________________________________________________________________________________________

def calcular_potencia_numera(numero_1:float, numero_2:float)-> float:

    potencia_numero = numero_1 ** numero_2

    return potencia_numero

numero_1 = input("Ingrese el primer numero: ")
numero_1 = float(numero_1)

numero_2 = input("Ingrese la potencia para el numero anterior: ")
numero_2 = float(numero_2)

potencia_numero = calcular_potencia_numera(numero_1, numero_2)


