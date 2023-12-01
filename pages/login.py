import streamlit as st
import pandas as pd

df = pd.read_csv("BWEC logins.csv")
st.table(df)
