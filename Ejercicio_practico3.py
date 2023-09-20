print("=================================================================")
print("programa para determinar cual es el numero mas grande de los tres")
print("=================================================================\n")


valor_a=int(input("introduzca el primer numero: "))
valor_b=int(input("introduzca el segundo numero: "))
valor_c=int(input("introduzca el tercer numero: "))


if valor_a> valor_b and valor_a > valor_c:
    print("el valor mayor es: ", valor_a)
    if valor_b > valor_c:
        print("el valor menor es", valor_c)
        if valor_b < valor_a and valor_b > valor_c:
            print("El valor del medio es ", valor_b)
    
elif valor_b> valor_a and valor_b > valor_c:
    print("el valor mayor es: ", valor_b)
    if valor_a > valor_c:
        print("el valor menor es", valor_c)
        if valor_a < valor_b and valor_a > valor_c:
            print("El valor del medio es ", valor_a)


elif valor_c> valor_b and valor_c > valor_a:
    print("el valor mayor es: ", valor_c)
    if valor_b > valor_a:
        print("el valor menor es", valor_a)
        if valor_b < valor_c and valor_b > valor_a: 
            print("El valor del medio es ", valor_b)

else:
    print("introdujo datos incorrectos")
