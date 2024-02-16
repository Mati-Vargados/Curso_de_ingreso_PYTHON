import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Matias 
apellido: Vargados
---
Ejercicio: while_06
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar 5 números mediante prompt. 
Calcular la suma acumulada y el promedio de los números ingresados. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_promedio

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_promedio = customtkinter.CTkEntry(master=self, placeholder_text="Promedio")
        self.txt_promedio.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):

        contador_interaciones = 0 
        acumuladores_numeros = 0 # no puedo recordarlos pero si acumularlo
        # antes del while
                
        while contador_interaciones < 5:
            # dentro del while
            numero = prompt("Ingreso", "Ingreso un numero")
            # "variable escalar"
            numero = int(numero)
            acumuladores_numeros = acumuladores_numeros + numero

            #promedio = acumuladores_numeros / 5

            contador_interaciones += 1
        
        #despues del while
        promedio = acumuladores_numeros / contador_interaciones

        self.txt_suma_acumulada.insert(0, acumuladores_numeros)

        self.txt_promedio.insert(0, promedio)  

              

            
            


        




    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
