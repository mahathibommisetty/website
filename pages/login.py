import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
df = pd.read_csv('BWEC Logins.csv')
st.data_editor(df, hide_index=True, use_container_width=True)

