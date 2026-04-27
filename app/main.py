import streamlit as st
import plotly.express as px
from utils import load_all_data, filter_data

st.set_page_config(page_title="Climate Dashboard", layout="wide")

# Sidebar
st.sidebar.header("Dashboard Filters")
df = load_all_data()

if not df.empty:
    # 1. Country multi-select widget
    countries = st.sidebar.multiselect(
        "Select Countries", 
        options=sorted(df['Country'].unique()), 
        default=["Ethiopia"]
    )
    
    # 2. Year range slider
    min_year, max_year = int(df['YEAR'].min()), int(df['YEAR'].max())
    year_range = st.sidebar.slider("Select Year Range", min_year, max_year, (2015, 2026))

    # Filtering data
    filtered_df = df[
        (df['Country'].isin(countries)) & 
        (df['YEAR'] >= year_range[0]) & 
        (df['YEAR'] <= year_range[1])
    ]

    # --- MAIN UI ---
    st.title("🌍 Climate Vulnerability Dashboard")
    
    if not countries:
        st.warning("Please select at least one country.")
    else:
        # 3. Temperature trend line chart
        st.subheader("Temperature Trend (T2M)")
        fig_line = px.line(
            filtered_df, x='DATE', y='T2M', color='Country',
            color_discrete_map={'Ethiopia': '#2980b9'},
            title="Monthly Temperature Trends"
        )
        st.plotly_chart(fig_line, use_container_width=True)

        # 4. Precipitation distribution boxplot
        st.subheader("Precipitation Distribution (PRECTOTCORR)")
        fig_box = px.box(
            filtered_df, x='Country', y='PRECTOTCORR', color='Country',
            color_discrete_map={'Ethiopia': '#2980b9'},
            title="Precipitation Variability"
        )
        st.plotly_chart(fig_box, use_container_width=True)
else:
    st.error("No data found.")