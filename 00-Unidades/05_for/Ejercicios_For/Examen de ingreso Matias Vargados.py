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

        contador_gato = 0

        contador_perro = 0

        contador_exotico = 0

        contador_femenino = 0

        contador_masculino = 0

        peso_maximo = 0

        bandera_peso_maximo = True

        edad_minima_gato = 0

        acumulador_total_peso = 0

        for i in range(5):

            nombre = prompt("UTN", "Ingrese el nombre de su mascota")

            tipo_mascota = prompt("UTN", "Ingrese el tipo de mascota (gato ,perro o exotico)")
            while tipo_mascota != "gato" and tipo_mascota != "perro" and tipo_mascota != "exotico":
                tipo_mascota = prompt("ERROR", "Ingrese el tipo de mascota (gato ,perro o exotico)")
            
            peso = prompt("UTN", "Ingrese el peso de su mascota (entre 10 y 80)")
            peso = float(peso)
            while peso < 10 or peso > 80:
                peso = prompt("UTN", "Ingrese el peso de su mascota (entre 10 y 80)")
                peso = float(peso)

            
            sexo = prompt("UTN", "Ingrese el sexo de su mascota (F o M)")
            while sexo != "F" and sexo != "M":
                sexo = prompt("ERROR", "Ingrese el sexo de su mascota (F o M)")

            edad = prompt("UTN", "Ingrese la edad de su mascota (mayor que 0)")
            edad = int(edad)
            while edad < 0:
                edad = prompt("ERROR", "Ingrese la edad de su mascota (mayor que 0)")
                edad = int(edad)

            #Informe A- Cuál fue el tipo mas ingresado (gato ,perro o exotico)
            match tipo_mascota:
                case "gato":
                    contador_gato = contador_gato + 1
                    #D- El nombre del gato más joven
                    if edad < edad_minima_gato or contador_gato == 1:
                        edad_minima_gato = edad
                        nombre_edad_minima_gato = nombre
            
                case "perro":
                    contador_perro = contador_perro + 1
                    
                case "exotico":
                    contador_exotico = contador_exotico + 1
                    

            if tipo_mascota == "gato" or tipo_mascota == "perro" or tipo_mascota == "exotico":
                acumulador_total_peso = acumulador_total_peso + peso

            #El porcentaje de mascotas femeninas y el de las masculinas.
            match sexo:
                case "F":
                    contador_femenino = contador_femenino + 1
                case "M":
                    contador_masculino = contador_masculino + 1

            #C -El tipo de la mascota más pesada
            if peso > peso_maximo or bandera_peso_maximo == True:
                peso_maximo = peso
                tipo_mascota_mas_pesada = tipo_mascota
                bandera_peso_maximo = False

        #Informe A- Cuál fue el tipo mas ingresado (gato ,perro o exotico)
        if contador_gato > contador_perro and contador_gato > contador_exotico:
            tipo_mascota_mas_ingresada = "gato"
        elif contador_perro > contador_exotico:
            tipo_mascota_mas_ingresada = "perro"
        else:
            tipo_mascota_mas_ingresada = "exotico"

        #El porcentaje de mascotas femeninas y el de las masculinas.
        total_de_animales = contador_masculino + contador_femenino
        porcentaje_cantidad_animales_femenino = (contador_femenino * 100) / total_de_animales
        porcentaje_cantidad_animales_maculino = (contador_masculino * 100) / total_de_animales

        #E- El promedio de peso de todas las mascotas
        promedio_peso = acumulador_total_peso / total_de_animales

        print(f"El tipo de mascota mas ingresado es: {tipo_mascota_mas_ingresada}.")

        print(f"El porcentaje de los animales femeninos es del {porcentaje_cantidad_animales_femenino}% y el de los masculinos es del {porcentaje_cantidad_animales_maculino}%.")

        print(f"El tipo de mascota mas pesado es: {tipo_mascota_mas_pesada}.")

        #D- El nombre del gato más joven
        if contador_gato > 0:
            print(f"El nombre del gato mas joven es: {nombre_edad_minima_gato}.")

        print(f"El promedio del peso de todas las mascotas es: {promedio_peso}.")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()