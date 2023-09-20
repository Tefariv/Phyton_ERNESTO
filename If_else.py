print("Sistema para calcular el promedio de un alumno")
nombre=str(input("Cual es tu nombre?: "))

materia1=float(input(nombre + " Cual fue tu calificación en matematicas?: "))
materia2=float(input(nombre +" Cual fue tu calificación en quimica?: "))
materia3=float(input(nombre +" Cual fue tu calificación en biologia?: "))

promedio=(materia3+ materia1 + materia2)/3


if promedio >= 6:
    print('Felicidades ' + nombre+ ' "aprobaste" con un promedio de: ', promedio)
    print('Felicidades ' + nombre+ ' "aprobaste" con un promedio de: ', round(promedio,2))
else :
    print('no aprobaste ' + nombre+ ' tuviste un promedio de: ', promedio)
    print('no aprobaste ' + nombre+ ' tuviste un promedio de: ', round(promedio,1))

print("fin")
