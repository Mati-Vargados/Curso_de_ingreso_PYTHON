import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: For_UTN_Factory
---
Enunciado:
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        
        canidad_postulantes_NB = 0

        edad_minima_jr = 0

        bandera_nombre_edad_minima_jr = True

        contador_f = 0

        contador_m = 0

        contador_nb = 0

        suma_edades_f = 0

        suma_edades_m = 0

        suma_edades_nb = 0

        contador_teconolgia_asp = 0

        contador_teconolgia_js = 0

        contador_teconolgia_python = 0

        porcentaje_f = 0

        porcentaje_m = 0

        porcentaje_nb = 0

        for i in range(1, 4 + 1):

            nombre = prompt("UTN", "Ingrese su Nombre")

            edad = prompt("UTN", "Ingrese su edad")
            edad = int(edad)
            while edad < 18:
                edad = prompt("ERROR", "Reingrese su edad")
                edad = int(edad)

            genero = prompt("UTN", "Ingrese su genero (F-M-NB)")
            while genero != "F" and genero != "M" and genero != "NB":
                genero = prompt("ERROR", "Reingrese su genero (F-M-NB)")
            
            tecnologia = prompt("UTN", "Ingrese su tecnologia (PYTHON - JS - ASP.NET)")
            while tecnologia != "PYTHON" and tecnologia != "JS" and tecnologia != "ASP.NET":
                tecnologia = prompt("ERROR", "Reingrese su tecnologia (PYTHON - JS - ASP.NET)")

            puesto = prompt("UTN", "Ingrese su puesto (Jr - Ssr - Sr)")
            while puesto != "Jr" and puesto != "Ssr" and puesto != "Sr":
                puesto = prompt("ERROR", "Reingrese su puesto (Jr - Ssr - Sr)")

            #a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.

            if genero == "NB" and (tecnologia == "ASP.NET" or tecnologia == "JS") and (edad > 25 and edad < 40) and puesto == "Ssr":
                canidad_postulantes_NB += 1

            #b. Nombre del postulante Jr con menor edad.
                
            if puesto == "Jr" and (edad < edad_minima_jr or bandera_nombre_edad_minima_jr == True):
                edad_minima_jr = edad
                nombre_minima_jr = nombre 
                bandera_nombre_edad_minima_jr = False
            else:
                nombre_minima_jr = "´NO SE INGRESO NOMBRE´"

            #c. Promedio de edades por género.

            match genero:
                case "F":
                    contador_f += 1 
                    suma_edades_f += edad
                case "M":
                    contador_m += 1
                    suma_edades_m += edad
                case "NB":
                    contador_nb += 1
                    suma_edades_nb += edad
            
            #d. Tecnologia con mas postulantes (solo hay una).
                    
            match tecnologia:
                case "ASP.NET":
                    contador_teconolgia_asp += 1
                case "JS":
                    contador_teconolgia_js += 1
                case "PYTHON":
                    contador_teconolgia_python += 1


        #c. Promedio de edades por género.
                    
        promedio_f = suma_edades_f / contador_f

        promedio_m = suma_edades_m / contador_m

        promedio_nb = suma_edades_nb / contador_nb

         #d. Tecnologia con mas postulantes (solo hay una).
        
        if contador_teconolgia_asp > contador_teconolgia_js and contador_teconolgia_asp > contador_teconolgia_python:
            mensaje = "La tecnologia con mas populantes es ASP.NET."
        elif contador_teconolgia_js > contador_teconolgia_python:
            mensaje = "La tecnologia con mas populantes es JS."
        else:
            mensaje = "La tecnologia con mas populantes es PYTHON."

        #e. Porcentaje de postulantes de cada genero.
            cien_porciento_generos = contador_f + contador_m + contador_nb
            
            porcentaje_f = (contador_f * 100) / cien_porciento_generos
            porcentaje_m = (contador_m * 100) / cien_porciento_generos
            porcentaje_nb = (contador_nb * 100) / cien_porciento_generos
        

        print(f"Hay {canidad_postulantes_NB} postulantes de genero NB que programan en ASP.NET o JS cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.")
        print(f"El nombre del postulante Jr con menor edad es {nombre_minima_jr}.") 
        print(f"El promedio de edad en F es de {promedio_f} años, en M es {promedio_m} años y en NB es de {promedio_nb} años.")
        print(mensaje)
        print(f"Hay un {porcentaje_f}% de genero F, un {porcentaje_m}% de M y un {porcentaje_nb}% de NB.")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
