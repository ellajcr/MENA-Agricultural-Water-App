import pandas as pd

from data.aquastat_data import water_data as wd

# Filtering for irrustrial Agriculture Water Use Efficiency
irr_use = wd[wd['Variable'] == 'SDG 6.4.1. Irrigated Agriculture Water Use Efficiency']

# Dropping extra columns
extraneous = ['Unit', 'Symbol', 'Variable']
irr_use = irr_use.drop(columns=extraneous)

# Dropping years without data for all countries
nd = ['1965', '1970', '1975', '1980', '1985']
irr_use = irr_use.drop(columns=nd)

# Converting numeric columns to float
numeric_columns = irr_use.columns[1:].tolist()
irr_use[numeric_columns] = irr_use[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Plotting the data
irr_use.set_index('Country', inplace=True)
irr_use = irr_use.T

