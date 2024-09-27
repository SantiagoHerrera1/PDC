#Escriba un programa para verificar si un número es negativo, positivo o cero.

#Input: Un número.
#Output: Es negativo, positivo o cero.

a=float(input("Digite un número:"))

if a>1:
    print("El número", a, "es positivo")
elif a<0:
    print("El número", a, "es negativo")
else:
    print("El número", a, "es cero")