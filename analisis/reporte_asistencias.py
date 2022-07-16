import pandas as pd
import matplotlib.pyplot as plt
import csv


# Punto 19
datos_del_estudiate = pd.read_csv('../datos/estudiante.csv')

# Punto 20
datos_de_asistencia = pd.read_csv('../datos/asistencia.csv')

# Punto 21
asistencias_completas = pd.merge(datos_del_estudiate,datos_de_asistencia, how='right')

# Punto 22
print(asistencias_completas)


# Punto 23
print('ESTUDIANTES POR CEDULA = 1111111111')
print(asistencias_completas[asistencias_completas.cedula == 1111111111])

# Punto 24
asistencias_completas[asistencias_completas.cedula == 1111111111].to_csv('datos\datos_reporte_1111111111.csv', index=True)

# Punto 25.
asistencias_completas[asistencias_completas.cedula == 1111111111]['fecha_año'].value_counts().plot(kind='bar')


plt.show()

