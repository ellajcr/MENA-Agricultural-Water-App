import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from ind_ag_data import ind_use

# 1. SETTING UP GRAPH
st.title('MENA Agricultural Water Usage')
st.write('This app uses the AQUASTAT Dissemination System dataset to investigate water usage trends in the MENA region.')
# Creating two rows and two columns
col1, col2 = st.beta_columns(2)

# 2. ADDING GRAPHS
# MENA Agricultural Water Withdrawal Graph
with col1:
    # Widgets for usSer interaction
    st.title('MENA Agricultural Water Withdrawal 1995-2020')
    selected_countries = st.multiselect(
        'Select Countries', ag_use['Country'].unique())

    # Allow user to select country
    filt_data = ag_use[ag_use['Country'].isin(selected_countries)]

    fig, ax = plt.subplots(figsize=(10, 6))
    for country in selected_countries:
        subset = filt_data[filt_data['Country'] == country]
        ax.plot(subset.columns[1:], subset.iloc[0, 1:],
                marker='o', label=country)

    # Labeling
    plt.xlabel('Year')
    plt.ylabel('Ag Water Withdrawal (% of renewable water resources)')
    plt.title('MENA Agricultural Water Withdrawal 1995-2020')
    plt.xticks(rotation=45)
    plt.legend()
    st.pyplot(fig)

# MENA Industrial Agriculture Water Use Efficiency
with col2:
    ind_use.set_index('Country', inplace=True)
    ind_use = ind_use.T
    ax = ind_use.plot(kind='line', marker='o', figsize=(10, 6))

    plt.xlabel('Year')
    plt.ylabel('Industrial Ag Water Use Efficiency (USD/m3)')
    plt.title('MENA Industrial Agriculture Water Use Efficiency 1995-2020')
    plt.legend(ind_use['Country'], title='Country')
    plt.xticks(rotation=45)

    plt.show()
