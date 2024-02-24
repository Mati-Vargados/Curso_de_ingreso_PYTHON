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

        numero = prompt("UTN", "Ingrese un numero")

        numero = int(numero)

        cantidad_primos = 0 #| 4) (si toma mas de un numero no es primo ya que se estaria dividiendo por mas numeros)
                         #10                    #|
        for i in range(2, numero + 1):          #| 1) hice un for que de 10 vueltas
            contador = 0                        #| 
                                                #|
            for j in range(2, i + 1):           #| 2) hice otro for para ver si es divisible por otros numeros
                if i % j == 0:                  #|      
                    contador += 1               #| 3) el contador tiene q tomar si el numero es divisible por si mismo  
            if contador < 2:                    #|
                cantidad_primos += 1            #|
                print(i)                        #|
        
        mensaje = f"Hay {cantidad_primos} numeros primos"

        alert("UTN", mensaje)

        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()