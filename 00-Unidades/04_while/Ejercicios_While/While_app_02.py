import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Matias
apellido: Vargados
---
Ejercicio: while_02
---
Enunciado:
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert 
10 repeticiones con números DESCENDENTE desde el 10 al 1
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        contador_interacion = 10 

        while contador_interacion > 0:
            alert("UTN", contador_interacion)
            contador_interacion = contador_interacion - 1 #decremento de la variable de control
            #contador_interacion -= 1
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()