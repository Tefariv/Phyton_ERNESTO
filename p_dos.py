compra =input (int("ingrese el valor de su compra"))
if compra <1000:
    print(compra)
    
    if compra < 5000:
        compra= compra-(compra*0.05)
        print(compra)
    elif compra < 7000:
        compra= compra-(compra*0.15)
        print(compra)
    elif compra < 10000:
        compra= compra-(compra*0.15)
        print(compra)
    elif compra < 15000:
        compra= compra-(compra*0.15)
        print(compra)
    elif compra > 25000:
        compra= compra-(compra*0.25)
        print(compra)
    

    
        
else:
    print("El valor es incorrecto")
    
    
   

