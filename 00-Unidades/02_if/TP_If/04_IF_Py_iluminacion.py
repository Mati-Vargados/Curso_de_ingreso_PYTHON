import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Matias 
apellido: Vargados
---
TP: IF_Iluminacion
---
Enunciado:
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        
     def btn_calcular_on_click(self):
        marca = self.combobox_marca.get()
        cantidad = self.combobox_cantidad.get()
        cantidad_int = int(cantidad)

        descuento_uno = "Tengo un descuento del 50%"
        descuento_dos = "Tengo un descuento del 40%"
        descuento_tres = "Tengo un descuento del 30%"
        descuento_cuatro = "Tengo un descuento del 25%"
        descuento_cinco = "Tengo un descuento del 20%"
        descuento_seis = "Tengo un descuento del 15%"
        descuento_siete = "Tengo un descuento del 10%"
        descuento_ocho = "Tengo un descuento del 5%"

        precio_lampara = 800
        precio_cantidad = precio_lampara * cantidad_int

        descuento = 0
        mensaje_de_descuento = 0

        if cantidad_int == 3:
            if marca == "ArgentinaLuz":
                descuento = 0.15
                mensaje_de_descuento = descuento_seis
            elif marca == "FelipeLamparas":
                descuento = 0.10
                mensaje_de_descuento = descuento_siete
            else:
                descuento = 0.05
                mensaje_de_descuento = descuento_ocho
        elif cantidad_int == 4:
            if marca == "ArgentinaLuz" or marca == "FelipeLamparas":
                descuento = 0.25
                mensaje_de_descuento = descuento_cuatro
            else:
                descuento = 0.2
                mensaje_de_descuento = descuento_cinco
        elif cantidad_int == 5:
            if marca == "ArgentinaLuz":
                descuento = 0.4
                mensaje_de_descuento = descuento_dos
            else:
                descuento = 0.3
                mensaje_de_descuento = descuento_tres  
        elif cantidad_int >= 6:
                descuento = 0.5
                mensaje_de_descuento = descuento_uno 
        
        valor_final = precio_cantidad - (precio_cantidad * descuento)

        mensaje_de_descuento_adicional = ""

        if valor_final > 4000:
            descuento_adicional = 0.05
            valor_final = valor_final - (valor_final * descuento_adicional)
            mensaje_de_descuento_adicional = "Obtuviste un adicional del 5%"

        mensaje = f"Tu valor final es de {valor_final} y el descuento es de {mensaje_de_descuento}. {mensaje_de_descuento_adicional}"

        alert("UTN", mensaje)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()