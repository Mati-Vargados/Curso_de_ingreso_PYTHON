import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: for_07
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):

        numero = prompt("UTN", "Ingrese un numero para determinar si es primo o no")
        numero = int(numero)
        
        bandera_divisor = False
        
        for i in range(2, numero): #cuenta desde el 2 hasta uno menos que el numero introducido 
            if numero % i == 0:
                bandera_divisor = True #si es divisor "no es primo"
                break
        if bandera_divisor == False: #si en el for no se encontro ni un solo divisor "es primo"
            mensaje = "es primo"
        else:
            mensaje = "no es primo"

        alert("UTN", mensaje)
                
            
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()