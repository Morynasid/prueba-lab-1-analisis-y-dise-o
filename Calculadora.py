a=input("Ingrese el primer numero")
b=input("ingrese el segundo numero")

operacion=input("ingrese el tipo de operacion(1=suma,2=resta,3=multiplicacion,4=division)")

if operacion==1:
    resultado=int(a)+int(b)
    print("El resultado de la suma es",resultado)
elif operacion==3:
    resultado=int(a)*int(b)
    print("El resultado de la multiplicacion es",resultado)
break