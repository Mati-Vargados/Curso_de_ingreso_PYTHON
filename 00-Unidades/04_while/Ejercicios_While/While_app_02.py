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
Se nos ha solicitado desarrollar una aplicación para llevar registro de las entradas vendidas en el Estadio River 
Plate, para el concierto de Taylor Swift. Para ello, se solicitará al usuario la siguiente información al momento de 
comprar cada entrada:

Al presionar el voton se debera pedir la carga de los siguientes datos, hasta que el usuario lo desee:

Los datos que deberas pedir para los ventas son:
    * Nombre del comprador #
    * Edad (no menor a 16) #
    * Género (Masculino, Femenino, Otro) #
    * Tipo de entrada (General, Campo delantero, Platea) #
    * Medio de pago (Crédito, Efectivo, Débito) #
    * Precio de la entrada (Se debe calcular) #

Para cada venta, se calculará el total a pagar en función del tipo de entrada elegida, 
el medio de pago y su precio correspondiente. #

 * Lista de precios: 
        * General: $16000
        * Campo:   $25000
        * Platea:  $30000

Las entradas adquiridas con tarjeta de crédito tendrán un 20% de descuento sobre el 
precio de la entrada, mientras que las adquiridas con tarjeta de débito un 15%. #

Al finalizar la carga, el programa debera mostrar los siguientes informes:

    #! 1) - Determina el género más frecuente entre las personas que compraron entradas de tipo "Campo".
    #! 2) - Determina cuántas personas compraron entradas de tipo "General" pagando con tarjeta 
    #!          de crédito y su edad promedio.
    #! 3) - Calcula el porcentaje de personas que compraron entradas de tipo "Platea" y 
    #!          pagaron con tarjeta de débito  respecto al total de personas en la lista.
    #! 4) - Cuál es el total de descuentos en pesos que aplicó la empresa, pero solo de 
    #!          los aplicados a tarjetas de crédito
    #! 5) - El nombre y la edad de la persona que pagó el precio más alto por una entrada de 
    #!          tipo "General" y pagó con tarjeta de débito (Solo la primera que se encuentre)
    #! 6) - La cantidad de personas que compraron entradas de tipo "Platea" y cuya 
    #!          edad es un número primo.
    #! 7) - Calcula el monto total recaudado por la venta de entradas de tipo "Platea" y 
    #!          pagadas con tarjeta de debito por personas cuyas edades son múltiplos de 6.
