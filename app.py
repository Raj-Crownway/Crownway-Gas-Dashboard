import streamlit as st
import pandas as pd

st.set_page_config(page_title="Crownway Gas Monitor", layout="wide")
st.title("⛽ Crownway Gas Price Monitor")
st.subheader("Real-time gas prices within 2 miles of 8501 Morganford Rd")

try:
    df = pd.read_csv("gas_data.csv")
    st.dataframe(df, use_container_width=True)
except FileNotFoundError:
    st.warning("Live gas data is not available yet. Please run the scraper.")
