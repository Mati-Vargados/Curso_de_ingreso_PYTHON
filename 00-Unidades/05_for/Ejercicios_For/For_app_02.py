import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: for_02
---
Enunciado 1 : De 5  personas que ingresan al hospital se deben tomar y validar los siguientes datos.

nombre , 
temperatura, entre 35 y 42 
sexo( f, m , nb ) 
edad(mayor a 0)

pedir datos por prompt y mostrar por print

Punto A-informar cual fue el sexo mas ingresado

Punto B-el porcentaje de personas con fiebre y el porcentaje sin fiebre

Punto C - por el número de DNI del alumno

DNI terminados en  8 o 9
1))informar la cantidad de personas menores de edad (menos de 18 años)
2)la temperatura promedio en total de todas las personas menores de edad
3) el nombre de la persona de sexo  femenino  con la temperatura mas baja(si la hay)

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
        
        cantidad_femeninos = 0

        cantidad_masculino = 0

        contador_con_fiebre = 0

        contador_sin_fiebre = 0

        cantidad_no_binario = 0

        cantidad_de_menores = 0

        temperatura_total = 0

        


        for i in range(1, 5 + 1):

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

            # A-informar cual fue el sexo mas ingresado
            match sexo:
                case "f":
                    cantidad_femeninos = cantidad_femeninos + 1 
                    #3) el nombre de la persona de sexo  femenino  con la temperatura mas baja(si la hay)
                    if cantidad_femeninos == 1 or temperatura < temperatura_minima:
                        temperatura_minima = temperatura
                        nombre_femenino_temperatura_minima = nombre

                case "m":
                    cantidad_masculino = cantidad_masculino + 1
                case "nb":
                    cantidad_no_binario = cantidad_no_binario + 1

            #B-el porcentaje de personas con fiebre y el porcentaje sin fiebre
            if temperatura > 37:
                contador_con_fiebre = contador_con_fiebre + 1
            else:
                contador_sin_fiebre = contador_sin_fiebre + 1

            #1))informar la cantidad de personas menores de edad (menos de 18 años)
                
            if edad < 18:
                cantidad_de_menores = cantidad_de_menores + 1 

                #2)la temperatura promedio en total de todas las personas menores de edad
                temperatura_total = temperatura_total + temperatura
            


        # A-informar cual fue el sexo mas ingresado
        if cantidad_femeninos > cantidad_masculino and cantidad_femeninos > cantidad_no_binario:
            sexo_mas_ingresado = "El sexo mas ingresado es f"
        elif cantidad_femeninos > cantidad_no_binario:
            sexo_mas_ingresado = "El sexo mas ingresado es m"
        else:
            sexo_mas_ingresado = "El sexo mas ingresado es nb"
        
        #B-el porcentaje de personas con fiebre y el porcentaje sin fiebre
        contador_total_fiebre = contador_con_fiebre + contador_sin_fiebre
        
        porcentaje_contador_con_fiebre = (contador_con_fiebre * 100) / contador_total_fiebre

        porcentaje_contador_sin_fiebre = (contador_sin_fiebre * 100) / contador_total_fiebre
        
        print(sexo_mas_ingresado)

        print(f"Hay un {porcentaje_contador_con_fiebre}% de personas con fiebre y un {porcentaje_contador_sin_fiebre}% sin.")

        print(f"Hay {cantidad_de_menores} perosnas menores de edad")

        #2)la temperatura promedio en total de todas las personas menores de edad
        if cantidad_de_menores > 0:
            promedio = temperatura_total / cantidad_de_menores
            print(f"El promedio de la temperatura en menores de edad es de {promedio}°")
        
        if nombre_femenino_temperatura_minima != None:
            print(f"El nombre de la femenina con la temperatura mas baja es {nombre_femenino_temperatura_minima}")

            
       
            

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()