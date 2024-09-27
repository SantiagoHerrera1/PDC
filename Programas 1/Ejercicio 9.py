#Determinar el pago mensual M de un préstamo simple con capital P, tasa de interés mensual r, y número de pagos n.

#input:capital, interes y num de pagos
#output:Pago mensual

P=float(input("Digite el valor de su capital:"))
r=float(input("Digite la tasa de interes mensual:"))
n=float(input("Digite el número de pagos."))

M=(P*r)/(1-(1+r)**-n)

print("El pago mensual de su prestamo es:", M)