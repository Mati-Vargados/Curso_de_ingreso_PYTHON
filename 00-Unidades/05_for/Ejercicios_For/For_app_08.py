import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: for_08
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número.
 Mostrar cada número primo entre 1 y el número ingresado
 informar la cantidad de números primos encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        
        numero = int(prompt("numero",""))

        cantidad_primos = 0  

        for i in range(2, numero+1):

            es_primo = True #el numero es primo hasta q se encuentre un divisor 

            for j in range(2, i): # para encontrar un divisor se hace otro for

                if i % j == 0: #esta sacando los divisores
                    es_primo = False  
                
            if es_primo: #dejando solamente los primos
                cantidad_primos += 1
                print(i)

        mensaje = f"cantidad de primos {cantidad_primos}"

        alert("",mensaje)
                
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()