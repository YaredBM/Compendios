#Ejercicio 01
#Dado el sueldo de un trabajador, aplique un aumento del 15%
#si su sueldo es inferior a $1000. Imprima el sueldo que percibirá.
din = float (input ("Escriba su salario: "))
if din<1000:
    cam=din*0.15
else:
    cam=0
nuevo_din=din+cam
print ("Se le aumenta : " + repr (cam))
print ("Se le pagará :" + repr (nuevo_din))
print ()



#Ejercicio 02
#Determinar si un año leído por teclado es o no bisiesto.
per = int(input("Ingresa año: "))

if per % 4 != 0: 
	print("No Bisiesto")
else:
    if per % 4 == 0 and per % 100 != 0: 
        print(" Bisiesto")
    else:
        if per % 4 == 0 and per % 100 == 0 and per % 400 != 0: 
            print("No Bisiesto")
        else:
            if per % 4 == 0 and per % 100 == 0 and per % 400 == 0:
                print("Bisiesto")

#Ejercicio 03
#Se desea leer por teclado un número comprendido entre 0 y 10
#(inclusive) y se desea visualizar si el número es par o impar.
parimpar = int(input("Escribir Numero: "))
if parimpar % 2 == 0:
    print("Par")
else:
    if parimpar % 2 != 0:
        print("Impar")
