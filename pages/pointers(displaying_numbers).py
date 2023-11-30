import streamlit as st
st.set_page_config(layout='wide')
st.title('c programming')
st.subheader("pointers to print numbers")
st.code("""

#include <stdio.h>
int main(){
    int num=42;
    int *ptr= &num;
    printf("value of num: %d\n", *ptr);
    *ptr = 100;
    printf("modified value of num: %d\n",num);
    int arr[5] = {1,2,3,4,5};
    int *p = arr;
    printf("using pointer arithematic:\n");
    for (int i=0; i<5; ++i){
        printf("element %d: %d\n", i+1, *(p+i));
        }
return 0;

}

 """)




st.subheader("pointers to print numbers")
st.code("""
#include <stdio.h>
int main(){
int arr[5] = {1,2,3,4,5};
    int *p = arr;
    printf("using pointer arithematic:\n");
    for (int i=0; i<5; ++i){
        printf("element %d: %d\n", i+1, *(p+i));
        }
return 0;

}

""")