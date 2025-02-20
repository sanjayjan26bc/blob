# 26-Dec - Working code - grid, editable, and waterfall
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

# Title of the app
st.set_page_config(page_title="Factor Analysis", layout="wide")

# Function to load the data
@st.cache_data()
def load_data():
    # Load data from CSV (assuming 'ex_fake_data.csv' is in your working directory)
    data = pd.read_csv('ex_fake_data.csv')
    return data

# Load the data
data = load_data()

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data)

# *** START *** CODE TO GROUP DATA AND SHOW 
# Below are the columns: Factor L1, Factor L2, Factor L3, Factor L4, BU Level 1, BU Level 2, Prior Measure, Current Measure, Value

# Set up the AG Grid configuration with row grouping, aggregation, and editable columns
gb = GridOptionsBuilder.from_dataframe(df)

# Configure the aggregation for different levels of grouping and make them editable
gb.configure_column("Factor L1", enableRowGroup=True, aggFunc="sum", rowGroup=True, hide=True, editable=True)
gb.configure_column("Factor L2", enableRowGroup=True, aggFunc="sum", rowGroup=True, hide=True, editable=True)

# Hide additional columns that are not needed in the grid but still make them editable
gb.configure_column("Factor L1", hide=False, editable=True)
gb.configure_column("Factor L2", hide=False, editable=True)
gb.configure_column("Factor L3", hide=False, editable=True)
gb.configure_column("Factor L4", hide=False, editable=True)
gb.configure_column("BU Level 1", hide=False, editable=True)
gb.configure_column("BU Level 2", hide=False, editable=True)
gb.configure_column("Prior Measure", hide=True, editable=True)
gb.configure_column("Current Measure", hide=True, editable=True)

# Configure the "Value" column to show aggregation and make it editable
gb.configure_column("Value", aggFunc="sum", enableValue=True, editable=True)

# Get the grid options and build the grid
grid_options = gb.build()

# Display AG Grid with the specified options, with autoHeight and without scroll bar
grid_response = AgGrid(
    df,
    gridOptions=grid_options,
    enable_enterprise_modules=True,
    height=400,  # You can increase the height if necessary
    fit_columns_on_grid_load=True,  # Automatically fit columns to content on grid load
    domLayout='autoHeight',  # Auto-adjust grid height based on content
    autoSizeColumns=True,  # Automatically adjust column sizes based on content
    width=300  # Adjust the width of the grid container (in pixels)
)

