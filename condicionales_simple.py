print("Sistema para calcular el promedio de un estudiante")
nombre= input("cual es tu nombre?: ")
materia1= int(input("cual es tu calificación en materia 1?: "))
materia2= int(input("cual es tu calificación en materia 2?: "))
materia3= int(input("cual es tu calificación en materia 3?: "))

promedio= (materia1 +materia2 +materia3)/3
promedio=int(promedio)

if promedio >= 6:
    print('felicidades '+ nombre + '"APROBASTE"',promedio)

print("fin")
