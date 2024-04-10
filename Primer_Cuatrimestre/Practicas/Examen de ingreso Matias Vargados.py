import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Matias
apellido: Vargados
---
Examen de ingreso - Programacion 
---
Enunciado:
Enunciado:
De 5 mascotas que ingresan a una veterinaria se deben tomar y validar los siguientes datos.
Nombre
Tipo (gato ,perro o exotico)
Peso ( entre 10 y 80)
Sexo( F o M )
Edad(mayor a 0)

Pedir datos por prompt y mostrar por print, se debe informar:
Informe A- Cuál fue el tipo mas ingresado (gato ,perro o exotico)
Informe B- El porcentaje de mascotas femeninas y el de las masculinas.
Informe C -El tipo de la mascota más pesada
Informe D- El nombre del gato más joven
Informe E- El promedio de peso de todas las mascotas
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):

        contador_perro = 0

        contador_gato = 0

        contador_exotio = 0

        contador_femeninos = 0

        contador_masculinos = 0

        acumulador_peso_total = 0
        
        for i in range(5):

            nombre = input("Ingrese su nombre: ")

            tipo = input("Ingrese tipo: ")
            tipo = tipo.upper()
            while tipo != "GATO" and tipo != "PERRO" and tipo != "EXOTICO": 
                tipo = input("Reingrese tipo: ")
                tipo = tipo.upper()
            
            peso = input("Ingrese el peso de su mascotra (entre 10kg y 80kg): ")
            peso = float(peso)
            while peso < 10 or peso > 80:
                peso = input("Reingrese el peso de su mascotra (entre 10kg y 80kg): ")
                peso = float(peso)
            
            sexo = input("Ingrese el sexo del animal: ")
            sexo = sexo.upper()
            while sexo != "F" and sexo != "M":
                sexo = input("Reingrese el sexo del animal: ")
                sexo = sexo.upper()

            edad = input("Ingrese su edad: ")
            edad = int(edad)
            while edad < 0:
                edad = input("Ringrese su edad: ")
                edad = int(edad)


            match tipo:

                case "PERRO":
                    contador_perro = contador_perro + 1

                case "GATO":
                    contador_gato = contador_gato + 1 
                    if contador_gato == 1 or edad < edad_gato_mas_joven:
                        edad_gato_mas_joven = edad
                        nombre_gato_mas_joven = nombre

                case "EXOTICO":
                    contador_exotio = contador_exotio + 1
            

            match sexo:
                case "F":
                    contador_femeninos = contador_femeninos + 1 
                case "M":
                    contador_masculinos = contador_masculinos + 1


            if i == 0 or peso > peso_maximo:
                peso_maximo = peso 
                tipo_peso_maximo = tipo


            acumulador_peso_total = acumulador_peso_total + peso


        if contador_perro > contador_gato and contador_perro > contador_exotio:
            tipo_mas_ingresado = "perro"

        elif contador_gato > contador_exotio:
            tipo_mas_ingresado = "gato"
        
        else:
            tipo_mas_ingresado = "exotico"
        

        porcentaje_femeninos = (contador_femeninos * 100) / 5
        porcentaje_masculinos = (contador_masculinos * 100) / 5


        promedio_peso_total = acumulador_peso_total / 5


        print(f"El tipo de animal mas ingresado es {tipo_mas_ingresado}.")
        print(f"El porcentaje de animales de sexo femenino es del {porcentaje_femeninos}% y el de masculinos es del {porcentaje_masculinos}%.")
        print(f"La mascota mas pesada es un {tipo_peso_maximo} pesnado {peso_maximo}kg.")
        print(f"El nombre del gato mas joven es {nombre_gato_mas_joven} y su edad es de {edad_gato_mas_joven} años.")
        print(f"El promedio del peso de todos los animales es de {promedio_peso_total}kg.")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()