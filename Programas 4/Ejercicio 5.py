#Proporciona un ejemplo de cómo usar el método `get()` para obtener el valor de 'Bioestadística'
#en el diccionario de 'Celestino', con un valor predeterminado de `0` si la clave no existe.

diccionario = {
    "Alondra": {"Regresion": 3.4, "InteligenciaArtificial": 2.8},
    "Baltasar": {"Calculo": 2.0, "Probabilidad": 4.0},
    "Celestino": {"Bioestadistica": 1.0},
    "Doroteo": {"Programacion": 1.5, "Probabilidad": 2.5, "Bayesiana": 3.0},
    "Esperancita": {"Programacion": 1.0},
    "Fabiola": {"Multivariante": 3.2, "Probabilidad": 4.1, "HistoriaEst": 2.9}
}

bioestadistica = diccionario['Celestino'].get('Bioestadística', 0)
print(bioestadistica)