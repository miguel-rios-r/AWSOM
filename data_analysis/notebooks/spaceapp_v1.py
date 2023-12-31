# -*- coding: utf-8 -*-
"""SpaceApp_v1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YrYkpH4V9SC4Fl-V14CD8ftXzUDGCBvS

### **DSCOVR PlasMAG 2023 Data**

Importar libreria pandas
"""

import pandas as pd
import matplotlib.pyplot as plt

# Carga el archivo CSV en un DataFrame de pandas
df_k = pd.read_csv('../notebooks/k_index_data_preprocessed.csv')
df_mag_data1 = pd.read_csv('../notebooks//mag_data1_preprocessed.csv')
df_mag_data3 = pd.read_csv('../notebooks/mag_data3_preprocessed.csv')
df_plasma_data1 = pd.read_csv('../notebooks/plasma_data1_preprocessed.csv')
df_plasma_data3 = pd.read_csv('../notebooks/plasma_data3_preprocessed.csv')

"""# Datos del campo magnético

**Campo magnético en 1 día**
"""

# Seleccionar las columnas de interés
selected_columns = ["bx_gsm", "by_gsm", "bz_gsm", "lon_gsm", "lat_gsm", "bt"]

# Calcular estadísticas descriptivas
statistics = df_mag_data1[selected_columns].describe()

# Imprimir las estadísticas descriptivas
print(statistics)

# Time in datatime
df_mag_data1['time_tag'] = pd.to_datetime(df_mag_data1['time_tag'])

# Columnas
bx_gsm = df_mag_data1['bx_gsm']
by_gsm = df_mag_data1['by_gsm']
bz_gsm = df_mag_data1['bz_gsm']
lon_gsm = df_mag_data1['lon_gsm']
lat_gsm = df_mag_data1['lat_gsm']
bt = df_mag_data1['bt']

# Crea un gráfico en función del tiempo
plt.figure(figsize=(12, 6))
plt.plot(df_mag_data1['time_tag'], bx_gsm, label='bx_gsm')
plt.plot(df_mag_data1['time_tag'], by_gsm, label='by_gsm')
plt.plot(df_mag_data1['time_tag'], bz_gsm, label='bz_gsm')
plt.plot(df_mag_data1['time_tag'], lon_gsm, label='lon_gsm')
plt.plot(df_mag_data1['time_tag'], lat_gsm, label='lat_gsm')
plt.plot(df_mag_data1['time_tag'], bt, label='bt')

plt.xlabel('Time')
plt.ylabel('Data')
plt.title('Campo Magnético en 1 día')
plt.legend()
plt.grid(True)
plt.show()

# Convertir la columna "time_tag" a tipo datetime
df_mag_data1["time_tag"] = pd.to_datetime(df_mag_data1["time_tag"])
df_k["time_tag"] = pd.to_datetime(df_k["time_tag"])

# Seleccionar las columnas de interés
mag_columns = ["bx_gsm", "by_gsm", "bz_gsm","lon_gsm","lat_gsm","bt"]
kp_columns = ["Kp"]

# Combinar los datos en un solo DataFrame usando el índice "time_tag"
combined_data = pd.merge(df_mag_data1[mag_columns + ["time_tag"]], df_k[kp_columns + ["time_tag"]], on="time_tag")

# Calcular la matriz de correlación
correlation_matrix = combined_data.corr()
print(correlation_matrix)

# Visualizar la matriz de correlación como un mapa de calor
plt.figure(figsize=(10, 6))
plt.imshow(correlation_matrix, cmap="coolwarm", interpolation="nearest", aspect="auto")
plt.colorbar()
plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=45)
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
plt.title("Matriz de Correlación")
plt.show()

"""**Campo magnético en 3 días**"""

# Seleccionar las columnas de interés
selected_columns = ["bx_gsm", "by_gsm", "bz_gsm", "lon_gsm", "lat_gsm", "bt"]

# Calcular estadísticas descriptivas
statistics = df_mag_data3[selected_columns].describe()

# Imprimir las estadísticas descriptivas
print(statistics)

# Time in datetime format
df_mag_data3['time_tag'] = pd.to_datetime(df_mag_data3['time_tag'])

# Columnas
bx_gsm = df_mag_data3['bx_gsm']
by_gsm = df_mag_data3['by_gsm']
bz_gsm = df_mag_data3['bz_gsm']
lon_gsm = df_mag_data3['lon_gsm']
lat_gsm = df_mag_data3['lat_gsm']
bt = df_mag_data3['bt']

