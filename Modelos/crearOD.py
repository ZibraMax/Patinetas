import pandas as pd
import numpy as np
from tqdm import tqdm

PATH_DATOS_BOGOTA = "Datos/Capas/bogota_data/bogota_data.csv"

# Leer datos
df = pd.read_csv(PATH_DATOS_BOGOTA)

# Eliminar datos que son nulos
df.dropna(inplace=True)

# Quedarse solo con las columnas interesantes (el tiempo todavía no lo tenemos en cuenta)
dfviajes = df[['sta_geohash', 'end_geohash',
               'sta_time_bogota', 'end_time_bogota']]

# Con este proceso se encuentran los nombres de los geohashes. Como son distintos en origen y destino se concatenan y unifican
labelsstart = dfviajes.sta_geohash.unique().tolist()
labelsend = dfviajes.end_geohash.unique().tolist()
labels = labelsstart+labelsend

# Aqui es la unificación
labelsgeo = np.unique(labels)

# Se crean diccionarios con ceros para que cuenten los viajes. Esta es quizas la manera mas eficiente de hacerlo para estos datos
dict_geo = {}
for labelo in labelsgeo:
    dictpart = {}
    for labeld in labelsgeo:
        dictpart[labeld] = 0
    dict_geo[labelo] = dictpart

# Se itera sobre los datos para contar los viajes que se realizan en cada par origen destino
datanumpy = dfviajes.values
for i, l in enumerate(tqdm(datanumpy)):
    o = l[0]
    d = l[1]
    dict_geo[o][d] += 1

# Se crea la matriz origen destino COMPLETA. Incluye los valores que son 0.
OD = []
for o in tqdm(dict_geo.keys()):
    for d in dict_geo[o].keys():
        OD += [[o, d, dict_geo[o][d]]]
np.savetxt('Datos/Train Data DNN/OD.csv', OD, delimiter=',', fmt='%s')

# Se crea la matriz origen destino LIVIANA. Solo incluye los valores distintos a 0.
ODLW = []
VIAJES_TOTALES = 0
for l in OD:
    if not l[2] == 0:
        VIAJES_TOTALES += l[2]
        ODLW += [l]
np.savetxt('Datos/Train Data DNN/ODLW.csv', ODLW, delimiter=',', fmt='%s')

# Principio de conservación de viajes
if len(dfviajes) == len(datanumpy) == VIAJES_TOTALES:
    print('Check')
else:
    print(len(dfviajes), len(datanumpy), VIAJES_TOTALES)
    raise Exception(
        'ERROR: Se perdieron o ganaron viajes en el proceso REVISAR')
