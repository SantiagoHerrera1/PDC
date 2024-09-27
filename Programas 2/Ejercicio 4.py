#Escriba un programa para verificar si un número es divisible o no por 5 y 11.

#Input:Un número
#Output: Si es o no divisible por 5 y 11

x=float(input("Digite un número:"))

if x%5==0 and x%11==0:
    print("El número ingresado es divisible por 5 y 11")
else:
    print("El número ingresado no es divisible por 5 y 11")