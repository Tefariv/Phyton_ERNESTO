print("Esto es una suma")
numero_uno= 2
numero_dos= 4
resultado= numero_uno + numero_dos
print(resultado)




#programa cap 12
print("===============================")
print("convertidor de numeros a letras")
print("===============================")

num=int(input("caul es l numero que deseas convertir? :"))

if num == 1:
    print("El numero es 'Uno'")
elif num == 2:
    print("El numero es 'dos'")
elif num == 3:
    print("El numero es 'tres'")
elif num == 4:
    print("El numero es 'cuatro'")
elif num == 5:
    print("El numero es 'cinco'")
    
    
else:
    print("este programa solo convierte hasta el numero 5")
    
    #condicionales anidadas
print("=========")
print("conversor")
print("=========")
print(" ")
print("menu de opciones)

opcion_uno=int(input("Elige uno para pasar de numero a letra: "))
opcion_dos=int(input("Elige dos para pasar de letra a numero: "))

if opcion_uno==1:
    dato_uno=int(input("cual es el numero que deseas pasar a palabra? :"))
    if dato_uno==1:
        print("el numero es 'uno'")
    elif dato_uno == 2:
        print("El numero es 'dos'")
    elif dato_uno == 3:
        print("El numero es 'tres'")
    elif dato_uno == 4:
        print("El numero es 'cuatro'")
    elif dato_uno == 5:
        print("El numero es 'cinco'")
        
elif opcion_uno==2:
    dato_dos=int(input("cual es el numero que deseas pasar a palabra? :"))
    if dato_dos==1:
        print("el numero es 'uno'")
    elif dato_dos == 2:
        print("El numero es 'dos'")
    elif dato_dos == 3:
        print("El numero es 'tres'")
    elif dato_dos == 4:
        print("El numero es 'cuatro'")
    elif dato_dos == 5:
        print("El numero es 'cinco'")
        
        