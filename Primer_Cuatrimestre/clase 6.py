from package_arrays.array_generales import *

lista = [-1] * 10

ingreso = False

mensaje = print("Error, primero debe ingresar los datos (opcion A).")

while True:

    print("""
        A- Pedir el ingreso de 10 números enteros entre -1000 y 1000. 
        B- Mostrar la cantidad de números positivos y negativos.
        C- Mostrar la sumatoria de los números pares.
        D- Informar el mayor de los números impares.
        E- Imprimir todos los números ingresados.
        F- Imprimir todos los números pares.
        G- Imprimir los números de los índices impares.  
        H- Salir.
          """)
    
    letra = input("Ingrese una selecccion: ")
    letra = letra.upper()
    
    while letra != "A" and letra != "B" and letra != "C" and letra != "D" and letra != "E" and letra != "F" and letra != "G" and letra != "H":
        letra = input("ERROR. Ingrese una selecccion valida: ")
        letra = letra.upper()
        
    match letra:

        case "A":

            ingresar_numeros_enteros(lista)
            ingreso = True

        case "B":

            if ingreso == True:
                contador_positivos_negativos(lista)
            else:
                mensaje

        case "C":

            if ingreso == True:
                sumar_numeros_pares(lista)
            else:
                mensaje

        case "D":

            if ingreso == True:
                calcular_maximo_numeros_impares(lista)
            else:
                mensaje

        case "E":

            if ingreso == True:
                imprimir_numeros_ingresados(lista)
            else:
                mensaje

        case "F":

            if ingreso == True:
                imprimir_numeros_pares(lista)
            else:
                mensaje

        case "G":

            if ingreso == True:
                imprimir_indices_impares(lista)
            else:
                mensaje

        case "H":
            print("¡Gracias por usar nuestro sistema!")
            break