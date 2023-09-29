import pandas as pd

from data.aquastat_data import water_data as wd

# Filtering Overall Water Use Efficiency
eff_use = wd[wd['Variable'] == 'SDG 6.4.1. Water Use Efficiency']

# Dropping extra columns
extraneous = ['Unit', 'Symbol', 'Variable']
eff_use = eff_use.drop(columns=extraneous)

# Combining duplicate Country rows 
eff_use = eff_use.groupby(['Country']).sum().reset_index()

# Converting numeric columns to float
numeric_columns = eff_use.columns[1:].tolist()
eff_use[numeric_columns] = eff_use[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Plotting the data
eff_use.set_index('Country', inplace=True)
eff_use = eff_use.T