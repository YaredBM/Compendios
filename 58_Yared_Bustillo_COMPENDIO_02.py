#EJERCICIO 01
#Escribir una función que tome un carácter y devuelva True
#si es una vocal, de lo contrario devuelve False.
vocales =("aeiou")
caracter = input("Digite una letra:")
for vocal in caracter:
   aux = "True"
   if vocal not in vocales:
       aux = "False"
print(aux)



#EJERCICIO 02
#Escribir una función sum() y una función multip() que sumen y multipliquen
#respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4])
#debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
def suma(a):
    total = 0
    for i in range(len(a)):
        total += a[i] 
    return total
def mult(a):
    total = 1
    for i in range(len(a)):
        total *= a[i]
        return total
