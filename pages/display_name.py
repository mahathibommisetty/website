import streamlit as st
st.set_page_config(layout='wide')
st.title('c programming')
st.subheader("Sample")
st.code("""
        #include<stdio.h>
        int main(){
        char name[10];
        printf("please enter your name: ");
        scanf("%s",name);
        printf("your name is %s",name);
        }
        """)
[theme]
base="light"
primaryColor="blue"
