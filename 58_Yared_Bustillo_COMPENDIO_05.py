#EJERCICIO 01
#Resuelva un problema que tiene una gasolinera. Los dispensadores de esta registran lo que “surten” en galones,
#pero el precio de la gasolina está fijado en litros. El DF debe calcular e imprimir lo que hay que cobrarle
#al cliente. Solución. Entrada Identificador Litros por galón (constante) LITXG Precio por litro (constante)
#PRECIOXL Cantidad surtida CONSU. Para calcular el total a pagar por lo surtido se debe multiplicar
#lo surtido (CONSU), cuyo valor está en galones, por la equivalencia de cuantos litros hay en un galón (LITXG),
#así obtendremos el total de litros que se surtió, a este resultado se le multiplica por el precio de cada
#litro (PRECIOXL). TOTAL = COSU * LITXG* PRECIOXL
print("-------------------------------------------------------")
print(" GASOLINERA ")
print("-------------------------------------------------------")
#Constantes
LITXG = 3.785
PRECIOXL = 4.50
#Entrada
consu = float( input("Ingresar consumo: "))
#Proceso
total = consu*LITXG*PRECIOXL
#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print("Total:", total)



#EJERCICIO 02
#Calcular el monto a pagar por un artículo si se tiene como datos de entrada
#la cantidad de docenas que compra y el costo por unidad de este artículo.
print("-------------------------------------------------------")
print(" CALCULAR MONTO A PAGAR ")
print("-------------------------------------------------------")
#Entradas
print("Ingrese costo unitario del artículo:")
c = float( input())
print("Ingrese el número de docenas:")
d = int( input())
#Proceso
p = d*12 * c
#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print("El precio del artículo es:", p)



#EJERCICIO 03
#Dado la velocidad de 2 cuerpos que se dirigen uno al encuentro de otro determinar el tiempo de
#encuentro si la distancia que los separa inicialmente es “D”. Pseudocódigo. va = velocidad del
#cuerpo “a” vb = velocidad del cuerpo “b” te = tiempo de encuentro D = distancia que separa “a” de “b
print("-------------------------------------------------------")
print("TIEMPO DE ENCUENTRO.")
print("-------------------------------------------------------")
#Entradas
print("Ingrese las velocidades:")
va = float( input("Va: "))
vb = float( input("Vb: "))
print("Ingrese la distancia que los separa:")



#EJERCICIO 04
#Dado como dato la calificación de un alumno, escriba “aprobado” en caso de que
#esa calificación sea mayor a 70.
print("-------------------------------------------------------")
print(" VERIFICAR SI UN ALUMNO ESTA APROBADO ")
print("-------------------------------------------------------")
#Entradas
CAL = float( input("Ingrese Calificación: "))
#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
if CAL > 10 :
print("Aprobado")



#EJERCICIO 05
#Dado el sueldo de un trabajador, aplique un aumento del 15% si su sueldo
#es inferior a $1000. Imprima el sueldo que percibirá.
print("-------------------------------------------------------")
print(" SUELDO A PERCIBIR ")
print("-------------------------------------------------------")
#Entradas
SUE = float( input("Ingrese Sueldo: "))
#Proceso
if SUE < 1000:
AUM = SUE*0.15
SUE = SUE + AUM
#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print("El sueldo es:", SUE)



#EJERCICIO 06
#Desarrolle un algoritmo para determinar si un año leído por teclado es o no bisiesto.
print("-------------------------------------------------------")
print(" VERIFICAR SI EL AÑO ES BISIESTO ")
print("-------------------------------------------------------")
#Entradas
anio = int( input("Ingrese año: "))
#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
if (anio % 400 == 0) or (anio % 4 == 0) and (anio % 100 != 0):
print("El año es BISIESTO")
else:
print("El año NO es BISIESTO")



#EJERCICIO 07
#Se desea leer por teclado un número comprendido entre 0 y 10 (inclusive)
#y se desea visualizar si el número es par o impar.
print("-------------------------------------------------------")
print(" PAR O IMPAR ")
print("-------------------------------------------------------")
#Entradas
NUM = int( input("Ingrese número:" ))
#Proceso
#Usando un diccionario
par_Impar = {
1 : 'Impar',
3 : 'Impar',
5 : 'Impar',
7 : 'Impar',
9 : 'Impar',
2 : 'Par',
4 : 'Par',
6 : 'Par',
8 : 'Par',
10 : 'Par'
}
#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print(par_Impar.get(NUM, "Numero fuera de Rango"))



#EJERCICIO 08
#Construya un algoritmo que, dados tres números, muestre el mensaje “IGUALES”
#si la suma de los dos primeros es igual al otro número y el mensaje “DISTINTOS”
#en caso contrario.
print("-------------------------------------------------------")
print("Complemento1: IGUALES O DISTINTOS.")
print("-------------------------------------------------------")
#Entradas
print("Ingrese tres números")
a = int( input("Ingrese a: "))
b = int( input("Ingrese b: "))
c = int( input("Ingrese c: "))
#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
if a + b == c :
print("IGUALES")
else:
print("DISTINTOS")


























