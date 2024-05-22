from calculos import *
from validaciones_de_líneas_y_coches import *
from recaudos import *
from extras import *
from generacion_y_verificacion_de_existencia_de_legajo import *
from matrices import *

bandera_validar = False

while True: 

    menu = print("""
        A)Cargar planilla         
        B)Mostrar la recaudación de todos los coches y líneas.
        C)Calcular y mostrar recaudación por línea.
        D)Calcular y mostrar recaudación por coche.
        E)Calcular y mostrar la recaudación total.
        F)Salir""")

    

    seccion_menu = input("Ingrese la sección del menú que quieras usar: ")
    seccion_menu = seccion_menu.upper()

    while (seccion_menu != "A" and 
           seccion_menu != "B" and 
           seccion_menu != "C" and 
           seccion_menu != "D" and 
           seccion_menu != "E" and 
           seccion_menu != "F"):
        
        seccion_menu = input("ERROR. Reingrese la sección del menú que quieras usar: ")
        seccion_menu = seccion_menu.upper()

    match seccion_menu:
        
        case "A": 
            
            print("\nLegajos")
            crear_legajos(matriz_choferes)
           

            while True:
                mostrar_matriz(matriz_choferes)
                print("\nLineas e internos de colectivos")
                mostrar_matriz(matriz_colectivo)

                while validar_legajo(matriz_choferes) == False:
                    print("")

                almacenar_recaudos(matriz_colectivo, matriz_recaudo)

                continuar = input("Desea continuar agregando recaudos a otra linea/interno? Si/No: ")
                    
                continuar = continuar.upper()
                    
                if continuar == "NO":
                    break
            
            bandera_validar = True
            
        case "B":

            if bandera_validar == True :
                print("Lineas de colectivos:") 
                mostrar_matriz(matriz_colectivo)
                print("Recaudos:") 
                mostrar_matriz(matriz_recaudo)
            else:
                print("ERROR, PRIMERO DEBE INGRESAR LA OPCION ´A´")
            
        case "C":

            if bandera_validar == True :
                
                suma_filas(matriz_recaudo)
                
                
            else:
                print("ERROR, PRIMERO DEBE INGRESAR LA OPCION ´A´")
            
        case "D":

            if bandera_validar == True :
                
                mostrar_recaudacion_coche(matriz_recaudo, matriz_colectivo)

            else:
                print("ERROR, PRIMERO DEBE INGRESAR LA OPCION ´A´")
            
        case "E":

            if bandera_validar == True :
                
                mostrar_recaudacion_total(matriz_recaudo)

            else:
                print("ERROR, PRIMERO DEBE INGRESAR LA OPCION ´A´")

        case "F":
            print("¡Gracias por usar nuestros sistema!")
            break