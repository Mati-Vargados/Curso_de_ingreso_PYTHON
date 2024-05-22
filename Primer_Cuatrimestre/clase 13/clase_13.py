lista = [1, 2, 3, 4, 1, 2, 3, 5]

tupla = tuple(lista) #Es inmutable
tupla = (1, 2, 3, 4) #Otra forma de representar la tupla

set_datos = set(lista) #Es inmutable y no tiene orden
set_datos = {1, 2, 3, 4, 1, 3, 4, 5} # = {1, 2, 3, 4, 5}
set_datos.add(6) # = {1, 2, 3, 4, 5, 6}
set_datos.discard(3) # = {1, 2, 4, 5, 6} | no rompe si el numero no existe / no esta ingresado
set_datos.remove(4) # = {1, 2, 5, 6} | si el numero no existe ´rompe´

print(set_datos)


diccionario = {'nombre': 'Juan', 
                'edad': 21, 
                'Ciudad': 'Buenos Aires'}

print(diccionario['nombre'])  
print(diccionario['edad'])   
print(diccionario["Ciudad"]) 

diccionario['nombre'] = "Pedro"
diccionario['edad'] = "25"
diccionario['Ciudad'] = "Mar del plata"
diccionario['Sexo'] = "Masculino" # Se le puede crear una clave pero si tratas de usar una clave q no existe rompe

print(diccionario) 

diccionario = {'a': 1, 'b': 2}
print(diccionario.get('a')) #1
print(diccionario.get('c')) #None porque no existe

diccionario = {'a': 1, 'b': 2}
diccionario.keys() #dict_keys(['a', 'b']) busca las claves
lista_claves = list(diccionario) #['a', 'b'] 
print(lista_claves)

diccionario = {'a': 1, 'b': 2}
diccionario.values() #dict_values([1, 2]) busca los valores
list(diccionario.values()) #[1, 2]

diccionario = {'a': 1, 'b': 2}
diccionario.pop('a', None) #1 si no lo encuentra busca el ultimo 
diccionario# = {'b': 2} # si no lo encuentra hay que darle un valor por retorno sino rompe

