#La función 'end=""' sirve para unir cadenas de caracteres sin hacer un salto de linea
print("Esto es un ", end="")
print("ejemplo")


#uso de format 
nombre="Stephanie"
edad=17

print ("hola ",()," tienes ", (), " años".format(nombre, edad))

#otro uso del format

print("Hola ",(nombre)," tienes ",(edad), " años".format(nombre="Tefa", edad=17)


z=0
a=["a", "b", "c", "a"]
for x in a:
 print(z)
z=z+1


a=[0,1,2,3,4,5]
c=0
b=a[c]
while b>0:
 print(a[c-2])