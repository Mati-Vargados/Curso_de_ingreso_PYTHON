import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Matias
apellido: Vargados
---
 # Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar en la bolsa de valores: 
 # Para ello deberás programar el botón  para poder cargar 10 operaciones de compra con los siguientes datos:
 #   * Nombre
 #  * Monto en pesos de la operación (no menor a $10000)
 #   * Tipo de instrumento(CEDEAR, BONOS, MEP) 
 #   * Cantidad de instrumentos  (no menos de cero) 
    
 # Realizar los siguientes informes:
 
    #! 1) - Tipo de instrumento que menos se operó en total.
    #! 2) - Cantidad de usuarios que compraron entre 50  y 200 MEP 
    #! 3) - Cantidad de usuarios que no compraron CEDEAR 
    #! 4) - Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR
    #! 5) - Nombre y posicion del usuario que invirtio menos dinero
    #! 6) - Promedio de dinero en CEDEAR  ingresado en total.  
    #! 7) - Promedio de cantidad de instrumentos  MEP vendidos en total
'''



class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
       
    def btn_mostrar_iteracion_on_click(self):

        interaciones = 0

        cantidad_de_cedear = 0

        cantidad_de_bonos = 0

        cantidad_de_mep = 0

        cantidad_usuarios_compraron_mep = 0

        cantidad_de_iteraciones_bonos = 0

        cantidad_de_iteraciones_mep = 0

        while interaciones < 3:

            nombre = prompt("UTN", "Ingresa tu nombre")

            monto = prompt("UTN", "Ingrese su monto (mayor a $10 mil)")
            monto = float(monto)
            while monto < 10000:
                monto = prompt("UTN", "Reingrese su monto (mayor a $10 mil)")
                monto = float(monto)

            tipo_instrumento = prompt("UTN", "Ingrese el tipo de instrumento(CEDEAR, BONOS, MEP)")
            while tipo_instrumento != "CEDEAR" and tipo_instrumento != "BONOS" and tipo_instrumento != "MEP":
                tipo_instrumento = prompt("UTN", "Reingrese el tipo de instrumento(CEDEAR, BONOS, MEP)")
            
            cantidad_de_instrumentos = prompt("UTN", "Ingrese la cantidad de instrumento que quiera")
            cantidad_de_instrumentos = int(cantidad_de_instrumentos)
            while cantidad_de_instrumentos < 0:
                cantidad_de_instrumentos = prompt("ERROR", "Reingrese la cantidad de instrumento que quiera")
                cantidad_de_instrumentos = int(cantidad_de_instrumentos)
            

            match tipo_instrumento:
                case "CEDEAR":
                    cantidad_de_cedear += cantidad_de_instrumentos
                case "BONOS":
                    cantidad_de_bonos += cantidad_de_instrumentos
                    cantidad_de_iteraciones_bonos += 1
                case "MEP":
                    cantidad_de_mep += cantidad_de_instrumentos
                    cantidad_de_iteraciones_mep += 1
                    if cantidad_de_mep > 50 and cantidad_de_mep < 200:
                        cantidad_usuarios_compraron_mep += 1

                    
                
            interaciones += 1
            
        #1) - Tipo de instrumento que menos se operó en total.
            
        if cantidad_de_cedear < cantidad_de_bonos and cantidad_de_cedear < cantidad_de_mep:
            mensaje_cantidad_instrumentos = "El instrumento que menos se uso fue el CEDEAR"
        elif cantidad_de_bonos < cantidad_de_mep:
            mensaje_cantidad_instrumentos = "El instrumento que menos se uso fue el BONOS"
        else:
            mensaje_cantidad_instrumentos = "El instrumento que menos se uso fue el MEP"
     
        #3) - Cantidad de usuarios que no compraron CEDEAR 
            cantidad_de_usuarios_no_compraron_cedar = cantidad_de_iteraciones_bonos + cantidad_de_iteraciones_mep

            
        alert("UTN", f"{mensaje_cantidad_instrumentos} \nLa cantidad de usuarios que compraron entre 50 y 200 instrumentos MEP es {cantidad_usuarios_compraron_mep} \n")

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()