# %% Import dataset
from statsmodels.stats.outliers_influence import variance_inflation_factor
import pandas as pd
import seaborn as sb

# %% The dataset
data = pd.read_csv('../Datos/TRAINING_FEATURES_GEOHASH_ORIGINAL.csv')
data.dropna(inplace=True)

# %% Printing first few rows
data.head(20)

# %% The independent variables set
X = data[data.columns[1:-1]]
X = X.apply(pd.to_numeric)
X.head(20)

# # %% Seaborn
# sns_plot = sb.pairplot(X, diag_kind="hist")
# sns_plot.savefig("output2.svg")

# %% VIF dataframe
vif_data = pd.DataFrame()
vif_data["feature"] = X.columns

# %% Calculating VIF for each feature
vif_data["VIF"] = [variance_inflation_factor(X.values, i)
                   for i in range(len(X.columns))]
print(vif_data)
