import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from data.water_withdrawal_data import ag_use
from data.ag_efficiency_data import irr_use
from data.water_efficiency_data import eff_use
from data.water_stress_data import water_stress

# 1. SETTING UP APP
st.set_page_config(layout="wide")
image = st.image('farming_header.png', caption='Photos from UW PoE 2023 Morocco study abroad program.', use_column_width=True)

st.markdown("<h1 style='text-align: center;'>MENA Agricultural Water Usage</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'>Ella Crowder Sept 29, 2023</h5>", unsafe_allow_html=True)
st.markdown(
    """<h6>The MENA region (Middle East/North Africa) encompasses the 
    historical Fertile Crescent, often considered as the cradle of agriculture. Early farmers 
    developed various techniques to manage their water resources (Crabben). With the rising temperatures 
    and frequent droughts of modern climate change, concerns over water conservation have intensified.</h6>""",
    unsafe_allow_html=True
) 
st.markdown(
    """<h6>Among the nations in the MENA region, the Syrian Arab Republic, 
    Algeria, Yemen, Egypt, Morocco, and Tunisia have the greatest reliance on 
    agriculture, forestry, and fishing sectors as a percentage of their GDP (World Bank). 
    These six countries are indicators of whether modern farming practices are creating a sustainable 
    agricultural economy. The following graphs are based on data sourced from AQUASTAT, a comprehensive 
    global dataset created by the Food and Agriculture Organization of the United Nations. 
    (https://www.fao.org/land-water/databases-and-software/aquastat/en/)</h6>""", 
    unsafe_allow_html=True
)
st.markdown(
    """<h6>Despite low scores in water efficiency measures, Morocco displays steady improvement over time. 
    Morocco also has the lowest levels of agricultural water withdrawal and water stress among 
    the six main agricultural countries. These outcomes place Morocco as a leader in agricultural 
    water conservation in the MENA region.</h6>""",
    unsafe_allow_html=True
)

# Sidebar with multiselect widget
agriculture_countries = ['Morocco', 'Syrian Arab Republic', 'Algeria', 'Yemen', 'Egypt', 'Tunisia']
selected_countries = st.sidebar.multiselect('Select Countries', agriculture_countries, default=agriculture_countries)

# Create a single column to display the graphs
col1 = st.container()

# 1. Plot Agricultural Water Withdrawal data
def plot_agricultural_water_withdrawal(ag_use):
    with col1:
        st.markdown("<h4 style='font-weight: bold'>1. Agricultural Water Withdrawal</h4>", unsafe_allow_html=True)
        st.markdown(
            """<h6>'This is the annual quantity of self-supplied water withdrawn 
            for irrigation, livestock, and aquaculture purposes. Includes water from 
            primary renewable and secondary freshwater resources, as well as water 
            from over-abstraction of renewable groundwater or withdrawal from fossil 
            groundwater, direct use of agricultural drainage water, direct use of 
            (treated) wastewater, and desalinated water.  Water for the dairy and 
            meat industries and industrial processing of harvested agricultural 
            products is included under industrial water withdrawal.' (AQUASTAT)</h6>""", 
            unsafe_allow_html=True
        )
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
def plot_irr_ag_efficiency(irr_use):
    with col1:
        st.markdown("<h4 style='font-weight: bold'>2. Irrigated Agriculture Water Use Efficiency</h4>", unsafe_allow_html=True)
        st.markdown(
            """<h6>'Annual quantity of water used for irrigation purposes. 
            It includes water from renewable freshwater resources, as well as water
            from over-abstraction of renewable groundwater or abstraction of 
            fossil groundwater, direct use of agricultural drainage water, 
            (treated) wastewater, and desalinated water. Determined by the monetary
            value added of the agriculture sector divided by the volume of water used 
            for irrigation.' (AQUASTAT glossary)</h6>""", 
            unsafe_allow_html=True
        )
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
        st.markdown("<h4 style='font-weight: bold'>3. Overall Water Use Efficiency</h4>", unsafe_allow_html=True) 
        st.markdown(
            """<h6>'The monetary value added across all sectors divided by the volume 
            of water used for irrigation.' (AQUASTAT glossary)</h6>""", 
            unsafe_allow_html=True
        )
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
        st.markdown("<h4 style='font-weight: bold'>4. Overall Water Stress</h4>", unsafe_allow_html=True) 
        st.markdown(
            """<h6>'Ratio between total freshwater withdrawn by all major sectors 
            and total renewable freshwater resources, after taking into account 
            environmental water requirements. This indicator provides an estimate 
            of pressure by all sectors on the country’s renewable freshwater resources. 
            Total freshwater withdrawal divided by total renewable water resources.'(AQUASTAT glossary)</h6>""", 
            unsafe_allow_html=True
        )
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
plot_irr_ag_efficiency(irr_use)
plot_overall_efficiency(eff_use)
plot_overall_stress(water_stress)

# Works Cited section
st.markdown("<h4 style='text-align: center; font-weight: bold'>Works Cited</h4>", unsafe_allow_html=True)
st.markdown(
    """
    ###### 'AQUASTAT home - FAO's Global Information System on Water and Agriculture'. 2023. AQUASTAT.
    https://www.fao.org/land-water/databases-and-software/aquastat/en/.
    """, 
    unsafe_allow_html=True
)
st.markdown(
    """
    ###### 'AQUASTAT glossary - FAO's Global Information System on Water and Agriculture'. 2023. AQUASTAT.
    https://www.fao.org/faoterm/terminology-at-fao/en/
    """, 
    unsafe_allow_html=True
)
st.markdown(
    """
    ###### 'Agriculture, forestry, and fishing, value added (% of GDP) - Middle East & North Africa'. 2023. The World Bank.
    https://data.worldbank.org/indicator/NV.AGR.TOTL.ZS?locations=ZQ.
    """, 
    unsafe_allow_html=True
)
st.markdown(
    """
    ###### Crabben, Jan. “Agriculture in the Fertile Crescent & Mesopotamia”. March 22, 2023. World History Encyclopedia. https://www.worldhistory.org/article/9/agriculture-in-the-fertile-crescent--mesopotamia/
    """, 
    unsafe_allow_html=True
)
