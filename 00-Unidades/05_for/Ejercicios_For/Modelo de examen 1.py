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
Enunciado 1 : De 5  personas que ingresan al hospital se deben tomar y validar los siguientes datos.

nombre , 
temperatura, entre 35 y 42 
sexo( f, m , nb ) 
 edad(mayor a 0)

pedir datos por prompt y mostrar por print

Punto A-informar cual fue el sexo mas ingresado

Punto B-el porcentaje de personas con fiebre y el porcentaje sin fiebre

Punto C - por el número de DNI del alumno
DNI terminados en  0 o 1

C-1)informar la cantidad de personas de sexo  femenino
C-2) la edad promedio de  personas de sexo  masculino
C-3) el nombre de la persona la persona de sexo  nb con más temperatura(si la hay)

Todos los alumnos: 
B-informar cual fue el sexo mas ingresado
C-el porcentaje de personas con fiebre y el porcentaje sin fiebre
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        
        contador_femeninos = 0

        contador_masculinos = 0

        contador_no_binario = 0

        contador_personas_con_fiebre = 0

        contador_personas_sin_fiebre = 0

        acumulador_edad_masculino = 0

        temperatura_maxima_no_binario = 0


        for i in range(3):

            nombre = prompt("UTN", "Ingrese su nombre")

            temperatura = prompt("UTN", "Ingrese su temperatura (entre 35 y 42)")
            temperatura = float(temperatura)
            while temperatura < 35 or temperatura > 42:
                temperatura = prompt("ERROR", "Reingrese su temperatura (entre 35 y 42)")
                temperatura = float(temperatura)
            
            sexo = prompt("UTN", "Ingrese su sexo (f, m , nb)")
            while sexo != "f" and sexo != "m" and sexo != "nb":
                sexo = prompt("ERROR", "Reingrese su sexo (f, m , nb)")

            edad = prompt("UTN", "Ingrese su edad (mayo a 0)")
            edad = int(edad)
            while edad <= 0:
                edad = prompt("ERROR", "Reingrese su edad (mayo a 0)")
                edad = int(edad)
            # A-informar cual fue el sexo mas ingresado
            match sexo:
                case "f":
                    contador_femeninos = contador_femeninos + 1
                case "m":
                    contador_masculinos = contador_masculinos + 1
                    #C-2) la edad promedio de  personas de sexo  masculino
                    acumulador_edad_masculino = acumulador_edad_masculino + edad
                case "nb":
                    contador_no_binario = contador_no_binario + 1
                    #C-3) el nombre de la persona la persona de sexo  nb con más temperatura(si la hay)
                    if temperatura > temperatura_maxima_no_binario or contador_no_binario == 1:
                        temperatura_maxima_no_binario = temperatura
                        nombre_temperatura_maxima_no_binario = nombre


            # B-el porcentaje de personas con fiebre y el porcentaje sin fiebre
            if temperatura >= 37:
                contador_personas_con_fiebre = contador_personas_con_fiebre + 1 
            else:
                contador_personas_sin_fiebre = contador_personas_sin_fiebre + 1

        # A-informar cual fue el sexo mas ingresado
        if contador_femeninos > contador_masculinos and contador_femeninos > contador_no_binario:
            mensaje_sexo_mas_ingresado = "f"
        elif contador_masculinos > contador_no_binario:
            mensaje_sexo_mas_ingresado = "m"
        else:
            mensaje_sexo_mas_ingresado = "nb"

        #B-el porcentaje de personas con fiebre y el porcentaje sin fiebre
        contador_total_perosnas_temperatura = contador_personas_con_fiebre + contador_personas_sin_fiebre

        porcentaje_personas_con_fiebre = (contador_personas_con_fiebre * 100) / contador_total_perosnas_temperatura

        porcentaje_personas_sin_fiebre = (contador_personas_sin_fiebre * 100) / contador_total_perosnas_temperatura

        
        print(f"El sexo mas ingresado es {mensaje_sexo_mas_ingresado}.")

        print(f"Hay un {porcentaje_personas_con_fiebre}% de personas con fiebre y un {porcentaje_personas_sin_fiebre}% que no tienen fiebre.")

        #C-1)informar la cantidad de personas de sexo  femenino
        print(f"Hay {contador_femeninos} personas con sexo femenino ingresadas.")

        #C-2) la edad promedio de  personas de sexo  masculino
        if contador_masculinos > 0:
            promedio_edad_masculino = acumulador_edad_masculino / contador_masculinos
            print(f"El promedio de la edad de los masculinos es de {promedio_edad_masculino} años.")
            
        #C-3) el nombre de la persona la persona de sexo  nb con más temperatura(si la hay)
        if contador_no_binario > 0:
            print(f"La persona con maxima temperatura y de sexo nb se llama {nombre_temperatura_maxima_no_binario}.")
            
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()