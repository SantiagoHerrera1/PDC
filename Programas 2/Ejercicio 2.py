#Escriba un programa para encontrar el máximo entre tres números.

#Input: Tres números.
#Output: El maximo de los 3 números.

a=float(input("Digite un número:"))
b=float(input("Digite otro número:"))
c=float(input("Digite un tercer número:"))

if a>b and a>c:
    print("El número máximo es:", a)
elif a<b and b>c:
    print("El número máximo es:", b)
elif a<c and b<c:
    print("El número máximo es:", c)
else:
    print("Los números ingresados son iguales")