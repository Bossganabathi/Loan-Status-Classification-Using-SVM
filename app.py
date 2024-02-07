import pickle
import streamlit as st

loan = pickle.load(open('model.pkl', 'rb'))

# page title
st.title("Loan Status Prediction Machine Learning")



Gender	= st.text_input('Gender')
Married	= st.text_input('Married')
Dependents = st.text_input('Dependents')
Education = st.text_input('Education')
Self_Employed = st.text_input('Self_Employed')
ApplicantIncome	= st.text_input('Applicant Income')
CoapplicantIncome = st.text_input('Co-applicant-Income')
LoanAmount = st.text_input('LoanAmount')
Loan_Amount_Term = st.text_input('Loan_Amount_Term')
Credit_History	= st.text_input('Credit_History')
Property_Area = st.text_input('Property_Area Rural:0, Semiurban:1, Urban:2')


#code for Prediction
loan_status =''


#creating a button for prediction
if st.button("Loan Prediction Result"):
    loan_prediction = loan.predict([[Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]])

    if (loan_prediction[0]==1):
        loan_status = 'Eligible'
    
    else:
        loan_status = 'not eligible'

st.success(loan_status)