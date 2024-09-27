#Escriba un programa para encontrar el máximo entre dos números.

#Input: Dos números.
#Output: El maximo de los 2 números.

a=float(input("Digite un número:"))
b=float(input("Digite otro número:"))

if a>b:
    print("El número máximo es:", a)
elif a<b:
    print("El número máximo es:", b)
else:
    print("Los números ingresados son iguales")