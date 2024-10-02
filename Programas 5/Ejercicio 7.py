#Dada una lista retorna una una nueva lista ordenada de mayor a menor

lista1=[3, 2, 12, 4, 13, 8, 5, 92, 99, 101]
lista2=[6, 5, 3, 20, 11, 99, 13, 93]
lista3=[]

for i in lista1:
  for w in lista2:
    if i==w:
      lista3=lista3+[w]
lista3.sort(reverse=True)
print(lista3)