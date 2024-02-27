import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: for_04
---
Enunciado:
Al presionar el botón 'Mostrar' pedir 10 valores por prompt o 
hasta que el usuario ingrese el valor 9 (se deberá utilizar 'BREAK').
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):

        iteraciones = prompt("UTN", "Ingrese cantidad de ganadores")
        iteraciones = int(iteraciones)
        

        bandera_importe_ganado_maximo = True

        acumulador_dinero_ruleta = 0 

        contador_personas_ruleta = 0

        contador_personas_tragamonedas = 0

        contador_personas_poker = 0 

        acumulador_dinero_ruleta_mayor_quince_mil = 0

        acumulador_dinero_tragamonedas_mayor_quince_mil = 0

        contador_personas_ruleta_mayor_quince_mil = 0 

        contador_personas_tragamonedas_mayor_quince_mil = 0 
        
        acumulador_dinero_poker = 0

        acumulador_dinero_tragamonedas = 0 

        

        for i in range(iteraciones):

            nombre = prompt("UTN", "Ingrese su nombre")

            importe_ganado = prompt("UTN", "Ingrese su importe gando (mayor o igual $1000)")
            importe_ganado = int(importe_ganado)
            while importe_ganado < 1000:
                importe_ganado = prompt("ERROR", "Reingrese su importe gando (mayor o igual $1000)")
                importe_ganado = int(importe_ganado)

            genero = prompt("UTN", "Ingrese su genero (Femenino, Masculino, Otro)")
            while genero != "Femenino" and genero != "Masculino" and genero != "Otro":
                genero = prompt("ERROR", "Reingrese su genero (Femenino, Masculino, Otro)")

            juego = prompt("UTN", "Ingrese su Juego (Ruleta, Poker, Tragamonedas)")
            while juego != "Ruleta" and juego != "Poker" and juego != "Tragamonedas":
                juego = prompt("ERROR", "Reingrese su Juego (Ruleta, Poker, Tragamonedas)")

            #Nombre y género de la persona que más ganó.
            if bandera_importe_ganado_maximo == True or importe_ganado > importe_ganado_maximo:
                importe_ganado_maximo = importe_ganado
                nombre_importe_ganado_maximo = nombre
                genero_importe_ganado_maximo = genero 
                bandera_importe_ganado_maximo = False
            

            match juego:
                #Promedio de dinero ganado en Ruleta.
                case "Ruleta":
                    contador_personas_ruleta = contador_personas_ruleta + 1
                    acumulador_dinero_ruleta = acumulador_dinero_ruleta + importe_ganado
                    if importe_ganado > 15000:
                        acumulador_dinero_ruleta_mayor_quince_mil = acumulador_dinero_ruleta_mayor_quince_mil + importe_ganado
                        contador_personas_ruleta_mayor_quince_mil = contador_personas_ruleta_mayor_quince_mil + 1 

                case "Tragamonedas":
                    contador_personas_tragamonedas = contador_personas_tragamonedas + 1
                    acumulador_dinero_tragamonedas = acumulador_dinero_tragamonedas + importe_ganado
                    if importe_ganado > 15000:
                        acumulador_dinero_tragamonedas_mayor_quince_mil = acumulador_dinero_tragamonedas_mayor_quince_mil + importe_ganado
                        contador_personas_tragamonedas_mayor_quince_mil = contador_personas_tragamonedas_mayor_quince_mil + 1

                case "Poker":
                    contador_personas_poker = contador_personas_poker + 1
                    acumulador_dinero_poker = acumulador_dinero_poker + importe_ganado

                                
            
        
        #Porcentaje de personas que jugaron en el Tragamonedas.
        contador_personas_total = contador_personas_tragamonedas + contador_personas_poker + contador_personas_ruleta

        porcentaje_personas_tragamonerdas = (contador_personas_tragamonedas * 100) / contador_personas_total

        #Cuál es el juego menos elegido por los ganadores.
        if contador_personas_poker < contador_personas_ruleta and contador_personas_poker < contador_personas_tragamonedas:
            juego_menos_elegido = "Poker"
        elif contador_personas_ruleta < contador_personas_tragamonedas:
            juego_menos_elegido = "Ruleta"
        else: 
            juego_menos_elegido = "Tragamonedas"
        
        #Porcentaje de dinero en función de cada juego
        contador_porcentaje_total_dinero = acumulador_dinero_ruleta + acumulador_dinero_poker + acumulador_dinero_tragamonedas

        porcentaje_dinero_ruleta = (acumulador_dinero_ruleta * 100) / contador_porcentaje_total_dinero

        porcentaje_dinero_poker = (acumulador_dinero_poker * 100) / contador_porcentaje_total_dinero

        porcentaje_dinero_tragamonedas = (acumulador_dinero_tragamonedas * 100) / contador_porcentaje_total_dinero
            
        print(f"La perosna que mas dinero gano se llama {nombre_importe_ganado_maximo} y su genero es {genero_importe_ganado_maximo}")
        #Promedio de dinero ganado en Ruleta.
        if contador_personas_ruleta > 0:
            promedio_ruleta = acumulador_dinero_ruleta / contador_personas_ruleta
            print(f"El promedio del dinero ganado en la Ruleta es de ${promedio_ruleta}")

        print(f"El porcentaje de las personas que jugaron al Tragamonedas es del {porcentaje_personas_tragamonerdas}%")

        print(f"El juego menos elegido es {juego_menos_elegido}")

        #Promedio de importe ganado de las personas que NO jugaron Poker, siempre y cuando el importe supere los $15000
        contador_personas_ruleta_tragamonedas = contador_personas_ruleta_mayor_quince_mil + contador_personas_tragamonedas_mayor_quince_mil
        acumulador_diero_ruleta_tragamonedas = acumulador_dinero_ruleta_mayor_quince_mil + acumulador_dinero_tragamonedas_mayor_quince_mil

        if contador_personas_ruleta_tragamonedas > 0:
            promedio_ruleta_tragamonedas = acumulador_diero_ruleta_tragamonedas / contador_personas_ruleta_tragamonedas
            print(f"El promedio del importe ganados de las peronas que no jugaron al Poker y superan los $15000 ganados es de ${promedio_ruleta_tragamonedas}")

        print("UTN", f"El porcentaje de dinero de cada juego es: \nRuleta: {porcentaje_dinero_ruleta}% \nPoker: {porcentaje_dinero_poker}% \nTragamonedas: {porcentaje_dinero_tragamonedas}%")

    

        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()