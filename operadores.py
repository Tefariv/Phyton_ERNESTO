print("Suma: ")
numero_uno= 5
numero_dos= 4

resultado=numero_uno + numero_dos

print("el resultado de la suma es: "+ str(resultado))


print("resta: ")
numero_uno= 5
numero_dos= 4

resultado=numero_uno - numero_dos

print("el resultado de la resta es: "+ str(resultado))


print("multipliocación: ")
numero_uno= 5
numero_dos= 4

resultado=numero_uno * numero_dos

print("el resultado de la multiplicación es: "+ str(resultado))



print("exponente: ")
numero_uno= 2
exponente= 5

resultado=numero_uno ** exponente

print("el resultado de el exponente es: "+ str(resultado))



print("división: ")
numero_uno= 4
numero_dos= 2

resultado=numero_uno / numero_dos

print("el resultado de la división: "+ str(resultado))




print("modulo: ")
numero_uno= 30
numero_dos= 8

resultado=numero_uno % numero_dos

print("el resultado de la multiplicación es: "+ str(resultado))



print("división entera: ")
numero_uno= 10
numero_dos= 3

resultado=numero_uno // numero_dos

print("el resultado de la división entera: "+ str(resultado))












print("=================================================================")
print("programa para determinar cual es el numero mas grande de los tres")
print("=================================================================")


valor_a=int(input("introduzca el primer numero"))
valor_b=int(input("introduzca el segundo numero"))
valor_c=int(input("introduzca el tercer numero"))


if valor_a> valor_b and valor_a > valor_c:
    print("el valor mayor es: ", valor_a)
    if valor_b > valor_c:
        print("el valor menor es", valor_c)
    elif valor_b < valor_a and valor_b > valor_c:
        print("El valor del medio es ", valor)
    
elif valor_b> valor_a and valor_b > valor_c:
    print("el valor mayor es: ", valor_b)
    if valor_a > valor_c:
        print("el valor menor es", valor_c)
    elif valor_a < valor_b and valor_a > valor_c:
        print("El valor del medio es ", valor)


elif valor_c> valor_b and valor_c > valor_a:
    print("el valor mayor es: ", valor_c)
    if valor_b > valor_a:
        print("el valor menor es", valor_a)
    elif valor_b < valor_c and valor_b > valor_a: 
        print("El valor del medio es ", valor_b)

else:
    print("introdujo datos incorrectos")






