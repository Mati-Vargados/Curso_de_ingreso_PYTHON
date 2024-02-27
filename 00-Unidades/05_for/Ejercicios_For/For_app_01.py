import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
nombre:
apellido:
---
Ejercicio: for_01
---
nunciado 1 : De 5  personas que ingresan al hospital se deben tomar y validar los siguientes datos.

nombre , 
temperatura, entre 35 y 42 
sexo( f, m , nb ) 
 edad(mayor a 0)

pedir datos por prompt y mostrar por print

Punto A-informar cual fue el sexo mas ingresado

Punto B-el porcentaje de personas con fiebre y el porcentaje sin fiebre

Punto C - por el número de DNI del alumno

DNI terminados en  6 o 7

C-1)informar la cantidad de personas mayores de edad (desde los 18 años)
C-2)la edad promedio en total de todas las personas mayores de edad (18 años)
C-3) el nombre de la persona de sexo  masculino con la temperatura mas baja(si la hay)


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

        contador_femenino = 0

        contador_masculino = 0
    
        contador_no_binario = 0

        contador_personas_con_fiebre = 0

        contador_personas_sin_fiebre = 0

        cantidad_de_adultos = 0

        edad_total_mayor = 0

        

        for i in range(1, 3 + 1):

            nombre = prompt("UTN", "Ingrese su nombre")

            temperatura = prompt("UTN", "Ingrese la temperatura (entre 35 y 42)")
            temperatura = float(temperatura)
            while temperatura < 35 or temperatura > 42:
                temperatura = prompt("ERROR", "Reingrese la temperatura (entre 35 y 42)")
                temperatura = float(temperatura)

            sexo = prompt("UTN", "Ingrese su sexo ( f, m , nb )")
            while sexo != "f" and sexo != "m" and sexo != "nb":
                sexo = prompt("ERROR", "Reingrese su sexo ( f, m , nb )")
            
            edad = prompt("UTN", "Ingrese edad (mayor a 0)")
            edad = int(edad)
            while edad < 0:
                edad = prompt("ERROR", "Reingrese edad (mayor a 0)")
                edad = int(edad)
            
            #Punto A-informar cual fue el sexo mas ingresado
            match sexo:
                case "f":
                    contador_femenino = contador_femenino + 1
                case "m":
                    contador_masculino = contador_masculino + 1
                    #C-3) el nombre de la persona de sexo  masculino con la temperatura mas baja(si la hay)
                    if contador_masculino == 1 or temperatura < temperatura_minima_hombre :
                        temperatura_minima_hombre = temperatura
                        nombre_temperatura_minima_hombre = nombre
                        
                    
                case "nb":
                    contador_no_binario = contador_no_binario + 1

            #Punto B-el porcentaje de personas con fiebre y el porcentaje sin fiebre
            if temperatura >= 37:
                contador_personas_con_fiebre = contador_personas_con_fiebre + 1
            else:
                contador_personas_sin_fiebre = contador_personas_sin_fiebre + 1
            
            #C-1)informar la cantidad de personas mayores de edad (desde los 18 años)
            if edad >= 18:
                cantidad_de_adultos = cantidad_de_adultos + 1
                #C-2)la edad promedio en total de todas las personas mayores de edad (18 años)
                edad_total_mayor = edad_total_mayor + edad
            
       #Punto A-informar cual fue el sexo mas ingresado
        if contador_femenino > contador_masculino and contador_femenino > contador_masculino:
            sexo_mas_ingresado = "f"
        elif contador_masculino > contador_no_binario:
            sexo_mas_ingresado = "m"
        else:
            sexo_mas_ingresado = "nb"

        #Punto B-el porcentaje de personas con fiebre y el porcentaje sin fiebre

        contador_personas_total = contador_personas_con_fiebre + contador_personas_sin_fiebre
        
        porcentaje_con_fiebre = (contador_personas_con_fiebre * 100) / contador_personas_total
        
        porcentaje_sin_fiebre = (contador_personas_sin_fiebre * 100) / contador_personas_total
                                # porcentaje si puede dar 0%

        print(f"El sexo mas ingresado fue {sexo_mas_ingresado}")

        print(f"Hay un {porcentaje_con_fiebre}% de personas con fiebre y un {porcentaje_sin_fiebre}% sin fiebre")

        print(f"Hay {cantidad_de_adultos} adultos")

        #C-2)la edad promedio en total de todas las personas mayores de edad (18 años)
        if cantidad_de_adultos > 0:
            promedio_edad_mayor = edad_total_mayor / cantidad_de_adultos
            print(f"El promedio de las personas mayores es de {promedio_edad_mayor} años")
        if nombre_temperatura_minima_hombre != None : 
            print(f"El nombre de la persona de sexo masculino con la temperatura mas baja es {nombre_temperatura_minima_hombre}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()