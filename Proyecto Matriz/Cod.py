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
    
#   Fin constructor
    
    def imprimir(self, decimales=2):
        for fila in self.matriz:
            for e in fila:
                print(f"{e:-8.0f}", end="")
            print("")
            
#--------------------------------------------------------------------------------------------------------
            
#   Santiago        
    def dimensiones(self):
        nfilas = self.nrows
        ncolumnas = self.ncols
        print(f"Dimensiones de la matriz: {nfilas} filas x {ncolumnas} columnas")
        if nfilas != ncolumnas: 
            print("La matriz no es cuadrada")
        else:
            print("La matriz es cuadrada")
            
#---------------------------------------------------------------------------------------------
            
#   Santiago 
    def imprimir_diagonal(self):
        if self.nrows != self.ncols:
            print("No se puede determinar si es identidad")
            return False
        
        identidad = True
        for i in range(self.nrows):
            for j in range(self.ncols):
                if i == j:
                    if self.matriz[i][j] != 1:
                        identidad = False
                else:
                    if self.matriz[i][j] != 0:
                        identidad = False

        if identidad:
            print("La matriz es identidad")
        else:
            print("La matriz no es identidad")
        return identidad
    
#-----------------------------------------------------------------------------------------------------
    
#   Santiago 
    def generar_identidad(self, tamaño):
        if tamaño <= 0:
            print("El tamaño debe ser un entero positivo.")
            return None

        identidad = [[1 if i == j else 0 for j in range(tamaño)] for i in range(tamaño)]

        print(f"Matriz identidad de tamaño {tamaño}x{tamaño} generada:")
        for fila in identidad:
            print(fila)
        
        return identidad

#-----------/-----------/------------/----------/------------/------------/-----------

A = Matriz("[1 0 0; 0 1 0; 0 0 1]")
A.imprimir()
A.dimensiones()
A.imprimir_diagonal()
identidad=A.generar_identidad(2)
