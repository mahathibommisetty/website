import streamlit as st


st.set_page_config(layout='wide')
tab1, tab2, tab3, tab4 = st.tabs(['if-else','for-loop','while-loop','do-while'])

with tab1:
    st.write("hi")

with tab2:
    st.write("hi")
    tabq, tabw, tabe, tabr = st.tabs(['12','13','14','15'])

    with tabq:
        st.write('tabq')

    with tabw:
        st.write('tabw')

with tab3:
    st.write("hi")

with tab4:
    st.write("hi")