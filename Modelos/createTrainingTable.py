# %% Imports
import pandas as pd
import numpy as np

# %% Files
OD = pd.read_csv('Datos/Train Data DNN/OD.csv')
DS = pd.read_csv('Datos/Train Data DNN/TRAINING_FEATURES.csv')
DS.set_index('Hash', inplace=True)

# %% Create bigass table
with open('Datos/Train Data DNN/TRAINING_TABLE.csv') as f:
    start_columns = ['start_' + i for i in DS.columns]
    end_columns = ['end_' + i for i in DS.columns]

    start_columns_string = ','.join(start_columns)
    end_columns_string = ','.join(end_columns)
    columns = start_columns_string + ',' + end_columns_string + ',trips\n'
    f.write(columns)
    for fila in OD:
        start_data = ','.join(DS[fila[1]])
        end_data = ','.join(DS[fila[1]])
        trips = format(fila[2])
        f.write(start_data + ',' + end_data + ',' + trips + '\n')
