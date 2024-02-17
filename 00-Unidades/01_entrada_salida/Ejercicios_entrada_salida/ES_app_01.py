import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import math

'''
nombre: Matias
apellido: Vargados
---
Ejercicio: entrada_salida_01
---
Enunciado:
Al presionar el  botón, se debe mostrar un mensaje como el siguiente "Esto no anda, funciona".
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        
       #costo 1 millon de km = 8 bitcoins

        destino = prompt("UTN", "Elegir entre Marte, Luna o Titan") 

        estacion_año = prompt("UTN", "Decinos una estacion del año (verano, primavera, otoño o invierno)")

        cantidad_personas = prompt("UTN", "¿Cuantas personas son?")

        cantidad_personas = int(cantidad_personas)

        bitcoin = 8 

        descuento_destino = 0 

        agrega_porcentaje_estacion = 0 

        match destino:

            case "Marte":
                valor = 60000000 * bitcoin

            case "Luna":
                valor = 500000 * (bitcoin / 2) # porque es medio millon 

            case "Titan":
                valor = 1300000000 * bitcoin

        if cantidad_personas >= 5:
                
                match destino:

                    case "Marte":
                        descuento_destino = 0.5

                        match estacion_año:

                            case "verano":
                                agrega_porcentaje_estacion = 0.1

                            case _:
                                agrega_porcentaje_estacion = 0.25

                    case "Luna":
                        descuento_destino = 0.4

                        match estacion_año:

                            case "verano":
                                agrega_porcentaje_estacion = 0.15

                            case _:
                                agrega_porcentaje_estacion = 0.25

                    case "Titan":
                        descuento_destino = 0.3

                        match estacion_año:

                            case "verano":
                                agrega_porcentaje_estacion = 0.1

                            case _:
                                agrega_porcentaje_estacion = 0.25    
        
        descuento_estetico = descuento_destino * 100 

        valor_descuento = valor - (valor * descuento_destino) 

        valor_sumado = valor_descuento + (valor_descuento * agrega_porcentaje_estacion)

        valor_final = valor_sumado * cantidad_personas #por las cantidades de personas

        valor_final /= 1000000

        alert("UTN", f"El valor final del viaje es {valor_final} M de Bitcoins, su descuento es del {descuento_estetico}%")
        
        


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

