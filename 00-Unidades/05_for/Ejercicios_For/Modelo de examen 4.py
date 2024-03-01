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
DNI terminados en  2 o 3

C-1) informar la cantidad de personas de sexo  masculino
C-2) la edad promedio de  personas de sexo  nb
C-3) el nombre de la persona de sexo  femenino  con la temperatura mas baja(si la hay)

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

        acumulador_edad_no_binario = 0

        temperatura_minima_femenino = 0
        
        for i in range(5):

            nombre = prompt("UTN", "Ingrese su nombre")

            temperatura = prompt("UTN", "Ingrese su temperatura (entre 35 y 42)")
            temperatura = float(temperatura)
            while temperatura < 35 or temperatura > 42:
                temperatura = prompt("ERROR", "Reingrese su temperatura (entre 35 y 42)")
                temperatura = float(temperatura)

            sexo = prompt("UTN", "Ingrese su sexo (f, m , nb)")
            while sexo != "f" and sexo != "m" and sexo != "nb":
                sexo = prompt("ERROR", "Reingrese su sexo (f, m , nb)")

            edad = prompt("UTN", "Ingrese su edad (mayor a 0)") 
            edad = int(edad)
            while edad < 0:
                edad = prompt("ERROR", "Reingrese su edad (mayor a 0)") 
                edad = int(edad)

            #A-informar cual fue el sexo mas ingresado
            match sexo:
                case "f":
                    contador_femenino = contador_femenino + 1
                    #C-3) el nombre de la persona de sexo  femenino  con la temperatura mas baja(si la hay)
                    if temperatura < temperatura_minima_femenino or contador_femenino == 1:
                        temperatura_minima_femenino = temperatura
                        nombre_temperatura_minima_femenino = nombre

                case "m":
                    contador_masculino = contador_masculino + 1
                case "nb":
                    contador_no_binario = contador_no_binario + 1
                    acumulador_edad_no_binario = acumulador_edad_no_binario + edad

            #B-el porcentaje de personas con fiebre y el porcentaje sin fiebre
            if temperatura >= 37:
                contador_personas_con_fiebre = contador_personas_con_fiebre + 1
            else:
                contador_personas_sin_fiebre = contador_personas_sin_fiebre + 1

        #A-informar cual fue el sexo mas ingresado
        if contador_no_binario > contador_femenino and contador_no_binario > contador_masculino:
            sexo_mas_ingresado = "nb"
        elif contador_masculino > contador_femenino:
            sexo_mas_ingresado = "m"
        else:
            sexo_mas_ingresado = "f"
        
        #B-el porcentaje de personas con fiebre y el porcentaje sin fiebre
        total_personas = contador_personas_con_fiebre + contador_personas_sin_fiebre
        porcentaje_con_fiebre = (contador_personas_con_fiebre * 100) / total_personas
        porcentaje_sin_fiebre = (contador_personas_sin_fiebre * 100) / total_personas

        
        print(f"El sexo mas ingresado es: {sexo_mas_ingresado}.")

        print(f"El porcentaje de las personas con {porcentaje_con_fiebre}% y de las sin fiebre {porcentaje_sin_fiebre}%.")

        #C-1) informar la cantidad de personas de sexo  masculino
        print(f"Hay {contador_masculino} personas ingresadas con sexo masculino.")

        #C-2) la edad promedio de  personas de sexo  nb
        if contador_no_binario > 0:
            promedio_edad_no_binario = acumulador_edad_no_binario /contador_no_binario

            print(f"El promedio de las edades de los nb es: {promedio_edad_no_binario} años.")

        #C-3) el nombre de la persona de sexo  femenino  con la temperatura mas baja(si la hay)
        if contador_femenino > 0:
            print(f"El nombre de la perosna con sexo femenino es {nombre_temperatura_minima_femenino}.")
            

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()