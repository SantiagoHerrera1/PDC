class Matriz:
    def __init__(self, cadena: str):
        if not (cadena[0]=="[" and cadena[-1]=="]"):
            print("Cadena no valida")
            return(None)
        #print("Continuamos")
        cadena=cadena[1:-1]
        sfilas=cadena.split(";")
        #print(sfilas)
        self.nrows=len(sfilas)
        ncols=0
        Filas=[]
        for s in sfilas: ##Llena la lista vacia con los valores separados
            filastr=s.split()        
            if ncols==0:
                ncols=len(filastr)
            elif ncols!=len(filastr):
                print("error por numero de filas")
                return(None)
            fila_float=[]
            for x in filastr:
                fila_float.append(float(x)) 
            Filas.append(fila_float)
            
            ncols=len(fila_float)
        self.ncols=ncols
        self.matriz=Filas.copy()


    def imprimir(self, decimales=2):
        for fila in self.matriz:
            for e in fila:
                print(f"{e:-8.2f}", end="")
            print(" ")

    def dimensiones(self):
        """Devuelve las dimensiones de la matriz."""
        nfilas = self.nrows
        ncolumnas = self.ncols
        
        return (nfilas, ncolumnas)

    def sumar(self, otra_matriz):
        """Suma dos matrices."""
        pass

    def multiplicar_escalar(self, escalar):
        if not self.matriz:
            #print("No se puede")
            return None
        res_matriz=[]
    
        for i in self.matriz:
            nrows = [elemento * escalar for elemento in i]
            res_matriz.append(nrows)
    
        self.matriz=res_matriz
    
    


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
        matriz1= self.matriz
        matriz2=[]
        for i in range(self.nrows):
            matriz2.append([0]*self.ncols)
        for j in range(self.nrows):
            for k in range(self.ncols):
                matriz2[k][j]= matriz1[j][k]
        self.matriz=matriz2


    def determinante_2x2(self):
        """Calcula el determinante de una matriz 2x2."""
        # Extraer los elementos de la matriz
        a = matriz[0][0]
        b = matriz[0][1]
        c = matriz[1][0]
        d = matriz[1][1] 
        
        # Calcular el determinante
        determinante=a*d-b*c
        return determinante

    def generar_identidad(self, n:int):
        """Genera una matriz identidad de tama~no n x n."""
        # Creamos una lista vacía que contendrá las filas de la matriz
        matriz=[]
        # Iteramos sobre las filas de la matriz
        for i in range(n):
            # Creamos una fila vacía
            fila=[]  
            
            # Iteramos sobre las columnas de la matriz
            for j in range(n):
                # Si estamos en la diagonal (índice i igual a índice j)
                if i==j:
                    # Colocamos un 3 en la posición diagonal
                    fila.append(1)  
                else:
                    # Si no estamos en la diagonal, colocamos un 1
                    fila.append(0)
            
            # Añadimos la fila a la matriz
            self.nrows=n
            self.ncols=n
            matriz.append(fila)  
            self.matriz=matriz
      

    def determinante(self):
        """Calcula el determinante de una matriz 3x3."""
        pass
    
    
    
    def zeros(self, f, c):
        """Genera una matriz de fxc con solo ceros"""
        if f <=0 or c <=0:
            print("El tamaño debe ser un entero positivo.")
            return None

        ceros = []
        for i in range(f):
            fila = []
            for j in range(c):
                fila.append(0)
            ceros.append(fila)

        self.nrows=f
        self.ncols=c

        self.matriz = ceros
        
    def unos(self, f, c):
        """Genera una matriz de fxc con solo unos"""
        if f <=0 or c <=0:
            print("El tamaño debe ser un entero positivo.")
            return None

        unos = []
        for i in range(f):
            fila = []
            for j in range(c):
                fila.append(1)
            ceros.append(fila)

        self.nrows=f
        self.ncols=c

        self.matriz = unos