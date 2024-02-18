import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Matias
apellido: Vargados
---
Ejercicio: while_01
---
Enunciado:
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert 
10 repeticiones con números ASCENDENTE desde el 1 al 10
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        
        numero = prompt("UTN", "Ingrese un numero del 100 al 1000")

        numero = int(numero)

        contador_vueltas = 0 

        contador_numeros_pares = 0 

        contador_nultiplo_5 = 0

        suma_multiplos_100 = 0 

        suma_total = 0 


        while numero >= 100 and numero <= 1000: 

            if contador_vueltas == numero:
                break

            contador_vueltas += 1
            
            if contador_vueltas % 2 == 0:
                contador_numeros_pares += 1 

            if contador_vueltas % 5 == 0:
                contador_nultiplo_5 += 1 

            if contador_vueltas % 100 == 0:
                suma_multiplos_100 += contador_vueltas

            suma_total += contador_vueltas

            

        alert("UTN", f"Hay {contador_numeros_pares} numeros pares, {contador_nultiplo_5} multiplos de cinco, la suma de los divisibles por cien da {suma_multiplos_100} y la suma total de todos los numeros es de {suma_total}")
                


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()