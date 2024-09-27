#Escriba un programa para verificar si un año es un año bisiesto o no.

#Input: número de días.
#Output: Es bisiesto o no.

a=float(input("Digite el número de días que tiene el año:"))

if a%2==0:
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")