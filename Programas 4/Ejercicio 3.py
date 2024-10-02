#¿Qué línea de código usarías para añadir un nuevo par clave-valor `'MineríaDatos': 3.5`
#al diccionario anidado de 'Alondra'?


diccionario = {
    "Alondra": {"Regresion": 3.4, "InteligenciaArtificial": 2.8},
    "Baltasar": {"Calculo": 2.0, "Probabilidad": 4.0},
    "Celestino": {"Bioestadistica": 1.0},
    "Doroteo": {"Programacion": 1.5, "Probabilidad": 2.5, "Bayesiana": 3.0},
    "Esperancita": {"Programacion": 1.0},
    "Fabiola": {"Multivariante": 3.2, "Probabilidad": 4.1, "HistoriaEst": 2.9}
}

diccionario['Alondra']['MineríaDatos'] = 3.5
print(diccionario)



