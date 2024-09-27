Padre=False
Madre=True
Hermanos=True
Hijos=False

if Padre==True and Madre==True:
    print("Familia nuclear")
elif Padre==True and Madre==False:
    print("Familia monoparental")
elif Padre==False and Madre==True:
    print("Familia monoparental")

if Madre==True:
    if Padre==True:
        print("Familia nuclear")
    else:
        print("Familia monoparental")
        
else:
    if Padre==True:
        print("Familia monoparental")
    else:
        print("Familia unipersonal")