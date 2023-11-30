import streamlit as st
st.set_page_config(layout='wide')
st.title('c programming')
st.title("pointers")
tab1, tab2, tab3 = st.tabs(["print numbers", "sum of 2 numbers", "swapping"])
with tab1:
  st.subheader("print numbers")
  st.code("""
    #include <stdio.h> 
    int main(){
    int num=42;
    int *ptr= &num;
    printf("value of num: %d\\n", *ptr);
    *ptr = 100;
    printf("modified value of num: %d\\n",num);
    int arr[5] = {1,2,3,4,5};
    int *p = arr;
    printf("using pointer arithematic:\\n");
    for (int i=0; i<5; ++i){
        printf("element %d: %d\\n", i+1, *(p+i));
        }
    return 0;
  }
  """)


with tab2:
  st.subheader("sum of 2 numbers")
  st.code("""
    #include <stdio.h>
    int main(){
   int first, second, *p, *q, sum;
   printf("Enter two integers to add\\n");
   scanf("%d%d", &first, &second);
   p = &first;
   q = &second;
   sum = *p + *q;
   printf("Sum of the numbers = %d\\n", sum);
 }
""")



with tab3:
    st.header("swapping")
    tab4, tab5, tab6 =st.tabs(["using formula", "using pointers", "using functions"])
    with tab4:
        st.subheader("swapping of 2 numbers using formula")
        st.code("""
        #include <stdio.h>
        int main() {
        int a, b;
        printf("enter two values for a, b:  ");
        scanf("%d %d",&a,&b);
        printf("Before swapping: a = %d, b = %d\\n", a, b);
        a = a + b;
        b = a - b;
        a = a - b;
        printf("After swapping: a = %d, b = %d\\n", a, b);
       return 0;
     }
     """)


with tab5:
 st.subheader("swapping of 2 numbers using pointers")
 st.code("""
    #include <stdio.h>
    int main() {
    int num1, num2, temp;
    printf("enter the values of num1, and num2: ");
    scanf("%d %d",&num1,&num2);
    int *ptr1, *ptr2;
    ptr1 = &num1;
    ptr2 = &num2;
    temp = *ptr1;
    *ptr1 = *ptr2;
    *ptr2 = temp;
    printf("\\n after swapping num1= %d and num2=%d",num1,num2);
    return 0;
}
""")



with tab6:
  st.subheader("swapping of 2 numbers using functions")
  st.code("""
   #include <stdio.h>
   void swap(int *a, int *b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}
int main() {
  int num1, num2;
  printf("enter two numbers num1, num2 :  ");
  scanf("%d %d",&num1,&num2);
  printf("Before swapping: num1 = %d, num2 = %d\\n", num1, num2);
  swap(&num1, &num2);
  printf("After swapping: num1 = %d, num2 = %d\\n", num1, num2);
  return 0;
}
""")