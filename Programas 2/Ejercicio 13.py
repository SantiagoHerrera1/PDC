#Escriba un programa para ingresar todos los lados de un triángulo y verifique si es válido o no.

#Input: Lados del triángulo
#Output: Es valido el triángulo

a=float(input("Digite el valor del primer lado del triángulo:"))
b=float(input("Digite el valor del segundo lado del triángulo:"))
c=float(input("Digite el valor del tercer lado del triángulo:"))

if a+b>c and a+c>b and b+c>a:
    print("El triángulo es valido")
else:
    print("El triángulo no es valido")