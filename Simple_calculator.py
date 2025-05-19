
import streamlit as st



def calculator(n1,n2,opr):

    if opr=='+':
        return n1+n2
    elif opr=='-':
        return n1-n2
    elif opr=='*':
        return n1*n2
    else:
        if n2!=0:
         return n1/n2
        else:
            return"devision by zero is not allowed"

def main():

    st.title("welcome to my calculator..... ")
    number1=st.number_input('Enter number1 ....',format='%2f')
    opreator=st.selectbox("selcet opreator",['+','-','*','/'])
    number2=st.number_input("enter number2 ....",format='%2f')

    result=calculator(number1,number2,opreator)
    if st.button("calculate"):
        st.success(result)

if __name__=="__main__":
    main()
