import streamlit as st
import pandas as pd

st.set_page_config(page_title="Crownway Gas Monitor", layout="wide")
st.title("⛽ Crownway Gas Price Monitor")
st.subheader("Gas stations within 2 miles of 8501 Morganford Rd, Affton, MO")

data = [
    {"Station": "Shell", "Address": "8510 Morganford Rd", "Regular": "$3.45", "Diesel": "$3.89", "Last Updated": "4:00 PM"},
    {"Station": "Circle K", "Address": "8400 Gravois Rd", "Regular": "$3.49", "Diesel": "$3.99", "Last Updated": "4:00 PM"},
    {"Station": "BP", "Address": "8555 Mackenzie Rd", "Regular": "$3.51", "Diesel": "$3.95", "Last Updated": "4:00 PM"}
]

df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)