'''
class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Datos del usuario", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):

        blucle = True

        general = 16000
        campo = 25000
        platea = 30000

        contador_campo_masculino = 0
        contador_campo_femenino = 0
        contador_campo_otro = 0 

        cantidad_personas_pagaron_general_credito = 0
        edad_personas_general_credito = 0

        contador_platea = 0
        contador_platea_debito = 0

        contador_campo = 0

        contador_general = 0

        descuento_total = 0 

        bandera_debito = True

        contador_numeros_primos_platea = 0

        platea_credito = 0
        platea_debito = 0
        platea_efectivo = 0

        while blucle == True:
               
            nombre = prompt("UTN", "Ingrese su nombre: ")

            edad = prompt("UTN", "Ingrese su edad: ")
            edad = int(edad)
            while edad <= 16:
                edad = prompt("UTN", "Reingrese su edad: ")
                edad = int(edad)

            genero = prompt("UTN", "Ingrese su genero (Masculino, Femenino, Otro): ")
            while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
                genero = prompt("ERROR", "Reingrese su genero (Masculino, Femenino, Otro): ")

            entrada = prompt("UTN", "Ingrese su tipo de entrada (General, Campo delantero, Platea): ")
            while entrada != "General" and general != "Campo delantero" and general != "Platea":
                entrada = prompt("ERROR", "Reingrese su tipo entrada (General, Campo delantero, Platea): ")
 
            metodos_pagos =  prompt("UTN", "Ingrese su medio de pago (Credito, Efectivo, Debito): ")
            while metodos_pagos != "Creditos" and metodos_pagos != "Efectivo" and metodos_pagos != "Debito":
                metodos_pagos = prompt("ERROR", "Reingrese su medio de pago (Credito, Efectivo, Debito): ")
 


        
         
            match entrada:

                
                
                case "General":

                    contador_general += 1 

                    match metodos_pagos:
                        case "Credito":
                            general -= (general * 0.2)
                            cantidad_personas_pagaron_general_credito += 1
                            edad_personas_general_credito += edad
                        case "Debito":
                            general -= (general * 0.15)
                            if bandera_debito == True:
                                guardar_nombre_debito = nombre 
                                guardar_edad_debito = edad
                                bandera_debito = False
                        case "Efectivo":
                            general -= (general * 0)

                    
                case "Campo delantero":

                    contador_campo += 1 

                    match metodos_pagos:
                        case "Credito":
                            campo -= (campo * 0.2)
                        case "Debito":
                            campo -= (campo * 0.15)
                        case "Efectivo":
                            campo -= (campo * 0)

                    match genero:

                        case "Masculino":
                            contador_campo_masculino += 1

                        case "Femenino":
                            contador_campo_femenino += 1
                        
                        case "Otro":
                            contador_campo_otro += 1
                
                case "Platea":
                    contador_platea += 1
                        
                    match metodos_pagos:
                        case "Credito":
                            platea_credito = platea - (platea * 0.2)
                        case "Debito":
                            platea_debito = platea - (platea * 0.15)
                            contador_platea_debito += 1
                        case "Efectivo":
                            platea_efectivo = platea - (platea * 0)

                    if edad % 2 != 0: #numeros primos
                        contador_numeros_primos_platea += 1

            blucle = question("UTN", "¿Desea ingrear a otra persona?")

           

            
            #7) - Calcula el monto total recaudado por la venta de entradas de tipo "Platea"  
       #   pagadas con tarjeta de debito por personas cuyas edades son múltiplos de 6.

            
           

        if contador_campo_masculino > contador_campo_femenino and contador_campo_masculino > contador_campo_otro:
            genero_frecuente_campo = "El genero mas frecuente en Campo delantero es el Masculino"
        elif contador_campo_femenino > contador_campo_otro:
            genero_frecuente_campo = "El genero mas frecuente en Campo delantero es el Femenino"
        else: 
            genero_frecuente_campo = "El genero mas frecuente en Campo delantero es otro"
            
        if cantidad_personas_pagaron_general_credito > 0:
            promedio_edad_personas_general_credito = edad_personas_general_credito / cantidad_personas_pagaron_general_credito
        else:
            cantidad_personas_pagaron_general_credito = 0
            promedio_edad_personas_general_credito = "0 ya que nadie realizo una compra"
        
        if contador_platea > 0:
            promedio_cantidad_personas_platea_debito = (contador_platea_debito * 100) / contador_platea
        else:
            promedio_cantidad_personas_platea_debito = 0

        if metodos_pagos == "Credito" and metodos_pagos != "Debito" and metodos_pagos != "Efectivo":
            descuento_en_pesos_general = general * contador_general
            descuento_en_pesos_campo = campo * contador_campo
            descuento_en_pesos_platea = platea * contador_platea
            descuento_total = descuento_en_pesos_general + descuento_en_pesos_campo + descuento_en_pesos_platea

        if entrada == "Platea":
            if edad % 6 == 0:
                monto_total_platea = platea_credito + platea_debito + platea_efectivo

        
                                        

        mensaje = f"{genero_frecuente_campo}. \nHay {cantidad_personas_pagaron_general_credito} personas que pagaron la entrada general en credito y el promedio de sus edades es {promedio_edad_personas_general_credito}. \nEl {promedio_cantidad_personas_platea_debito}% de personas fueron a platea y pagaron en debito. \n El total de descuento en tarjeta de credito es ${descuento_total}. \n El nombre de la persona que pago mas dinero con la tarjeta de debito por una entrada general es {guardar_nombre_debito} y tiene {guardar_edad_debito} años. \nHay {contador_numeros_primos_platea} personas que su edad es un numero primo. \nEl monto de las personas que su edad es multiplo de seis es de {monto_total_platea}"

        alert("UTN", mensaje)
            

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()