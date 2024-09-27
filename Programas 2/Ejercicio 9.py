#Escriba un programa para ingresar cualquier caracter y verificar si es una letra, dígito o carácter especial.

#Input: Un caracter.
#Output: Es letra, digito o caracter especial.

char=str(input("Digite un caracter:"))

if char.isalpha():
    print("El caracter es una letra")
elif char.isdigit():
    print("El caracter es un digito")
else:
    print("El caracter es un caracter especial")