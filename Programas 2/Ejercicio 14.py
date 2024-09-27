#Escriba un programa para verificar si el triángulo es equilatero, isósceles o escaleno.

#Input: Lados del triángulo
#Output: Clasificación del triángulo

a=float(input("Digite el valor de un lado del triángulo:"))
b=float(input("Digite el valor del segundo lado del triángulo:"))
c=float(input("Digite el valor del tercer lado del triángulo:"))

if a==b and a==c:
    print("El triángulo es equilatero")
elif a==b and a!=c:
    print("El triángulo es isósceles")
else:
    print("El triángulo es escaleno")