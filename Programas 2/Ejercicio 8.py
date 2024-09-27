#Escriba un programa para ingresar cualquier caracter y verifique si es vocal o consonante.

#Input: Una letra
#Output: Es vocal o caracter

char=str(input("Digite una letra:"))

if char=="a" or char=="e" or char=="i" or char=="o" or char=="u" or char=="A" or char=="E" or char=="I" or char=="O" or char=="U":
    print("La letra es una vocal")
elif char.isalpha():
    print("La letra es una consonante")