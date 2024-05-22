class Boligrafo:
    def __init__(self, grosor_punta:str, color:str)-> None:
        
#-----------ATRIBUTOS--------------------------------------------------------------------------------------
        self.capacidad_tinta_maxima = 100
        self.grosor_punta = grosor_punta
        self.color = color
        self.cantida_tinta = 80

#------------METODOS---------------------------------------------------------------------------------------
    def escribir(self, texto:str)-> str:
                              # cantidad de caracteres = cantidad de tinta      
        longitud_caracteres = len(texto) #para saber cuanta tinta gasta texto

        mensaje = "No alcanza la tinta"

        if longitud_caracteres <= self.cantida_tinta:

            self.cantida_tinta -= longitud_caracteres #se resta la cantidad de tinta q se gasto

            mensaje = texto
        
        return mensaje
        
    def recargar(self, cantidad_tinta_ingresada:int)-> None:

        self.cantida_tinta += cantidad_tinta_ingresada

        mensaje = "Lapicera recargada"

        if self.cantida_tinta > self.capacidad_tinta_maxima:

            diferencia = self.cantida_tinta - self.capacidad_tinta_maxima

            self.cantida_tinta = self.capacidad_tinta_maxima

            mensaje = f"Se recargó la lapicera y sobró {diferencia} cantidad de tinta"

        return mensaje