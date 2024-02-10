import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Matias 
apellido: Vargados
---
Ejercicio: entrada_salida_02
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener un dato utilizando el Dialog Prompt
y luego mostrarlo utilizando el Dialog Alert
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
    #para saber el costo de un viaje necesitamos el siguiente algoritmo, sabiendo que el precio por kilo de pasajero es 1000 pesos. 
    #Se ingresan todos los datos por PROMPT los datos a solicitar de dos personas son, nombre, edad y peso se pide  armar el siguiente mensaje:
    #"hola german y marina , sus pesos son 80 kilos y 60 kilos respectivamente , sumados da 140 kilos , el promedio de edad es 33 y su viaje vale 140 000 pesos.  

        kilo_pasajero = 1000

        nombre_p1 = prompt("Pasajero 1", "Nombre del pasajero")

        edad_p1 = prompt("Pasajero 1", "Edad")
        edad_p1 = int(edad_p1)

        peso_p1 = prompt("Pasajero 1","Su peso")
        peso_p1 = float(peso_p1)

        nombre_p2 = prompt("Pasajero 2", "Nombre del pasajero")

        edad_p2 = prompt("Pasajero 2", "Edad")
        edad_p2 = int(edad_p2)

        peso_p2 = prompt("Pasajero 2","Su peso")
        peso_p2 = float(peso_p2)

        suma_de_kilos = peso_p1 + peso_p2

        resultado = suma_de_kilos * 1000

        promedio = (edad_p1 + edad_p2) / 2

        alert("UTN Aerolineas", f"hola {nombre_p1} y {nombre_p2}, sus pesos son {peso_p1} kilos y {peso_p2} kilos respectivamente , sumados da {suma_de_kilos} kilos , el promedio de edad es {promedio} y su viaje vale {resultado} pesos")






        

        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()