#Calcular las soluciones x1, x2 de una ecuación de segundo grado dados los coeficientes a, b, y c.

#Input=Valores de a, b y c.
#Output=x1 y x2

a=float(input("Digite el valor de X o a:"))
b=float(input("Digite el valor de Y o b:"))
c=float(input("Digite el valor de Z o c:"))

x1= (-b+((((b)**2)-4*a*c)**0.5))/(2*a)
x2= (-b-((((b)**2)-4*a*c)**0.5))/(2*a)

print("El valor de x1 es:", x1, "y el valor de x2 es:", x2)