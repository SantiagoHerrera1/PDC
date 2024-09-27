#Dada una lista de numeros encuentre la media

lista=[2,5,21,7,13]

contador=0
suma=0
for i in lista:
    print(i, end=",")
    contador= contador+1
    suma= suma+i

media=suma/contador
print("La media es:", media)