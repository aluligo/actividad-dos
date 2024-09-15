print("*********************************************************")
print("Ejercicio 1")
# Ejericio 1. Conversión de tipos de datos
entero = 100
decimal = 5.89
cadena = "Bienvenido a mi mundo Artificial"

print("Numero Entero:", entero, "Tipo:", type(entero))
print("Numero Decimal:", decimal, "Tipo:", type(decimal))
print("Cadena:", cadena, "Tipo:", type(cadena))

print("*********************************************************")
print("Ejercicio 2")
# Ejercio 2. Multilíneas de cadenas.
multilinea = """Esto es una práctica para el parcial
que será entregado el día 15 de septiembre del 2024
de la materia Electiva Profesional I"""
print("\nPRACTICA:\nElectiva Profesional I :")
print(multilinea)

print("*********************************************************")
print ("Ejercicio 3")
# Ejercicio 3. Función len(): Cuenta cuántos elementos hay en una cadena, palabra o ítems en una lista.
cadena = "Bienvenido a mi mundo Artificial"
print("\nLongitud de la cadena:", len(cadena))

print("*********************************************************")
print ("Ejercicio 4")
#Sub cadenas
#Obtiene los primeros n caracteres de una cadena.
cadena = "Bienvenido a mi mundo Artificial"
print("**** Obtiene los Primeros 10 caracteres ****:", cadena[:10])

#Obtiene los caracteres de en medio de una cadena.
cadena = "Bienvenido a mi mundo Artificial"
print("**** Obtiene los caracteres del medio ****:", cadena[13:21])

#Obtiene los últimos n caracteres de una cadena.
cadena = "Bienvenido a mi mundo Artificial"
print("**** Obtiene los últimos 10 caracteres ****:", cadena[-10:])

print("*********************************************************")
print ("Ejercicio 5")
#Función upper() :Convierte todas las letras de una cadena de texto a mayúsculas.
cadena = "Bienvenido a mi mundo Artificial"
print("\nCadena en mayúsculas:", cadena.upper())

print("*********************************************************")
print ("Ejercicio 6")
#Función lower(): Convierte todas las letras de una cadena de texto a minúsculas
cadena = "Bienvenido a mi mundo Artificial"
print("Cadena en minúsculas:", cadena.lower())

print("*********************************************************")
print ("Ejercicio 7")
#Multilíneas de cadenas de caracteres.
mensaje1 = "Mensaje con las comillas: \"Hola, Popayan!\""
mensaje2 = "Mensaje con tabulación:\n\tEste es un texto tabulado."
mensaje3 = "Mensaje con multiples líneas:\nLínea 1\nLínea 2\nLínea 3"
mensaje4 = "Mensaje con caracteres especiales:\n\t* Punto 1\n\t* Punto 2"
mensaje5 = "Mensaje final con \"comillas dobles\" y \\barra invertida\\"
print(mensaje1,"    Tipo:",type(mensaje1))

print("*********************************************************")
print ("Ejercicio 8")
# Función strip():Elimina los espacios en blanco (o caracteres específicos) al principio y al final de una cadena de texto.
cadena1 = "     Bienvenido a mi mundo Artificial    "
print("\nCadena sin espacios con la funcion strip:\n", cadena1.strip())
#sin la funcion strip para notar la diferencia
print("\nCadena con espacios sin la funcion strip:\n",cadena1)

print("*********************************************************")
print ("Ejercicio 9")
#Función replace():Cambia una palabra o parte del texto por otra en una cadena.
cadena2 = "¡Cada pequeño paso te acerca mas a tus grandes sueños!"
cadena_reemplazada = cadena2.replace("sueños", "metas")
print("\nCadena reemplazada:", cadena_reemplazada)

print("*********************************************************")
print ("Ejercicio 10")
#Función split(): Divide una cadena de texto en una lista de partes,basándose
#en un separador que le indiques (o el espacio por defecto).
cadena3="Tú eres capaz de lograr cosas increíbles. Solo cree en ti mismo y da el primer paso."
palabras = cadena3.split()
print("\nCadena dividida en palabras:", palabras)

print("*********************************************************")
print ("Ejercicio 11")
#Formato de cadenas F-String: Permiten incluir expresiones y variables dentro de una cadena de manera directa y legible.
ciudad= "Popayan"
departamento="Cauca"
f_string = f"Bienvenido a la ciudad de {ciudad}, Departamento del {departamento} "
print("\nF-String:", f_string)
