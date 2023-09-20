print("Introduce dos números a comparar: \n")
    
a_num=int(input("Introduce el primer número: "))
b_num=int(input("Introduce el segundo número: "))

print("\n Los números a comparar son: ", a_num, " y ", b_num, "\n")

if a_num != b_num:
    print("Es diferente...")
if a_num == b_num:
    print("Son iguales...")
if a_num > b_num:
    print("Es mayor...")
if a_num < b_num:
    print("Es menor...")
if a_num >= b_num:
    print("Es mayor o igual...")
if a_num <= b_num:
    print("Es menor o igual...")

#se pone solo if ya que debe pasar por todas las condiciones
