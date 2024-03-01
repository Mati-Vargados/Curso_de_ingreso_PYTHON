import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Examen de ingreso - Programacion 
---
Enunciado:

UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para su proximo desarrollo en python, 
que promete revolucionar el mercado. 
Las posibles aplicaciones son las siguientes: 
# Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA), 
# Internet de las cosas (IOT) o 
# Procesamiento de lenguaje natural (NLP).
Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:

Los datos a ingresar por cada encuestado son:
    * nombre del empleado
    * edad (no menor a 18)
    * genero (Masculino - Femenino - Otro)
    * tecnologia (IA, RV/RA, IOT)   
En esta opción, se ingresaran empleados hasta que el usuario lo desee.

Una vez finalizado el ingreso, mostrar:

    #!X 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
    #!X 2) - Tecnología que mas se votó.
    #!X 3) - Porcentaje de empleados por cada genero
    #!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.  
    #!X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
    #!X 6) - Nombre y género del empleado que voto por RV/RA con menor edad.

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        
        seguir = True

        contador_masculinos_iot_ia = 0

        contador_ia = 0

        contador_iot = 0

        contador_rv_ra = 0

        contador_masculino = 0

        contador_femenino = 0

        contador_otro = 0

        contador_empleados_iot_edades = 0

        edad_ia_femenino = 0

        contador_ia_femenino = 0

        edad_minima = 0



        while seguir:

            nombre = prompt("UTN", "Ingrese su nombre") 

            edad = prompt("UTN", "Ingrese su edad (no menor a 18)") 
            edad = int(edad)
            while edad < 18:
                edad = prompt("ERROR", "Reingrese su edad (no menor a 18)") 
                edad = int(edad)

            genero = prompt("UTN", "Ingrese su genero (Femenino, Masculino , Otro)")
            while genero != "Femenino" and genero != "Masculino" and genero != "Otro":
                genero = prompt("ERROR", "Reingrese su genero (Femenino, Masculino , Otro)")

            tecnologia = prompt("UTN", "Ingrese su tecnologia (IA, RV/RA, IOT)")
            while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
                tecnologia = prompt("ERROR", "Reingrese su tecnologia (IA, RV/RA, IOT)")

            

            #!X 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
            match genero:
                case "Masculino":
                    if tecnologia == "IOT" or tecnologia == "IA" and edad > 25 and edad <= 50:
                        contador_masculinos_iot_ia = contador_masculinos_iot_ia + 1
                    #!X 3) - Porcentaje de empleados por cada genero
                    contador_masculino = contador_masculino + 1
                case "Femenino":
                    contador_femenino = contador_femenino + 1
                case "Otro":
                    contador_otro = contador_otro + 1

            #!X 2) - Tecnología que mas se votó.
            match tecnologia:
                case "IA":
                    contador_ia = contador_ia + 1
                    #!X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
                    if genero == "Femenino":
                        edad_ia_femenino = edad_ia_femenino + edad
                        contador_ia_femenino = contador_ia_femenino + 1
                case "IOT":
                    contador_iot = contador_iot + 1
                    #!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.
                    if (edad > 18 and edad < 25) or (edad > 33 and edad < 42):
                        contador_empleados_iot_edades = contador_empleados_iot_edades + 1
                case "RV/RA": 
                    contador_rv_ra = contador_rv_ra + 1
                    #!X 6) - Nombre y género del empleado que voto por RV/RA con menor edad.
                    if edad < edad_minima or contador_rv_ra == 1:
                        edad_minima = edad
                        nombre_edad_minima_rv_ra = nombre
                        genero_edad_minima_rv_ra = genero

            seguir = question("UTN", "¿Desea ingresar a otra persona?")
            
        #!X 2) - Tecnología que mas se votó.
        if contador_ia > contador_iot and contador_ia > contador_rv_ra:
            teconologia_mas_votada = "IA"
        elif contador_iot > contador_rv_ra:
            teconologia_mas_votada = "IOT"
        else: 
            teconologia_mas_votada = "RV/RA"
        

        #!X 3) - Porcentaje de empleados por cada genero
        total_personas = contador_femenino + contador_masculino + contador_otro

        porcentaje_masculino = (contador_masculino * 100) / total_personas
        porcentaje_femenino = (contador_femenino * 100) / total_personas
        porcentaje_otro = (contador_otro * 100) / total_personas

        #!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.
        porcentaje_iot_edades = (contador_empleados_iot_edades * 100) / contador_iot

        print(f"Hay {contador_masculinos_iot_ia} empleados de genero masculino que votaron a IOT o IA de edades entre 25 y 50 años.")

        print(f"La tecnologia mas votada es {teconologia_mas_votada}.")

        print(f"Hay un {porcentaje_femenino}% de femeninos, un {porcentaje_masculino}% de masculinos y un {porcentaje_otro}% de otro.")
        
        print(f"El {porcentaje_iot_edades}% de personas que votaron IOT y su edad se encuentra entre 18 y 25 o entre 33 y 42.")

        #!X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
        if contador_ia_femenino > 0:
            promedio_ia_femenino = edad_ia_femenino / contador_ia_femenino
            print(f"El promedio de las edades de las personas femeninas que votaron IA: {promedio_ia_femenino}%.")

        #!X 6) - Nombre y género del empleado que voto por RV/RA con menor edad.
        if contador_rv_ra > 0:
            print(f"El nombre del empleado que voto RV/RA con menor edad es {nombre_edad_minima_rv_ra} y su genero es {genero_edad_minima_rv_ra}.")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()