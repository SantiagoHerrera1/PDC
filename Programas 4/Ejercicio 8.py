#Escribe un código que liste todos los estudiantes que tienen una
#nota en 'Probabilidad' mayor a 3.0.

diccionario = {
    "Alondra": {"Regresion": 3.4, "InteligenciaArtificial": 2.8},
    "Baltasar": {"Calculo": 2.0, "Probabilidad": 4.0},
    "Celestino": {"Bioestadistica": 1.0},
    "Doroteo": {"Programacion": 1.5, "Probabilidad": 2.5, "Bayesiana": 3.0},
    "Esperancita": {"Programacion": 1.0},
    "Fabiola": {"Multivariante": 3.2, "Probabilidad": 4.1, "HistoriaEst": 2.9}
}

for nombre, asignaturas in diccionario.items():
    if 'Probabilidad' in asignaturas and asignaturas['Probabilidad'] > 3.0:
        print(nombre)