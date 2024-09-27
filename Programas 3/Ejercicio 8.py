#Escriba un programa que dado un número indique si es primo o no(8)

x=int(input("Digite un número para saber si es primo: "))
no_primo=False

for i in range(2,x,1):
    if x%i == 0:
        print("El número no es primo")
        no_primo=True
        break
if no_primo==False:
    print("El numero es primo")