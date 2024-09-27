#Escriba un programa para verificar si un caracter está en mayúsculas o en minúscula.

#Input: Un caracter.
#Output: Es Mayuscula o minuscula.

char=str(input("Digite un caracter:"))

if char.isalpha() and char.isupper():
    print("El carácter está en mayúscula")
elif char.isalpha and char.islower():
    print("El carácter está en minúscula")
else:
    print("El carácter no es valido")