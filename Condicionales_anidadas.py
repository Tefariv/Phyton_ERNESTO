print("=========")
print("Converosr")
print("========= \n")
#se hace salto de linea con: \n

print("Menu de opciones \n")

print("Presiona 1 para convertir de número a palabra")
print("Presiona 2 para converitir de número a letra")
            
opcion=int(input("Cual es tu opción deseada?: "))

if opcion == 1:
    print("\n Conversor de número a palabra.\n")
    
    numero_uno=int(input("cual es el numero que deseas convertir a palabra?: "))
    
    if numero_uno == 1:
        print("El número es 'uno'")
    elif numero_uno ==2:
        print("El número es 'dos'")
    elif numero_uno ==3:
        print("El número es 'tres'")
    elif numero_uno ==4:
        print("El número es 'cuatro'")
    elif numero_uno ==5:
        print("El número es 'cinco'")
    elif numero_uno > 5:
        print("El número no esta registrado")
    else:
        print("El número no esta registrado")
        
elif opcion == 2:
    print("\n Conversor de palabras a número.\n")
    
    numero_dos=str(input("cual es la palabra que deseas convertir a numero?: "))
    numero_dos= numero_dos.lower()
#la función lower vulve todos los datos que se ingresen en minusculas

    if numero_dos == "uno":
        print("El número es '1'")
    elif numero_dos =="dos":
        print("El número es '2'")
    elif numero_dos =="tres":
        print("El número es '3'")
    elif numero_dos =="cuatro":
        print("El número es '4'")
    elif numero_dos =="cinco":
        print("El número es '5'")
    else:
        print("El número no esta registrado")

else:
    print("Opción no disponible")
    
print("fin")


