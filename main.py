import streamlit as st
st.set_page_config(layout='wide')
st.title('c programming')
st.subheader('factorial')
st.code("""
#include <stdio.h>
int factorial(int n) {
    if (n == 0) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}
int main() {
    int number;
    printf("Enter a number: ");
    scanf("%d", &number);
    int result = factorial(number);
    printf("The factorial of %d is %d\n", number, result);
    return 0;
}
""")