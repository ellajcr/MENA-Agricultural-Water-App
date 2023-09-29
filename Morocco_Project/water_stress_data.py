import pandas as pd

from aquastat_data import water_data as wd

# Filtering Water Stress
water_stress = wd[wd['Variable'] == 'SDG 6.4.2. Water Stress']

# Dropping extra columns
extraneous = ['Unit', 'Symbol', 'Variable']
water_stress = water_stress.drop(columns=extraneous)
water_stress.head(50)

# Combining duplicate Country rowater_stress 
water_stress = water_stress.groupby(['Country']).sum().reset_index()

# Dropping years without data for all countries
nd = ['1965', '1970']
water_stress = water_stress.drop(columns=nd)

# Converting numeric columns to float
numeric_columns = water_stress.columns[1:].tolist()
water_stress[numeric_columns] = water_stress[numeric_columns].apply(pd.to_numeric, errors='coerce')

water_stress.set_index('Country', inplace=True)
water_stress = water_stress.T