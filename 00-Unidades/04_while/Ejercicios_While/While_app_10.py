import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Matias 
apellido: Vargados
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). #

Luego calcular:
    A. La suma acumulada de los negativos

    B. La suma acumulada de los positivos

    C. Cantidad de números positivos ingresados

    D. Cantidad de números negativos ingresados
    
    E. Cantidad de ceros

    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        
        numero_positivo = 0 
        cantidad_numero_positivo = 0 

        numero_negativo = 0
        cantidad_numero_negativo = 0

        cantidad_ceros = 0 

        while True:

            numero = prompt("UTN", "Ingrese su numero")
            
            if numero == None:
                break
            
            numero = int(numero)

            if numero < 0:
                numero_negativo += numero
                cantidad_numero_negativo += 1 

            if numero > 0:
                numero_positivo += numero
                cantidad_numero_positivo += 1 

            if numero == 0:
                cantidad_ceros += 1

        
        diferencia_menos_mas = numero_negativo + numero_positivo

        alert("UTN", f"Hay {cantidad_ceros} ceros, {cantidad_numero_negativo} numeros negativos y {cantidad_numero_positivo} numeros positivos. Los negativos dan como resultado {numero_negativo}, los positivos {numero_positivo} y la diferencia des estos es de {diferencia_menos_mas}. ")
            


    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
