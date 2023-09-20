print("*****************************************")
print("* Sistema de control de vacacional Rappi *")
print("*****************************************\n")

#Se va a pedir los datos
nombre=input("Ingresa tu nombre: ")
clave_dep=int(input("Ingresar la clave del departamento: "))
años=int(input("Ingrese los años que lleva en el trabajo: "))

if clave_dep==1:
    if años==1:
        print(nombre, "Recibe 6 días de vacaciones")
        
    elif años > 1 and años < 7:
        print(nombre, "Recibe 14 días de vacaciones")
    elif años >6:
        print(nombre, "Recibe 20 días de vacaciones")

elif clave_dep==2:
    if años==1:
        print(nombre, "Recibe 7 días de vacaciones")
    elif años > 1 and años < 7:
        print(nombre, "Recibe 15 días de vacaciones")
    elif años >6:
        print(nombre, "Recibe 22 días de vacaciones")


elif clave_dep==3:
    if años==1:
        print(nombre, "Recibe 10 días de vacaciones")
    elif años > 1 and años < 7:
        print(nombre, "Recibe 20 días de vacaciones")
    elif años >6:
        print(nombre, "Recibe 30 días de vacaciones")

else:
    print("ingreso mal la clave")

print("Fin")
