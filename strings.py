#ejercicio de asignación
mensaje= "Hola"
mensaje+= " "
mensaje+= "Ernesto"
print(mensaje)

#ejercicio de concatenación
print("concatenación:")

mensaje="Hola"
espacio= ' '
nombre="Ernesto"
print(mensaje + espacio + nombre)
 

numero_uno=4
numero_dos=6
resultado= numero_uno + numero_dos
resultado= str(resultado)
#toca declarar la variable resultado como str para poder hacer la concatenación
print("El resultado de la suma es: " + resultado)

#ejercicio de busqueda(de uan subcadena mas pequeña de un caracter)

print("Busqueda:")
mensaje= "Hola Ernesto"
buscar_subcadena= mensaje.find("Ernesto")
print(buscar_subcadena)


#Extracción(sacar una parte de la cadena, segun suposiciión)

mensaje= "Hola Ernesto"
extraer_subcadena= mensaje[1:8]
#Va a tomar hasta la letra ubicada en 7, osea, uno antes de lo establecido
print(extraer_subcadena)



#ejercicio de comparación

mensaje_uno="Hola"
mensaje_dos="Hola"
print(mensaje_uno == mensaje_dos)


mensaje_uno="Hola"
mensaje_dos="ernesto"
print(mensaje_uno==mensaje_dos)








