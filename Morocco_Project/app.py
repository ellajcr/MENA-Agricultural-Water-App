import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from water_withdrawal_data import ag_use
from ag_efficiency_data import irr_use
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

# 1. Plot Agricultural Water Withdrawal data
def plot_agricultural_water_withdrawal(ag_use):
    with col1:
        st.markdown("<h4>1. Agricultural Water Withdrawal</h4>", unsafe_allow_html=True)
        st.markdown("###### 'This is the annual quantity of self-supplied water withdrawn for irrigation, livestock, and aquaculture purposes. Includes water from primary renewable and secondary freshwater resources, as well as water from over-abstraction of renewable groundwater or withdrawal from fossil groundwater, direct use of agricultural drainage water, direct use of (treated) wastewater, and desalinated water.  Water for the dairy and meat industries and industrial processing of harvested agricultural products is included under industrial water withdrawal.' (AQUASTAT)")
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
def plot_ind_ag_efficiency(irr_use):
    with col1:
        st.markdown("<h4>2. Irrigated Agriculture Water Use Efficiency</h4>", unsafe_allow_html=True)
        st.markdown("###### 'Annual quantity of water used for irrigation purposes. It includes water from renewable freshwater resources, as well as water from over-abstraction of renewable groundwater or abstraction of fossil groundwater, direct use of agricultural drainage water, (treated) wastewater, and desalinated water. Determined by the monetary value added of the agriculture sector divided by the volume of water used for irrigation.' (AQUASTAT)", unsafe_allow_html=True)
        # Allow the user to select a country
        fig, ax = plt.subplots(figsize=(10, 6))
        for country in agriculture_countries:
            subset = irr_use.loc[irr_use.index, [country]]
            ax.plot(subset.index, subset[country], marker='o', label=country)

        plt.xlabel('Year')
        plt.ylabel('Irrigated Ag Water Use Efficiency (USD/m3)')
        plt.title('MENA Irrigated Agriculture Water Use Efficiency 1995-2020')
        plt.legend(agriculture_countries, title='Country')
        plt.xticks(rotation=45)
        st.pyplot(fig)

# 3. Plot Overall Water Use Efficiency
def plot_overall_efficiency(eff_use):
    with col1:
        st.markdown("<h4>3. Overall Water Use Efficiency</h4>", unsafe_allow_html=True) 
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
        st.markdown("<h4>4. Overall Water Stress</h4>", unsafe_allow_html=True) 
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
plot_ind_ag_efficiency(irr_use)
plot_overall_efficiency(eff_use)
plot_overall_stress(water_stress)

# Works Cited section
st.markdown("<h4>Works Cited</h4>")
st.markdown("###### 'AQUASTAT - FAO's Global Information System on Water and Agriculture'. 2023. AQUASTAT. https://www.fao.org/aquastat/en/?id=4250")




