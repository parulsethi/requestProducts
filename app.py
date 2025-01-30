import streamlit as st
import pandas as pd
import requests

# API URL (Replace with your actual API)
API_URL = "https://6yazzrln3tcxp4biq7fn3b5fzq0djvug.lambda-url.ap-south-1.on.aws/"

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
df['productImage'] = df['productImage'].apply(lambda x: x[0] if isinstance(x, list) else x)
# Streamlit UI
st.title("Requested Products")
# st.write("This table updates when the page is refreshed.")

# Show data table
# st.dataframe(df)
st.markdown("""
    <style>
    .dataframe-container {
        max-width: 100%;
    }
    </style>
""", unsafe_allow_html=True)
st.dataframe(df, height=300)
