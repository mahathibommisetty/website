import streamlit as st
st.set_page_config(layout='wide')
st.title('c programming')
st.header("recursion")
st.subheader("factorial")
st.code("""
#include<stdio.h>
int factorial(int n) {
    if (n == 0) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}
int main() {
    int num;
    printf("Enter a non-negative integer: ");
    scanf("%d", &num);
    if (num < 0) {
        printf("Please enter a non-negative integer.\n");
    } else {
        printf("Factorial of %d = %d\n", num, factorial(num));
    }
    return 0;
}
""")