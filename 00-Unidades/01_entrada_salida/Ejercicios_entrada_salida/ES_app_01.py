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
        
        #AB = Diágonal mayor
        #DC = Diágonal menor
        #BD y BC = lados menores
        #AD y AC = lados mayores

        #Debemos tener en cuenta que la estructura del cometa estará dada por un perímetro de varillas de plástico y los correspondientes entrecruces (DC y AB) del mismo material para mantener la forma del cometa.
        #El cometa estará construido con papel de alta resistencia. La cola del mismo se construirá con el mismo papel que el cuerpo y representará un 10% adicional del necesario para el cuerpo.
        #Necesitamos saber cuántos Mts de varillas de plástico y cuántos de papel son necesarios para la construcción en masa de 10 cometas. Tener en cuenta que los valores de entrada están expresados en Cms.    
        
        diágonal_mayor = prompt("UTN", "Diagonal mayor")
        diágonal_mayor = float(diágonal_mayor)

        diágonal_menor = prompt("UTN", "Diagonal menor")
        diágonal_menor = float(diágonal_menor)

        lados_menores = prompt("UTN", "Lados menores")
        lados_menores = float(lados_menores)

        lados_mayores = prompt("UTN", "Lados mayores")
        lados_mayores = float(lados_mayores)

        perimetro_principal = (lados_mayores + lados_menores) * 2  #porque son 4 lados "bd", "bc", "ad", "ac"

        perimetro_secundario = diágonal_mayor + diágonal_menor

        perimetro_final = perimetro_principal + perimetro_secundario

        area = (diágonal_mayor * diágonal_menor) / 2 #es el papel

        cola = area * 0.1

        perimetro_total = (perimetro_final/ 100) * 10
        
        papel = area + cola 

        papel_total = (papel / 100) * 10
                                                                                                                    # area metros cuadrados

        alert("Cometa de Octavio", f"Necesitas {math.ceil(perimetro_total)}Mts de varillas, {math.ceil(papel_total)}Mts2 de cada color de papel para hacer 10 cometas")
                                                #el math lo redondea para arriba



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

