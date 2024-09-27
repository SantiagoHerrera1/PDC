#Escriba un programa para ingresar ángulos de un triángulo y verifique si es válido o no.

#Input: Ángulos del triángulo
#Output: Es valido el triángulo

a=float(input("Digite el valor del primer ángulo del triángulo:"))
b=float(input("Digite el valor del segundo ángulo del triángulo:"))
c=float(input("Digite el valor del tercer ángulo del triángulo:"))

if a+b+c==180:
    print("El triángulo es valido")
else:
    print("Su triángulo no es valido")