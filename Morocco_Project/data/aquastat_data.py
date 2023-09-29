import pandas as pd

# Load MENA data from AQUASTAT
aquastat_data = pd.read_csv("AQUASTAT Dissemination System.csv", sep=",")

# Fix column names
aquastat_data.columns = aquastat_data.columns.str.replace(
    '"', '').str.replace(' ', '')

# Remove leading and trailing whitespace from 'Variable' and 'Country' columns
aquastat_data['Variable'] = aquastat_data['Variable'].str.strip()
aquastat_data['Variable'] = aquastat_data['Variable'].str.lstrip()
aquastat_data['Country'] = aquastat_data['Country'].str.strip()
aquastat_data['Country'] = aquastat_data['Country'].str.lstrip()

# Filter for top 7 agriculturally dependent MENA countries
agriculture_countries = ['Morocco', 'Syrian Arab Republic',
                         'Algeria', 'Yemen', 'Iran', 'Egypt', 'Tunisia']
filtered_data = aquastat_data[aquastat_data['Country'].isin(
    agriculture_countries)]

# Remove extraneous data
water_data = filtered_data[filtered_data['Variable']
                           != 'SDG_6.4.1_Services_Water_Use_Efficiency']
