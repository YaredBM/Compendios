#EJERCICIO 01
#Escribir un pequeño programa donde:
#- Se ingresa el año en curso.
#- Se ingresa el nombre y el año de nacimiento de tres personas.
#- Se calcula cuántos años cumplirán durante el año en curso.
#- Se imprime en pantalla.

anioActual = int(input("Introduce el año en curso: "))
persona1 = str(input("Escribe el nombre de la persona 1: "))
anio1 = int(input("Ingresa el año de nacimiento de la persona 1: "))
persona2 = str(input("Escribe el nombre de la persona 2: "))
anio2 = int(input("Ingresa el año de nacimiento de la persona 2: "))
persona3 = str(input("Escribe el nombre de la persona 3: "))
anio3 = int(input("Ingresa el año de nacimiento de la persona 3: "))

anios1 = anioActual - anio1
anios2 = anioActual - anio2
anios3 = anioActual - anio3

print ("\n")
print (persona1, "cumplirá ", anios1, " años.")
print (persona2, "cumplirá ", anios2, " años.")
print (persona3, "cumplirá ", anios3, " años.\n")



#EJERCICIO 02
#Imprimir la cantidad de personas con edades superiores a 20.
#Que sea el usuario quien ingrese las edades.

patron = (23,23,46,3,2,54,23,34,24,64)

array = []

for x in range(1,11):
	array.append(int(input("Escribe una edad: ")))
cantidad = 0
for elemento in array:
	if elemento >= 20:
		cantidad = cantidad + 1
	else:
		cantidad = cantidad
print(cantidad)



#EJERCICIO 03
#Crear una función contar vocales (), que reciba una palabra
#y cuente cuantas letras "a" tiene, cuantas letras "e" tiene
#y así hasta completar todas las vocales.
#Se puede hacer que el usuario sea quien elija la palabra.

def contar_vocales(palabra):
	palabra_min = palabra.lower()
	cant_a = 0
	cant_e = 0
	cant_i = 0
	cant_o = 0
	cant_u = 0
	
	for letra in palabra_min:
		if letra == "a":
			cant_a = cant_a + 1
		elif letra == "e":
			cant_e = cant_e + 1
		elif letra == "i":
			cant_i = cant_i + 1
		elif letra == "o":
			cant_o = cant_o + 1
		elif letra == "u":
			cant_u = cant_u + 1		

	print("Hay "+ str(cant_a)+ " a")
	print("Hay "+ str(cant_e)+ " e")
	print("Hay "+ str(cant_i)+ " i")
	print("Hay "+ str(cant_o)+ " o")
	print("Hay "+ str(cant_u)+ " u")

palabra = str(input("Escribe una palabra: "))
contar_vocales(palabra)	


#EJERCICIO 04
#Escriba una función es bisiesto () que determine si un año
#determinado es un año bisiesto. Un año bisiesto es divisible por 4,
#pero no por 100. También es divisible por 400.

def es_bisiesto(ano):
	if ano%4 == 0:
		if ano%100 != 0:
			print("Es bisiesto")
	else:
		print("No es bisiesto")

ano = int(input("Escriba un año para saber si es bisiesto: "))
es_bisiesto(ano)
