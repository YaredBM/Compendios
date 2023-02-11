#Diseñar un algoritmo para calcular la velocidad 
#EJERCICIO #1
v=int(input("Ingrese la velocidad :"))
t=int(input("Ingrese el tiempo:"))
d=v*t
print("El promedio es de:"+str(d),"Kilómetros")


#Cree un algoritmo que pida tres notas al usuario
#y luego imprima el promedio.
#EJERCICIO #2
N1=int(input("Ingrese nota numero 1 :"))
N2=int(input("Ingrese nota numero 2 :"))
N3=int(input("Ingrese nota numero 3 :"))
NP=int(N1+N2+N3)/3
print("El promedio es de:"+str(NP),"%")


#Se necesita elaborar un algoritmo que solicite el número de respuestas
#correctas, incorrectas y en blanco, correspondientes a postulantes, y muestre
#su puntaje final considerando que por cada respuesta correcta tendrá 3 puntos,
#respuestas incorrectas tendrá -1 y respuestas en blanco tendrá 0.
#EjERCICIO #3
RC=int(input("Ingrese el numero de respuestas correctas: "))
RI=int(input("Ingrese el numero de respuestas incorrectas: "))
RB=int(input("Ingrese el numero de respuestas en blanco: "))
PF=int((RC*3)+(RI*(-1)))
PRC=RC*3
PRI=RI*-1
PRB=RB*0
PF=(PRC+PRI+PRB)
print("El puntaje final es: " +str(PF),"%")


#Elaborar un algoritmo que permita ingresar el número de partidos ganados,
#perdidos y empatados, por ABC club en el torneo apertura, se debe de mostrar
#su puntaje total, teniendo en cuenta que por cada partido ganador obtendrá
#3 puntos, empatado 1 punto y perdido 0 puntos.
#EjERCICIO #4
PG=int(input("Escriba el total de partidos ganados: "))
PP=int(input("Escriba el total de partidos perdidos: "))
PE=int(input("Escriba el total de partidos empatados: "))
PPG=PG*3
PPP=PP*0
PPE=PE*1
PT=int(PPG+PPE+PPP)
print("La puntuación total es de: "+str(PT),"%")


#Se tiene los puntos A y B en el cuadrante positivo del plano cartesiano,
#elabore el algoritmo que permite obtener la distancia entre A y B. 
#EjERCICIO #5
AX=int(input("Ingrese los valores del punto 1 eje x: "))
AY=int(input("Ingrese los valores del punto 1 eje y:"))
BX=int(input("Ingrese los valores del punto 2 eje x: "))
BY=int(input("Ingrese los valores del punto 2 eje y:"))
D=((AX-BX)^2+(AY-BY)^2)^0,5
print("La distancia entre dos puntos X,Y es de: "+str(D),"metros")
