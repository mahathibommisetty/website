import streamlit as st
st.set_page_config(layout='wide')
st.title("c programming")
st.header("control statements")
tab1, tab2, tab3, tab4, tab5 = st.tabs(["if-else statement", "for-loop statement", "while-loop statement", "do-while", "switch statement"])

with tab1:
    st.header(" if-else statement")
    st.subheader("roller coaster")
    st.code("""
    #include<stdio.h>
     int main(){ 
     int age,height;
     printf("enter your age and height: ");
        scanf("%d %d",&age, &height);
        if(age>18 && height>=150){
          print("eligible");
        }else{
          printf("not eligible");
        }
        }
    """)


with tab3:
    st.subheader(" while statement")
    st.code("""
    #include<stdio.h>
    int main(){
        int num=1,stop;
            while(1){
            printf("enter the key:");
            scanf("%d",&stop);
            if(stop==5){
            break;
      }
     }
    }
""")

with tab4:
    st.subheader("do-while")
    st.code("""
    #include<stdio.h>
    int main(){
    int numbers=10;
    while(number<10){
    print("hi");
    break;
    }
    do{
    print("hi");
    break;
    }
    while(number<10);
    }
""")

with tab5:
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
    printf("choose the operator from(+,-,*,/): ");
    scanf(" %c",&operator);
    switch(operator){
    case'+':
    printf("addition is %d",(num2+num1));
    break;
    case'-':
    printf("subtraction is %d",(num2-num));
    break;
    case'*':
    printf("multiplication is %d",(num2*num1));
    break;
    case'/':
    printf("division is %d",(num2/num1));
    break;
    default:
    printf("not exist");
}
}
""")


with tab2:
    st.header(" for-loop statement")
    tab6, tab7, tab8, tab9 =(["tree 1", "tree 2", "tree 3", "length of array"])
    with tab6:
       st.subheader("tree 1")
       st.code("""
          #include<stdio.h>
          int main(){
          for(int i=0; i<3;i++){
          for(int j=0;j<=i;j++){
          printf("*");
          }
          printf("\\n");
          }
        }
    """)


    with tab7:
        st.subheader("tree 2")
        st.code("""
        #include<stdio.h>
        int main(){
        for(int j=0; j<3;j++){
        for(int i=0;i<=j;i++){
        printf("*");
        }
        printf("\\n");
        }
        }
    """)


    with tab8:
        st.subheader(" tree 3")
        st.code("""
        #include<stdio.h>
        int main(){
        for(int i=5; i>0;i--){
        for(int j=i;j>0;j--){
        printf("*");
        }
        printf("\\n");
        }
        }
    """)

    with tab9:
       st.subheader("length of array")
       st.code("""
       #include<studio.h>
       int main(){
             int len;
             Printf("enter the len of array:");
            scanf("%d",len);
            int arr[len];
       for(int i=0;i<len;i++){
        printf("enter the value for arr[%d]:i);
       scanf("%d",&arr[i]);
       }
       """)