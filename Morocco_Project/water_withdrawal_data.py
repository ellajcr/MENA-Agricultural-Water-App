import pandas as pd

from aquastat_data import water_data as wd

# Filtering for agricultural water withdrawal
ag_use = wd[wd['Variable'] == 'Agricultural water withdrawal as % of total renewable water resources']

# Dropping extra columns
extraneous = ['Unit', 'Symbol', 'Variable']
ag_use = ag_use.drop(columns=extraneous)

# Combining duplicate Country rows 
ag_use = ag_use.groupby(['Country']).sum().reset_index()

# Dropping years without data for all countries
nd = ['1965', '1970', '1975', '1980', '1985']
ag_use = ag_use.drop(columns=nd)

# Converting numeric columns to float
numeric_columns = ag_use.columns[1:].tolist()
ag_use[numeric_columns] = ag_use[numeric_columns].apply(pd.to_numeric, errors='coerce')

ag_use.set_index('Country', inplace=True)
ag_use = ag_use.T