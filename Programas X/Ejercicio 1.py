palabra="anilina"

for i,w in zip(palabra, palabra[::1]):
    print(i,w)

if i == w:
    print("La palabra es palindroma")
else:
    print("La palabra no es palindroma")