import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout='wide')
with st.container():
    components.iframe("https://chat.openai.com/share/c299a9a9-fff6-4974-95ca-70915f52468d", height=750)

