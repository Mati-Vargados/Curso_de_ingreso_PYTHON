#La división de higiene está trabajando en un control de stock para productos sanitarios. Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe obtener los siguientes datos:
#El tipo (validar "barbijo", "jabón" o "alcohol")
#El precio: (validar entre 100 y 300)
#La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades)
#La marca y el Fabricante.
  
#Se debe informar lo siguiente:
#Del más caro de los barbijos, la cantidad de unidades y el fabricante.
#Del ingreso con más unidades, el fabricante.
#Cuántas unidades de jabones hay en total.

unidad_barijos = 0

acumulador_jabon = 0

unidad_alcohol = 0

unidad_barbijo_mas_caro = 0

for i in range(5):

    stock = input("Ingrese el tipo de prevencion para el contagio que necesite (barbijo, jabon o alcohol): ")
    while stock != "barbijo" and stock != "jabon" and stock != "alcohol":
        stock = input("Reingrese el tipo de stock que necesite (barbijo, jabon o alcohol): ")
    
    precio = input("Ingrese el precio (entre 100 y 300): ")
    precio = float(precio)
    while precio < 100 or precio > 300:
        precio = input("Reingrese el precio (entre 100 y 300): ")
        precio = float(precio)

    cantidad_unidades = input("Ingrese cantidad de unidades (mayor que 0 y menor de 1000): ")
    cantidad_unidades = int(cantidad_unidades)
    while cantidad_unidades <= 0 or cantidad_unidades > 1000:
        cantidad_unidades = input("Reingrese cantidad de unidades (mayor que 0 y menor de 1000): ")
        cantidad_unidades = int(cantidad_unidades)

    fabricante = input("Ingrese el fabricante del prodcuto (puede ser cualquiera): ")

    match stock:
        case "barbijo":
            unidad_barijos = unidad_barijos + 1 
            if unidad_barijos == 1 or precio > precio_barbijo_mas_caro:
                fabricante_barbijos_mas_caro = fabricante
                precio_barbijo_mas_caro = precio
                unidad_barbijo_mas_caro = cantidad_unidades

        case "jabon":
            acumulador_jabon = acumulador_jabon + cantidad_unidades
        
        case "alcohol":
            unidad_alcohol = unidad_alcohol + 1
    
    if i == 0 or cantidad_unidades > max_unidades:
        max_unidades = cantidad_unidades
        fabricante_con_mas_unidades = fabricante


print(f"El mas caros de los barbijos tienen una cantidad de: {unidad_barijos}, es fabricado por {fabricante_barbijos_mas_caro} y su precio es {precio_barbijo_mas_caro}.")

print(f"El fabricante que hizo mas unidades es: {fabricante_con_mas_unidades} y armo {max_unidades} unidades.")

print(f"Hay {acumulador_jabon} jabones.")

print("Gracias por usar nuestra empresa <3.")


