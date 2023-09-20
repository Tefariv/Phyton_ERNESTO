#Conjunción
print("Conjuncion (and)")

num_uno=int(input("Escribe un numero mayor a 2 o menor 5:"))

if num_uno > 2 and num_uno <5:
    print("El numero", num_uno, " cumple con la condición\n")
else:
    print("El", num_uno, " no cumple con la condición \n")


#Disyunción
print("Disyunción (or)")

palabra=input("Para cumplir la condición escribe 'si' o 'yes':")
palabra=palabra.lower()

if palabra== "si" or palabra == "yes":
    print("la condición se ha cumplido\n")
else:
    print("La condición no se ha cumplido")


#Negación(not)
print("Negacion (not)")

num_uno=int(input("Introduce un numero igual a 5:"))

if not num_uno ==5:
    print("El numero es diferente de 5, si cumple la condición")
else:
    print("El numero es igual a 5, y no cumple la función")




























    
