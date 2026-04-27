import pandas as pd
import glob
import os
import streamlit as st

@st.cache_data
def load_all_data():
    """Loads cleaned CSVs from the notebooks/data/ folder."""
    # This path matches your tree structure exactly
    data_path = "notebooks/data/*_clean.csv" 
    all_files = glob.glob(data_path)
    
    if not all_files:
        st.error("No cleaned data files found in notebooks/data/. Please check the path.")
        return pd.DataFrame()

    df_list = []
    for filename in all_files:
        df = pd.read_csv(filename)
        # Extract country name from filename (e.g., 'ethiopia' from 'ethiopia_clean.csv')
        country_name = os.path.basename(filename).split('_')[0].capitalize()
        df['Country'] = country_name
        
        # Ensure DATE is datetime
        if 'DATE' in df.columns:
            df['DATE'] = pd.to_datetime(df['DATE'])
        
        df_list.append(df)
    
    return pd.concat(df_list, ignore_index=True)

def filter_data(df, countries, year_range, variable):
    """Filters data based on sidebar selections."""
    filtered = df[
        (df['Country'].isin(countries)) &
        (df['YEAR'] >= year_range[0]) &
        (df['YEAR'] <= year_range[1])
    ]
    return filtered