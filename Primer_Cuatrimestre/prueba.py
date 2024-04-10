#Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
#Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
#Crear una función que le solicite al usuario el ingreso de una cadena y la retorna. 
#Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables (que reciban el mensaje de pedido de datos por parámetro). Agregar validaciones.
#Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.
#Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.
#Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.
#Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.

def numero_entero()-> int:

    "Le solisitara al usuario que ingrese un numero entero (int)"

    numero_1 = input("Ingrese el numero entero: ")
    numero_1 = int(numero_1)
    
    return numero_1

def numero_flotante()-> float:

    "Le solisitara un numero flotante (float) al usuario"

    numero_2 = input("Ingrese el numero flotante: ")
    numero_2 = float(numero_2)

    return numero_2

def cadena()-> str:

    "Se le pedira al usuario que ingrese un texto (str)"

    texto_ingresar = input("Ingrese un texto: ")

    return texto_ingresar


def numero_entero_edad(mensaje_edad:str, rango_1:int, rango_2:int)-> int:

    numero_1 = input(mensaje_edad)
    numero_1 = int(numero_1)
    while numero_1 < rango_1 or numero_1 > rango_2:
        numero_1 = input(mensaje_edad)
        numero_1 = int(numero_1)

    return numero_1

mensaje_edad = "Ingrese su edad Por favor: "
edad = numero_entero_edad(mensaje_edad, 1, 115)


def numero_entero_altura(mensaje_altura:str, rango_1:float, rango_2:float)-> float:

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

#Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.

def area_circulo(radio:int)-> int:

    radio = input(radio)
    radio = int(radio)
    area = 3.14 * (radio * radio)

    return area 

mensaje_radio = "Ingrese el radio del circulo: "
area = area_circulo(mensaje_radio)

#Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar

def numero_entero()-> int:

    "Le solisitara al usuario que ingrese un numero entero (int)"

    numero_1 = input("Ingrese el numero entero: ")
    numero_1 = int(numero_1)
    
    return numero_1
