a=int(input("Ingrese el primer numero"))
b=int(input("ingrese el segundo numero"))

operacion=int(input("ingrese el tipo de operacion(1=suma,2=resta,3=multiplicacion,4=division)"))

if operacion==1:
    resultado=a+b
    print("El resultado de la suma es",resultado)
elif operacion==2:
	resultado=a-b
elif operacion==3:
    resultado=a*b
    print("El resultado de la multiplicacion es",resultado)
elif operacion==4:
	resultado=a/b

print(resultado)