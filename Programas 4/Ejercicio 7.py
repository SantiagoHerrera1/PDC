#Crea una función en Python que calcule y devuelva el promedio de todas las notas
#de un estudiante dado, tomando como argumento el nombre del estudiante.

diccionario = {
    "Alondra": {"Regresion": 3.4, "InteligenciaArtificial": 2.8},
    "Baltasar": {"Calculo": 2.0, "Probabilidad": 4.0},
    "Celestino": {"Bioestadistica": 1.0},
    "Doroteo": {"Programacion": 1.5, "Probabilidad": 2.5, "Bayesiana": 3.0},
    "Esperancita": {"Programacion": 1.0},
    "Fabiola": {"Multivariante": 3.2, "Probabilidad": 4.1, "HistoriaEst": 2.9}
}

def promedio(nombre, diccionario):
    if nombre in diccionario:
        asignaturas = diccionario[nombre]
        if asignaturas:
            promedio = sum(asignaturas.values()) / len(asignaturas)
            return promedio
        else:
            return 0  
    else:
        return None

promedio_estudiante=promedio("Fabiola", diccionario)
print("El promedio de las notas de Fabiola es:", promedio_estudiante)