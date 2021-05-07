import argparse

import h2o
import pandas as pd
from h2o.estimators.random_forest import H2ORandomForestEstimator
parser = argparse.ArgumentParser(description='Ramdom Forest Model')
parser.add_argument("-i","--input", action='store', help="Input relative path to .csv input file (info in README.md)", type=str,default='input.csv')
parser.add_argument("-o","--output", action='store', help="Output file name with extension", type=str,default='output.csv')
args = parser.parse_args()
input_file = args.input
output_file= args.output

h2o.init(nthreads = -1, max_mem_size = 6)

#This model was created to predict the value (price by square meter) of each feature, then, this parameter will be used to predict population density.
print('----------------------- Model is being loaded -----------------------')
ModeloValor = h2o.import_mojo('ModeloValor.zip')
print('--------------------- Model loaded successfully ---------------------')

#The original dataset for predicting is loaded
print('------------------- Loading predicting dataset -------------------')
datosPredecirValor = h2o.upload_file(path=input_file)
#input must contain a table with the following columns: SES, Valor, CBD, Alimentador, Parques, Estaciones, Vias, Salud, Colegios
#The column names of the input table have to match with the columns names mentioned below. The order of the table is not relevant.
print('------------------- Dataset loaded successfully ------------------')
#Predict Value over each feature
print('----------------------- Predicting "Valor" -----------------------')
predictions = ModeloValor.predict(datosPredecirValor)
print('----------------- "Valor" predicted successfully -----------------')
#The model is deleted, because, models can be very large.
del ModeloValor

#The "Valor" column is assigned to each feature
print('----------------- Joining predictions on original dataset -----------------')
datosPredecidosValor = datosPredecirValor.concat(predictions)
columnas = datosPredecirValor.columns
columnas.append('Valor')
datosPredecidosValor.set_names(columnas)
print('--------------------- Predictions joined successfully ---------------------')

#Loads the model for predicting population density
print('----------------------- Model is being loaded -----------------------')
ModeloDensidad = h2o.import_mojo('ModeloDensidad.zip')
print('--------------------- Model loaded successfully ---------------------')

#Predict population density over each feature of the dataset
print('----------------------- Predicting "PobDens(Predecido)" -----------------------')
predictions = ModeloDensidad.predict(datosPredecidosValor)
columnas = datosPredecidosValor.columns
print('----------------- "PobDens(Predecido)" predicted successfully -----------------')

#Assign the "DensPob(Predecido)" column containing the predicted population density for the feature
print('----------------- Joining predictions on original dataset -----------------')
datosPredecidos = datosPredecidosValor.concat(predictions)
columnas.append('DensPob(Predecido)')
datosPredecidos.set_names(columnas)
del ModeloDensidad
print('--------------------- Predictions joined successfully ---------------------')

#Save the results to a CSV file.
print('--------------------- Saving predictions ---------------------')
ph2o = pd.DataFrame(datosPredecidos.as_data_frame())
ph2o.to_csv(output_file)
print('--------------- Predictions saved successfully ---------------')
