import pandas as pd

from aquastat_data import water_data as wd

# Filtering for Industrial Agriculture Water Use Efficiency
ind_use = wd[wd['Variable'] == 'SDG 6.4.1. Irrigated Agriculture Water Use Efficiency']

# Dropping extra columns
extraneous = ['Unit', 'Symbol', 'Variable']
ind_use = ind_use.drop(columns=extraneous)

# Dropping years without data for all countries
nd = ['1965', '1970', '1975', '1980', '1985']
ind_use = ind_use.drop(columns=nd)

# Converting numeric columns to float
numeric_columns = ind_use.columns[1:].tolist()
ind_use[numeric_columns] = ind_use[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Plotting the data
ind_use.set_index('Country', inplace=True)
ind_use = ind_use.T
print(ind_use)
