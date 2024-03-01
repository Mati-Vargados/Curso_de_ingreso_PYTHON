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

Un famoso casino de mar del plata,  requiere una app para controlar el egreso de dinero durante una jornada. Para ello se ingresa por cada ganador:

Nombre
Importe ganado (mayor o igual $1000)
Género (“Femenino”, “Masculino”, “Otro”)
Juego (Ruleta, Poker, Tragamonedas)


Necesitamos saber:
Nombre y género de la persona que más ganó.
Promedio de dinero ganado en Ruleta.
Porcentaje de personas que jugaron en el Tragamonedas.
Cuál es el juego menos elegido por los ganadores.

Promedio de importe ganado de las personas que NO jugaron Poker, siempre y cuando el importe supere los $15000

Porcentaje de dinero en función de cada juego

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):

        seguir = True

        importe_ganado_maximo = 0

        bandera_importe_maximo = 0

        contador_personas_ruleta = 0

        acumulador_dinero_ruleta = 0

        contador_personas_poker = 0 

        contador_personas_tragamonedas = 0

        acumulador_dinero_poker = 0

        acumulador_dinero_tragamonedas = 0 

        contador_personas_no_poker = 0

        acumulador_importe_ganado_no_poker = 0 

        while seguir:

            nombre = prompt("UTN", "Ingrese su nombre") 

            importe_ganado = prompt("UTN", "Ingrese su importe ganado (mayor o igual $1000)")
            importe_ganado = float(importe_ganado)
            while importe_ganado < 1000:
                importe_ganado = prompt("ERROR", "Reingrese su importe ganado (mayor o igual $1000)")
                importe_ganado = float(importe_ganado)

            genero = prompt("UTN", "Ingrese su genero (Femenino, Masculino , Otro)")
            while genero != "Femenino" and genero != "Masculino" and genero != "Otro":
                genero = prompt("ERROR", "Reingrese su genero (Femenino, Masculino , Otro)")

            juego = prompt("UTN","Ingrese el juego (Ruleta, Poker, Tragamonedas)")
            while juego != "Ruleta" and juego != "Poker" and juego != "Tragamonedas":
                juego = prompt("ERROR","Reingrese el juego (Ruleta, Poker, Tragamonedas)")
            
            #Nombre y género de la persona que más ganó.
            if importe_ganado > importe_ganado_maximo or bandera_importe_maximo == True:
                importe_ganado_maximo = importe_ganado
                nombre_importe_maximo = nombre
                genero_importe_maximo = genero
                bandera_importe_maximo = False

            match juego:
                case "Ruleta":
                    #Promedio de dinero ganado en Ruleta.
                    contador_personas_ruleta = contador_personas_ruleta + 1
                    acumulador_dinero_ruleta = acumulador_dinero_ruleta + importe_ganado
                case "Poker":
                    contador_personas_poker = contador_personas_poker + 1
                    acumulador_dinero_poker = acumulador_dinero_poker + importe_ganado
                case "Tragamonedas":
                    contador_personas_tragamonedas = contador_personas_tragamonedas + 1
                    acumulador_dinero_tragamonedas = acumulador_dinero_tragamonedas + importe_ganado

            #Cuál es el juego menos elegido por los ganadores.
            if contador_personas_ruleta < contador_personas_poker and contador_personas_ruleta < contador_personas_tragamonedas:
                juego_menos_elegido = "Ruleta"
            elif contador_personas_poker < contador_personas_tragamonedas:
                juego_menos_elegido = "Poker"
            else:
                juego_menos_elegido = "Tragamonedas"

            #Promedio de importe ganado de las personas que NO jugaron Poker, siempre y cuando el importe supere los $15000
            
            if juego != "Poker" and importe_ganado > 15000:
                contador_personas_no_poker = contador_personas_no_poker + 1
                acumulador_importe_ganado_no_poker = acumulador_importe_ganado_no_poker + importe_ganado

            seguir = question("UTN", "Desea ingresar a otra persona?")

        #Porcentaje de personas que jugaron en el Tragamonedas.
        cantidad_total_personas = contador_personas_ruleta + contador_personas_poker + contador_personas_tragamonedas
        porcentaje_personas_tragamonedas = (contador_personas_tragamonedas * 100) / cantidad_total_personas

        #Porcentaje de dinero en función de cada juego
        cantidad_total_dinero = acumulador_dinero_ruleta + acumulador_dinero_poker + acumulador_dinero_tragamonedas

        porcentaje_dinero_ganado_ruleta = (acumulador_dinero_ruleta * 100) / cantidad_total_dinero
        porcentaje_dinero_ganado_poker = (acumulador_dinero_poker * 100) / cantidad_total_dinero
        porcentaje_dinero_ganado_tragamonedas = (acumulador_dinero_tragamonedas * 100) / cantidad_total_dinero

        print(f"La perosona que mas gano se llama {nombre_importe_maximo} y su genero es {genero_importe_maximo}.")

        #Promedio de dinero ganado en Ruleta.
        if contador_personas_ruleta > 0:
            promedio_dinero_ruleta = acumulador_dinero_ruleta / contador_personas_ruleta
            print(f"El promedio del dinero ganado en ruleta es de ${promedio_dinero_ruleta}")
        
        print(f"El porcentaje de las personas que jugaron al tragamonedas es del {porcentaje_personas_tragamonedas}%.")

        print(f"El juego menos elegido es: {juego_menos_elegido}.")

        if contador_personas_no_poker > 0:
            promedio_importe_ganado_no_poker = acumulador_importe_ganado_no_poker / contador_personas_no_poker
            print(f"El promedio del importe ganado por las personas que no jugaron al poker y ganaron mas de $15.000 es de {promedio_importe_ganado_no_poker}.")

        print(f"El porcentaje del total dinero ganado de Ruleta es del {porcentaje_dinero_ganado_ruleta}%, el de Poker es del {porcentaje_dinero_ganado_poker}% y el de Tragamonedas es del {porcentaje_dinero_ganado_tragamonedas}%. ")

        


            
                
            

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()