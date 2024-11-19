class Matriz:
    def __init__(self, cadena: str):
        if not (cadena[0] == "[" and cadena[-1] == "]"):
            print("No se puede construir la matriz.")
            return None
        
        cadena = cadena[1:-1]
        
        sfilas = cadena.split(";")
        self.nrows = len(sfilas)
        self.ncols = 0
        self.matriz = []

        for s in sfilas:
            filastr = s.split()
            filafloat = [float(e) for e in filastr]

            if self.ncols == 0:
                self.ncols = len(filafloat)
            elif self.ncols != len(filafloat):
                print("Número diferente de columnas en las filas.")
                self.matriz = []
                return None

            self.matriz.append(filafloat)

    def imprimir(self, decimales=2):
        for fila in self.matriz:
            for e in fila:
                print(f"{e:-8.2f}", end="")
            print(" ")

    def dimensiones(self):
        nfilas = self.nrows
        ncolumnas = self.ncols
        print(f"Dimensiones de la matriz: {nfilas} filas x {ncolumnas} columnas")
        if nfilas != ncolumnas: 
            print("La matriz no es cuadrada")
        else:
            print("La matriz es cuadrada")

    def sumar(self, otra_matriz):
        """Suma dos matrices."""
        pass

    def multiplicar_escalar(self, escalar):
        """Multiplica la matriz por un escalar."""
        pass

    def multiplicar_matriz(self, otra_matriz):
        """Multiplica dos matrices."""
        pass

    def son_iguales(self, otra_matriz):
        """Verifica si dos matrices son iguales."""
        pass

    def traza(self):
        """Calcula la traza de la matriz."""
        pass

    def traspuesta(self):
        """Devuelve la traspuesta de la matriz."""
        pass

    def determinante_2x2(self):
        """Calcula el determinante de una matriz 2x2."""
        pass

    def generar_identidad(self, tamano):
        if tamano <= 0:
            print("El tamaño debe ser un entero positivo.")
            return None

        identidad = [[1 if i == j else 0 for j in range(tamano)] for i in range(tamano)]

        print(f"Matriz identidad de tamaño {tamano}x{tamano} generada:")
        for fila in identidad:
            print(fila)
        
        return identidad

    def determinante(self):
        """Calcula el determinante de una matriz 3x3."""
        pass
    
A=Matriz("[1 0 0;0 1 0;0 0 1]")
A.imprimir()
A.dimensiones()
identidad=A.generar_identidad(5)