import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from water_withdrawal_data import ag_use
from ag_efficiency_data import ind_use
from water_efficiency_data import eff_use
from water_stress_data import water_stress

# 1. SETTING UP APP
st.set_page_config(layout="wide")
image = st.image('farming_header.png', caption='Photos from UW PoE 2023 Morocco study abroad program.', use_column_width=True)
st.markdown("<h1 style='text-align: center;'>MENA Agricultural Water Usage</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'>This app uses the AQUASTAT Dissemination System dataset to investigate water usage trends in the MENA region.</h5>",  unsafe_allow_html=True)

# Sidebar with multiselect widget
agriculture_countries = ['Morocco', 'Syrian Arab Republic', 'Algeria', 'Yemen', 'Egypt', 'Tunisia']
selected_countries = st.sidebar.multiselect('Select Countries', agriculture_countries, default=agriculture_countries)

# Create a single column to display the graphs
col1 = st.container()

# Function to create smaller numbered titles
def numbered_title(text, size=4):
    return f"<h{size}>{text}</h{size}>"

# 1. Plot Agricultural Water Withdrawal data
def plot_agricultural_water_withdrawal(ag_use):
    with col1:
        st.markdown(numbered_title("1. Agricultural Water Withdrawal"), unsafe_allow_html=True)
        st.markdown("###### This is the annual quantity of self-supplied water withdrawn for irrigation, livestock, and aquaculture purposes. Includes water from primary renewable and secondary freshwater resources, as well as water from over-abstraction of renewable groundwater or withdrawal from fossil groundwater, direct use of agricultural drainage water, direct use of (treated) wastewater, and desalinated water.  Water for the dairy and meat industries and industrial processing of harvested agricultural products is included under industrial water withdrawal.")
        fig, ax = plt.subplots(figsize=(10, 6))
        for country in selected_countries:
            subset = ag_use.loc[ag_use.index, [country]]
            ax.plot(subset.index, subset[country], marker='o', label=country)

        # Labeling
        plt.xlabel('Year')
        plt.ylabel('Ag Water Withdrawal (% of renewable water resources)')
        plt.title('MENA Agricultural Water Withdrawal 1995-2020')
        plt.xticks(rotation=45)
        plt.legend()
        st.pyplot(fig)

# 2. Plot Industrial Agriculture Water Use Efficiency
def plot_ind_ag_efficiency(ind_use):
    with col1:
        st.markdown(numbered_title("2. Industrial Agriculture Water Use Efficiency"), unsafe_allow_html=True) 
        # Allow the user to select a country
        fig, ax = plt.subplots(figsize=(10, 6))
        for country in agriculture_countries:
            subset = ind_use.loc[ind_use.index, [country]]
            ax.plot(subset.index, subset[country], marker='o', label=country)

        plt.xlabel('Year')
        plt.ylabel('Industrial Ag Water Use Efficiency (USD/m3)')
        plt.title('MENA Industrial Agriculture Water Use Efficiency 1995-2020')
        plt.legend(agriculture_countries, title='Country')
        plt.xticks(rotation=45)
        st.pyplot(fig)

# 3. Plot Overall Water Use Efficiency
def plot_overall_efficiency(eff_use):
    with col1:
        st.markdown(numbered_title("3. Overall Water Use Efficiency"), unsafe_allow_html=True) 
        fig, ax = plt.subplots(figsize=(10, 6))
        for country in selected_countries:
            subset = eff_use.loc[eff_use.index, [country]]
            ax.plot(subset.index, subset[country], marker='o', label=country)

        # Labeling
        plt.xlabel('Year')
        plt.ylabel('Water Use Efficiency (USD/m3)')
        plt.title('MENA Water Use Efficiency 1995-2020')
        plt.xticks(rotation=45)
        plt.legend()
        st.pyplot(fig)

# 4. Plot Overall Water Stress
def plot_overall_stress(water_stress):
    with col1:
        st.markdown(numbered_title("4. Overall Water Stress"), unsafe_allow_html=True) 
        fig, ax = plt.subplots(figsize=(10, 6))
        for country in selected_countries:
            subset = water_stress.loc[water_stress.index, [country]]
            ax.plot(subset.index, subset[country], marker='o', label=country)

        # Labeling
        plt.xlabel('Year')
        plt.ylabel('Water Stress (%)')
        plt.title('MENA Water Stress 1975-2020')
        plt.xticks(rotation=45)
        plt.legend()
        st.pyplot(fig)

# Call the functions to display each graph one below the other
plot_agricultural_water_withdrawal(ag_use)
plot_ind_ag_efficiency(ind_use)
plot_overall_efficiency(eff_use)
plot_overall_stress(water_stress)

# Works Cited section
st.title("Works Cited")
st.markdown(
    1. Author 1, Title of Reference 1, Publisher, Year.
    2. Author 2, Title of Reference 2, Publisher, Year.
    3. Author 3, Title of Reference 3, Publisher, Year.
)




