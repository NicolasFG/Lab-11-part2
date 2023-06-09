import pandas as pd

# Lectura del archivo CSV
data = pd.read_csv('baby-names-state.csv')

# Filtrar los datos para obtener solo los registros de California
california_data = data[data['state_abb'] == 'CA']

# Obtener la frecuencia del nombre repetido
frecuencia_nombres = california_data['name'].value_counts()

# Obtener el nombre más común y su frecuencia
nombre_comun = frecuencia_nombres.idxmax()
frecuencia_comun = frecuencia_nombres.max()

print("El nombre más común en California es:", nombre_comun)
print("Frecuencia:", frecuencia_comun)