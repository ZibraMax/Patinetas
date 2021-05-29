# %% Imports
import pandas as pd
import numpy as np
from tqdm import tqdm
# %% Files
OD = pd.read_csv('OD.csv')
DS = pd.read_csv('TRAINING_FEATURES.csv')
DS.set_index('Hash', inplace=True)
DS.dropna(inplace=True)
OD.dropna(inplace=True)
OD = OD.values


def toString(a):
    return [format(i) for i in a]


# %% Create bigass table
with open('TRAINING_TABLE_COMPLETE.csv', 'w') as f:
    start_columns = ['start_' + i for i in DS.columns]
    end_columns = ['end_' + i for i in DS.columns]

    start_columns_string = ','.join(start_columns)
    end_columns_string = ','.join(end_columns)
    columns = start_columns_string + ',' + end_columns_string + ',trips\n'
    f.write(columns)

    C = 0
    for i, fila in enumerate(tqdm(OD)):
        try:
            start_data = ','.join(toString(DS.loc[fila[0]].values))
            end_data = ','.join(toString(DS.loc[fila[1]].values))
            trips = format(fila[2])
            f.write(start_data + ',' + end_data + ',' + trips + '\n')
        except:
            C += fila[-1]
            if C % 1000 == 0:
                print(f'No se pudo con el dato {C}')

# %%
