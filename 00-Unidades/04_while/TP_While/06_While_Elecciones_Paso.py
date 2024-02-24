import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Matias
apellido: Vargados
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        
        candidato_mayor_votos = 0

        candidato_menor_votos = 0

        edad_candidato_promedio = 0

        edad_contador = 0

        cantidad_votos_total = 0 

        bandera = True

        bandea_edad = True

        while bandera == True:
            
            nombre_candidato = prompt("UTN", "Ingrese el candidato")

            edad_candidato = prompt("UTN", "Ingrese la edad del candidato")
            edad_candidato = int(edad_candidato)
            while edad_candidato < 25:
                edad_candidato = prompt("ERROR", "Reingrese la edad del candidato (acordate tener mayor de 25)")
                edad_candidato = int(edad_candidato)
            
            cantidad_votos = prompt("UTN", "Ingrese la cantidad de votos")
            cantidad_votos = int(cantidad_votos)
            while cantidad_votos < 0:
                cantidad_votos = prompt("ERROR", "Reingrese la cantidad de votos")
                cantidad_votos = int(cantidad_votos)
            
            if cantidad_votos > candidato_mayor_votos or bandea_edad == True:
                nombre_candidato_mayor_votos = nombre_candidato
                candidato_mayor_votos = cantidad_votos


            if cantidad_votos < candidato_menor_votos or bandea_edad == True:
                nombre_candidato_menor_votos = nombre_candidato
                candidato_menor_votos = cantidad_votos
                edad_menor_votos = edad_candidato
                bandea_edad = False

            edad_contador += 1
            edad_candidato_promedio += edad_candidato
             

            cantidad_votos_total += cantidad_votos

            bandera = question("UTN", "¿Desea ingresar a otro usuario?")
        
        promedio_edades = edad_candidato_promedio / edad_contador

        alert("UTN", f"El candidato con mas votos se llama {nombre_candidato_mayor_votos}. \nEl candidato con menos votos se llama {nombre_candidato_menor_votos} y tiene {edad_menor_votos} años. \nEl promedio de las edades es {promedio_edades}. \nHay en total {cantidad_votos_total} emitidos" )


        

        
        
            



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
