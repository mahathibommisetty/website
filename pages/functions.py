import streamlit as st
st.set_page_config(layout='wide')
st.title('c programming')
st.title("functions")
tab1, tab2, tab3 = st.tabs(["operations", "factorial", "name and lucky number"])
with tab1:
  st.subheader("operations")
  st.code("""
  #include<stdio.h>
  int add(int a, int b){
  int c=a+b;
  return c;
  }
  void main(){
  int a= add(3,4);
  int b= add(4,5);
  int c= add(5,6);
  printf("%d %d %d",a,b,c);
  }
  """)

  with tab2:
    st.subheader("factorial")
    st.code("""
            
         """)


    with tab3:
      st.subheader("name and lucky number")
      st.code("""
              
      """)