print(" * Programa que determina si un numero es par o inpar *")
print("==================================================")

valor=int(input("Introduzca un  número entero: "))


if valor % 2==0:
    print(valor,"El numero es par", valor, "es par")

elif valor % 2 ==1:
    print(valor,"El numero es inpar", valor, "es par")

else:    
    print("Ingreso un valor erroneo")
