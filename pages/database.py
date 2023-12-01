import sqlite3
import streamlit as st

conn = sqlite3.connect('example.db')

cursor = conn.cursor()

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS example_table (
#         id INTEGER PRIMARY KEY,
#         name TEXT,
#         age INTEGER
#     )
# ''')

name = st.text_input("Enter Your name")
age = st.number_input("Enter Your Age")

if st.button("Add"):
    cursor.execute("INSERT INTO example_table (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    st.toast("Added Successfully")
    st.success("Added Successfully")
    st.



