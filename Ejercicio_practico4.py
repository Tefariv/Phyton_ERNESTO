print("Calculadora con una sola variable")

print("***********************")
print("*  Menú de opciones  *")
print("***********************")

#Menu de opciones
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Division entera")
print("6. Exponente")
print("7. Modulo y resto \n")

opcion=int(input("Introduce la opción deseada: "))

if opcion ==1:
    print("Elegiste suma\n")
    valor_a=int(input("Introduce el primer número: "))
    valor_b=int(input("Introduce el segundo número: "))
    print("El resultado de la suma es: ", valor_a+valor_b)


elif opcion ==2:
    print("Elegiste resta\n")
    valor_a=int(input("Introduce el primer número: "))
    valor_b=int(input("Introduce el segundo número: "))
    print("El resultado de la resta es: ", valor_a-valor_b)
    
elif opcion ==3:
    print("Elegiste multiplicción\n")
    valor_a=int(input("Introduce el primer número: "))
    valor_b=int(input("Introduce el segundo número: "))
    print("El resultado de la multiplicación es: ", valor_a*valor_b)

elif opcion ==4:
    print("Elegiste división\n")
    valor_a=int(input("Introduce el primer número: "))
    valor_b=int(input("Introduce el segundo número: "))
    print("El resultado de la división es: ", round (valor_a/valor_b, 2))

elif opcion ==5:
    print("Elegiste división entera\n")
    valor_a=int(input("Introduce el primer número: "))
    valor_b=int(input("Introduce el segundo número: "))
    print("El resultado de la división entera es", valor_a//valor_b)

elif opcion ==6:
    print("Elegiste exponente\n")
    valor_a=int(input("Introduce el primer número: "))
    valor_b=int(input("Introduce el segundo número: "))
    print("El resultado del exponente es: ", valor_a**valor_b)

elif opcion ==7:
    print("Elegiste modulo\n")
    valor_a=int(input("Introduce el primer número: "))
    valor_b=int(input("Introduce el segundo número: "))
    print("El resultado del modulo es: ", valor_a%valor_b)

else:
    print("Opción invalida")
