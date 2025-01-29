import streamlit as st
import pandas as pd
import requests

# API URL (Replace with your actual API)
API_URL = "https://api.example.com/data"

# Fetch JSON data from API
@st.cache_data
def fetch_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        st.error("Failed to fetch data")
        return pd.DataFrame()

# Load data
df = fetch_data()

# Streamlit UI
st.title("Live Data Viewer")
st.write("This table updates when the page is refreshed.")

# Show data table
st.dataframe(df)
