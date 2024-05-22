
# .strip() ______________________________________________________________

cadena = "##Hola mundo##"
print(cadena)
cadena = cadena.strip("#")
print(cadena)
print("--------------------------------------")

# .upper() ______________________________________________________________

cadena = "Hola"
print(cadena)
cadena = cadena.upper()
print(cadena)
print("--------------------------------------")

# .lower() ______________________________________________________________

cadena = "HOLA"
print(cadena)
cadena = cadena.lower()
print(cadena)
print("--------------------------------------")

# .capitalize() ______________________________________________________________

cadena = "hola MUNDO"
print(cadena)
cadena = cadena.capitalize()
print(cadena)
print("--------------------------------------")

# .replace() ______________________________________________________________

cadena = "Trueno | Sesión #1"
print(cadena)
cadena = cadena.replace("| Sesión ", "")
print(cadena)
print("--------------------------------------")

# .split() ______________________________________________________________

cadena = "Python,Java,C"
print(cadena)
cadena = cadena.split(",")
print(cadena)
print("--------------------------------------")

# .join() ______________________________________________________________

cadena = " | "
print(cadena)
cadena = cadena.join(['Python', 'Java', 'C'])
print(cadena)
print("--------------------------------------")

# .zfill() ______________________________________________________________

cadena = "Hola"
print(cadena)
cadena = cadena.zfill(8)
print(cadena)
print("--------------------------------------")

# .isalpha() ______________________________________________________________

cadena = "Hola"
print(cadena)
cadena = cadena.isalpha()
print(cadena)
print("--------------------------------------")

# .isnumeric() ______________________________________________________________

cadena = "123"
print(cadena)
cadena = cadena.isnumeric()
print(cadena)
print("--------------------------------------")

# .count() ______________________________________________________________

cadena = "pedro pedro pedro pedro pe"
print(cadena)
cadena = cadena.count("pe")
print(cadena)
print("--------------------------------------")

# .format() ______________________________________________________________

nombre = "Juan"
edad = "35"
cadena = "El nombre es: {1} y su edad es: {0}"
print(cadena)
cadena = cadena.format(edad, nombre)
print(cadena)
print("--------------------------------------")