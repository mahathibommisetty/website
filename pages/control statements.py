import streamlit as st
st.set_page_config(layout='wide')
st.title("c programming")
st.header("control statements")
st.subheader("switch statement")
st.code("""
#include<stdio.h>
int main(){
    int num1,num2;
    char operator;
    printf("enter a number1");
    scanf("%d",&num1);
    printf("enter number2");
    scanf("%d",&num2);

    switch(operator){
    case'+':printf("addition is %d",(num2+num1));
break;
case'-':printf("subtraction is %d",(num2-num));
break;
case'*':printf("multiplication is %d",(num2*num1));
break;
case'/':printf("division is %d",(num2/num1));
break;
default:printf("not exist");
}
}
""")