# Crea un gráfico en función del tiempo
plt.figure(figsize=(12, 6))
plt.plot(df_mag_data3['time_tag'], bx_gsm, label='bx_gsm')
plt.plot(df_mag_data3['time_tag'], by_gsm, label='by_gsm')
plt.plot(df_mag_data3['time_tag'], bz_gsm, label='bz_gsm')
plt.plot(df_mag_data3['time_tag'], lon_gsm, label='lon_gsm')
plt.plot(df_mag_data3['time_tag'], lat_gsm, label='lat_gsm')
plt.plot(df_mag_data3['time_tag'], bt, label='bt')

plt.xlabel('Time')
plt.ylabel('Data')
plt.title('Campo magnético en  3')
plt.legend()
plt.grid(True)
plt.show()



# Convertir la columna "time_tag" a tipo datetime
df_mag_data3["time_tag"] = pd.to_datetime(df_mag_data3["time_tag"])
df_k["time_tag"] = pd.to_datetime(df_k["time_tag"])

# Seleccionar las columnas de interés
mag_columns = ["bx_gsm", "by_gsm", "bz_gsm","lon_gsm","lat_gsm","bt"]
kp_columns = ["Kp"]

# Combinar los datos en un solo DataFrame usando el índice "time_tag"
combined_data = pd.merge(df_mag_data3[mag_columns + ["time_tag"]], df_k[kp_columns + ["time_tag"]], on="time_tag")

# Calcular la matriz de correlación
correlation_matrix = combined_data.corr()
print(correlation_matrix)

# Visualizar la matriz de correlación como un mapa de calor
plt.figure(figsize=(10, 6))
plt.imshow(correlation_matrix, cmap="coolwarm", interpolation="nearest", aspect="auto")
plt.colorbar()
plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=45)
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
plt.title("Matriz de Correlación")
plt.show()

"""# Datos del plasma

**Datos del plasma de 1 día**
"""

# Seleccionar las columnas de interés
columns_of_interest = ["density", "speed", "temperature"]

# Calcular estadísticas descriptivas
statistics = df_plasma_data1[columns_of_interest].describe()

# Mostrar las estadísticas descriptivas
print(statistics)

# Time in datatime
df_plasma_data1['time_tag'] = pd.to_datetime(df_plasma_data1['time_tag'])

# Columnas
density = df_plasma_data1['density']
speed = df_plasma_data1['speed']
temperature = df_plasma_data1['temperature']

# Crea un gráfico en función del tiempo
plt.figure(figsize=(12, 6))
plt.plot(df_plasma_data1['time_tag'],density, label='density')
plt.plot(df_plasma_data1['time_tag'],speed, label='speed')
plt.plot(df_plasma_data1['time_tag'],temperature, label='temperature')

plt.xlabel('Time')
plt.ylabel('Data')
plt.title('Plasma en un día')
plt.legend()
plt.grid(True)
plt.show()

# Convertir la columna "time_tag" a tipo datetime
df_plasma_data1["time_tag"] = pd.to_datetime(df_plasma_data1["time_tag"])
df_k["time_tag"] = pd.to_datetime(df_k["time_tag"])

# Seleccionar las columnas de interés
mag_columns = ["density", "speed", "temperature"]
kp_columns = ["Kp"]

# Combinar los datos en un solo DataFrame usando el índice "time_tag"
combined_data = pd.merge(df_plasma_data1[mag_columns + ["time_tag"]], df_k[kp_columns + ["time_tag"]], on="time_tag")

# Calcular la matriz de correlación
correlation_matrix = combined_data.corr()
print(correlation_matrix)

# Visualizar la matriz de correlación como un mapa de calor
plt.figure(figsize=(10, 6))
plt.imshow(correlation_matrix, cmap="coolwarm", interpolation="nearest", aspect="auto")
plt.colorbar()
plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=45)
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
plt.title("Matriz de Correlación")
plt.show()

"""**Datos del plasma de 3 días**"""

# Seleccionar las columnas de interés
columns_of_interest = ["density", "speed", "temperature"]

# Calcular estadísticas descriptivas
statistics = df_plasma_data3[columns_of_interest].describe()

# Mostrar las estadísticas descriptivas
print(statistics)

# Time in datatime
df_plasma_data3['time_tag'] = pd.to_datetime(df_plasma_data3['time_tag'])

# Columnas
density = df_plasma_data3['density']
speed = df_plasma_data3['speed']
temperature = df_plasma_data3['temperature']

# Crea un gráfico en función del tiempo
plt.figure(figsize=(12, 6))
plt.plot(df_plasma_data3['time_tag'],density, label='density')
plt.plot(df_plasma_data3['time_tag'],speed, label='speed')
plt.plot(df_plasma_data3['time_tag'],temperature, label='temperature')

plt.xlabel('Time')
plt.ylabel('Data')
plt.title('Plasma en un 3 días')
plt.legend()
plt.grid(True)
plt.show()

