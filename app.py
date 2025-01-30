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

# Define the field name mapping (Old Field → New Field)
FIELD_RENAME_MAP = {
    "createdAt": "Created Date",
    "updatedAt": "Updated Date",
    "requestDate": "Request Date",
    "status": "Status",
    "productName": "Product Name",
    "productImage": "Product Image",
    "type": "Type",
    "category": "Category",
    "cuisine": "Cuisine",
    "timeOfDay": "Time of Day",
    "productType": "Product Type"
}

def transform_record(record):
    transformed = {}
    for key, value in record.items():
        new_key = FIELD_RENAME_MAP.get(key, key)  # Rename if mapped
        transformed[new_key] = value  # Keep other values as is

    return transformed

df.rename(columns=FIELD_RENAME_MAP, inplace=True)

# Streamlit UI
st.title("Requested Products")
# st.write("This table updates when the page is refreshed.")

# Show data table
st.markdown("""
    <style>
    .dataframe-container {
        max-width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

st.dataframe(df, height=350)
