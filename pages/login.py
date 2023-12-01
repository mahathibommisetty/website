import streamlit as st
import pandas as pd
try:
  df = pd.read_csv("BWEC Logins.csv")
  st.table(df)
