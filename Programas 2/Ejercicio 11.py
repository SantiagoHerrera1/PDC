#Escriba un programa para que dado el número del mes, indique el número de días del mes

#Input= número del mes
#Output= días del mes

x=float(input("Digite un número del 1 al 12, donde cada número representa un mes del año:"))

if x==1:
    print("El mes de Enero tiene 31 días")
if x==2:
    print("El mes de Febrero tiene 28 diás y 29 días si el año es bisiesto")
if x==3:
    print("El mes de Marzo tiene 31 días")
if x==4:
    print("El mes de Abril tiene 30 diás")
if x==5:
    print("El mes de Mayo tiene 31 días")
if x==6:
    print("El mes de Junio tiene 30 días")
if x==7:
    print("El mes de Julio tiene 31 días")
if x==8:
    print("El mes de Agosto tiene 31 días")
if x==9:
    print("El mes de Septiembre tiene 30 días")
if x==10:
    print("El mes de Octubre tiene 31 días")
if x==11:
    print("El mes de Noviembre tiene 30 días")
if x==12:
    print("El mes de Diciembre tiene 31 días")
if x<1:
    print("El número ingresado no corresponde a ningun mes del año")
if x>12:
    print("El número ingresado no corresponde a ningun mes del año")