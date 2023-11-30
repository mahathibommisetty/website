import streamlit as st
st.set_page_config(layout='wide')
st.title("c programming")
st.header("control statements")
tab1, tab2, tab3, tab4, tab5 = st.tabs(["if statement", "if-else statement", "for-loop statement", "while-loop statement", "switch statement"])
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


with tab4:
    st.subheader(" while statement")
    st.code("""
    #include<stdio.h>
    int main(){
        int num=1,stop;
            while(1){
            printf("enter the key:");
            scanf("%d",&stop);
            if(stop==0){
            break;
      }
     }
    }
         """)


with tab2:
    st.subheader(" if-else statement")
    st.code("""
    #include<stdio.h>
     int main(){ 
     int age,height;
     printf("enter your age and height");
        scanf("%d",&age,&height);
        if(age>18 && height>=150){
          print("eligible");
        }else{
          printf("not eligible");
        }
        }
    """)


with tab3:
    st.header(" for-loop statement")
    tab6, tab7, tab8 =(["tree 1", "tree 2", "tree 3"])
    with tab6:
      st.subheader("tree 1")
      st.code("""
      #include<stdio.h>
      int main()
      for(int i=0; i<3;i++){
      for(int j=0;j<=i;j++){
      printf("*");
      }
      printf("/n")
      }
    }
    """)


    with tab7:
        st.subheader("tree 2")
        st.code("""
        #include<stdio.h>
        int main()
        for(int j=0; j<3;j++){
        for(int i=0;i<=j;i++){
        printf("*");
        }
        printf("/n")
        }
        }
    """)


    with tab8:
        st.subheader(" tree 3")
        st.code("""
        #include<stdio.h>
        int main()
        for(int i=5; i>0;i--){
        for(int j=i;j>0;j--){
        printf("*");
        }
        printf("/n")
        }
        }
    """)
