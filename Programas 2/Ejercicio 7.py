#Escriba un programa para verificar si un caracter es una letra del alfabeto o no.

#Input: Un caracter.
#Output: Hace parte del alfabeto.

char=str(input("Digite un caracter:"))

if char.isalpha():
    print("El caracter hacer parte del alfabeto")
else:
    print("El caracter no hace parte del alfabeto")