# Convertir la columna "time_tag" a tipo datetime
df_plasma_data3["time_tag"] = pd.to_datetime(df_plasma_data3["time_tag"])
df_k["time_tag"] = pd.to_datetime(df_k["time_tag"])

# Seleccionar las columnas de interés
mag_columns = ["density", "speed", "temperature"]
kp_columns = ["Kp"]

# Combinar los datos en un solo DataFrame usando el índice "time_tag"
combined_data = pd.merge(df_plasma_data3[mag_columns + ["time_tag"]], df_k[kp_columns + ["time_tag"]], on="time_tag")

# Calcular la matriz de correlación
correlation_matrix = combined_data.corr()
print(correlation_matrix)

# Visualizar la matriz de correlación como un mapa de calor
plt.figure(figsize=(10, 6))
plt.imshow(correlation_matrix, cmap="coolwarm", interpolation="nearest", aspect="auto")
plt.colorbar()
plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=45)
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
plt.title("Matriz de Correlación")
plt.show()

"""# Datos del índice Kp

"""

# Seleccionar las columnas de interés
columns_of_interest = ["Kp", "a_running", "station_count"]

# Calcular estadísticas descriptivas
statistics = df_k[columns_of_interest].describe()

# Mostrar las estadísticas descriptivas
print(statistics)

# Time in datatime
df_k['time_tag'] = pd.to_datetime(df_k['time_tag'])

# Columnas
Kp = df_k['Kp']
a_running = df_k['a_running']
station_count = df_k['station_count']

# Crea un gráfico en función del tiempo
plt.figure(figsize=(12, 6))
plt.plot(df_k['time_tag'],Kp, label='Kp')
plt.plot(df_k['time_tag'],a_running, label='a_running')
plt.plot(df_k['time_tag'],station_count, label='station_count')

plt.xlabel('Time')
plt.ylabel('Data')
plt.title('Planetary k index')
plt.legend()
plt.grid(True)
plt.show()

"""# Correlación del Plasma con el Campo Magnético de la Tierra

**Datos de un día**
"""

# Convertir la columna "time_tag" a tipo datetime
df_mag_data1["time_tag"] = pd.to_datetime(df_mag_data1["time_tag"])
df_plasma_data1['time_tag'] = pd.to_datetime(df_plasma_data1['time_tag'])

# Seleccionar las columnas de interés
mag_columns = ["bx_gsm", "by_gsm", "bz_gsm","lon_gsm","lat_gsm","bt"]
plasma_columns = ["density", "speed", "temperature"]

# Combinar los datos en un solo DataFrame usando el índice "time_tag"
combined_data = pd.merge(df_mag_data1[mag_columns + ["time_tag"]], df_plasma_data1[plasma_columns + ["time_tag"]], on="time_tag")

# Calcular la matriz de correlación
correlation_matrix_p_m = combined_data.corr()
print(correlation_matrix_p_m)

# Visualizar la matriz de correlación como un mapa de calor
plt.figure(figsize=(10, 6))
plt.imshow(correlation_matrix_p_m, cmap="coolwarm", interpolation="nearest", aspect="auto")
plt.colorbar()
plt.xticks(range(len(correlation_matrix_p_m.columns)), correlation_matrix_p_m.columns, rotation=45)
plt.yticks(range(len(correlation_matrix_p_m.columns)), correlation_matrix_p_m.columns)
plt.title("Matriz de Correlación Plasma y Campo Magnético del viento solar")
plt.show()

"""**En tres días**"""

# Convertir la columna "time_tag" a tipo datetime
df_mag_data3["time_tag"] = pd.to_datetime(df_mag_data3["time_tag"])
df_plasma_data3['time_tag'] = pd.to_datetime(df_plasma_data3['time_tag'])

# Seleccionar las columnas de interés
mag_columns = ["bx_gsm", "by_gsm", "bz_gsm","lon_gsm","lat_gsm","bt"]
plasma_columns = ["density", "speed", "temperature"]

# Combinar los datos en un solo DataFrame usando el índice "time_tag"
combined_data = pd.merge(df_mag_data3[mag_columns + ["time_tag"]], df_plasma_data3[plasma_columns + ["time_tag"]], on="time_tag")

# Calcular la matriz de correlación
correlation_matrix_p_m = combined_data.corr()
print(correlation_matrix_p_m)

# Visualizar la matriz de correlación como un mapa de calor
plt.figure(figsize=(10, 6))
plt.imshow(correlation_matrix_p_m, cmap="coolwarm", interpolation="nearest", aspect="auto")
plt.colorbar()
plt.xticks(range(len(correlation_matrix_p_m.columns)), correlation_matrix_p_m.columns, rotation=45)
plt.yticks(range(len(correlation_matrix_p_m.columns)), correlation_matrix_p_m.columns)
plt.title("Matriz de Correlación Plasma y Campo Magnético del viento solar")
plt.show()