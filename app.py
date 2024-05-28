# import streamlit as st
# import numpy as np
# import joblib 
# from interpret.blackbox import LimeTabular
# import pandas as pd

# model = joblib.load(open("./loan_model.pkl","rb"))
# X_train=pd.read_csv('./X_Train1.csv')
# def check_eligibility(data):
#     prediction = model.predict(data)[0]
#     lime = LimeTabular(model=model.predict_proba, data=X_train.values, random_state=1)
    
#     # Get local explanations for the user-input data point
#     lime_local = lime.explain_local(data, name='LIME')
#     data3 = lime_local.data(key=0)
#     # dataofname1=data3["names"]
#     dataofname=data3["scores"]
#     # Show local explanations
#     # st.write(dataofname1)
#     # dum=["num_dependents",  "education" ,"employment" , "annual_income", "loan_amount", "loan_term", "cibil_score", "movable", "immovable"]
#     dum=[' cibil_score',
#   ' loan_term',
#   'Immovable_assets',
#   ' income_annum',
#   'Movable_assets',
#   ' loan_amount',
#   ' self_employed',
#   ' no_of_dependents',
#   ' education']
#     for idx, i in enumerate(dum):
#         st.write(i)
#         st.write(dataofname[idx])
    
#     # Iterate over the explanations and display them
#     # for explanation in lime_local.data:
#     #     st.write(explanation)
#     return prediction



# def main():
#     st.title('Loan Eligibility Checker')
#     st.write('Enter your details below to check your eligibility for a loan.')

#     st.header('Personal Information')
#     col1, col2 = st.columns(2)
#     with col1:
#         fname = st.text_input('First Name')
#         contactno = st.text_input('Contact Number')
#         fathername = st.text_input('Father Name')
#         mothername = st.text_input('Mother Name')
#         sathername = st.text_input('Sibling Name')
#         aadharc = st.text_input('Aadhar card Number')             
#         education = st.selectbox('Education', ['No formal education', 'Primary education', 'High School', 'Bachelor\'s degree', 'Master\'s degree', 'Doctorate'], help="Select your highest level of education.")
#         annual_income = st.number_input('Annual Income (INR)', min_value=0, step=1000, help="Enter your annual income in INR.")
        
#     with col2:
#         lname = st.text_input('Last Name')        
#         emailid = st.text_input('E-mail ID')        
#         fcontactno = st.text_input('Father Contact Number')
#         mcontactno = st.text_input('Mother Contact Number')
#         scontactno = st.text_input('Sibling Contact Number')
#         panc = st.text_input('Pan card Number')
#         employment = st.selectbox('Employment Status', ['Employed', 'Unemployed'], help="Select your employment status.")        
        
#     st.header('Proof')
#     col3, col4 = st.columns(2)
#     with col3:
#         paadharc = st.file_uploader(label='Address Card Proof', help="Front-side and Back-side of Your Aadhar Card")        
#         peduc = st.file_uploader(label='Education Proof', help="Marksheet of Your Highest Qualification")
#     with col4:
#         ppanc = st.file_uploader(label='Pan Card Proof', help="Front-side of Your Pan Card")
#         pempc = st.file_uploader(label='Employement Proof', help="Employement Proof")
    
#     st.header('Loan Information')
#     col1, col2 = st.columns(2)
#     with col1:
#         loan_amount = st.number_input('Loan Amount', min_value=0, step=1000)        
#         cibil_score = st.number_input('CIBIL Score', min_value=0, max_value=1000, step=1, help="Enter your CIBIL score.")
#     with col2:
#         num_dependents = st.number_input('Number of Dependents', min_value=0, max_value=10, step=1)
#         loan_term = st.number_input('Loan Term (Months)', min_value=0, step=1, help="Enter the loan term in months.")
        

#     st.header('Assets Information')
#     col3, col4 = st.columns(2)
#     with col3:
#         bank_asset = st.number_input('Bank Asset Value (INR)', min_value=0, step=1000, help="Enter the value of bank assets in INR.")
#         lux_asset = st.number_input('Luxury Asset Value (INR)', min_value=0, step=1000, help="Enter the value of luxury assets in INR.")
#     with col4:
#         residential = st.number_input('Residential Property Value (INR)', min_value=0, step=1000, help="Enter the value of residential property in INR.")
#         commercial = st.number_input('Commercial Property Value (INR)', min_value=0, step=1000, help="Enter the value of commercial property in INR.")
      
#     input_data = np.array([[num_dependents, 0 if education == 'No formal education' else 1, 1 if employment == 'Employed' else 0, annual_income, loan_amount, loan_term, cibil_score, bank_asset+lux_asset, residential+commercial]])

#     if st.button('Check Eligibility'):
#         result = check_eligibility(input_data)
#         if result == 0:
#             st.success('Congratulations! You are eligible for the loan.')
#             st.balloons()
#         else:
#             st.error('Sorry, you are not eligible for the loan.')

# if __name__ == '__main__':
#     main()


# import streamlit as st
# import numpy as np
# import joblib
# from interpret.blackbox import LimeTabular
# import pandas as pd
# import matplotlib.pyplot as plt

# # Load the model and training data
# model = joblib.load(open("./loan_model.pkl", "rb"))
# X_train = pd.read_csv('./X_Train1.csv')

# # Function to check eligibility and display explanations
# def check_eligibility(data):
#     prediction = model.predict(data)[0]
#     lime = LimeTabular(model=model.predict_proba, data=X_train.values, random_state=1)
    
#     # Get local explanations for the user-input data point
#     lime_local = lime.explain_local(data, name='LIME')
#     data3 = lime_local.data(key=0)
#     dataofname = data3["scores"]
    
#     # Feature names
#     dum = ['cibil_score', 'loan_term', 'Immovable_assets', 'income_annum', 
#            'Movable_assets', 'loan_amount', 'self_employed', 'no_of_dependents', 'education']
    
#     # Create a bar graph
#     fig, ax = plt.subplots()
#     ax.barh(dum, dataofname, color='skyblue')
#     ax.set_xlabel('Importance Score')
#     ax.set_title('Feature Importance for Loan Eligibility')
    
#     # Display the bar graph in Streamlit
#     st.pyplot(fig)
    
#     return prediction

# # Main function to run the Streamlit app
# def main():
#     st.title('Loan Eligibility Checker')
#     st.write('Enter your details below to check your eligibility for a loan.')

#     st.header('Personal Information')
#     col1, col2 = st.columns(2)
#     with col1:
#         fname = st.text_input('First Name')
#         contactno = st.text_input('Contact Number')
#         fathername = st.text_input('Father Name')
#         mothername = st.text_input('Mother Name')
#         sathername = st.text_input('Sibling Name')
#         aadharc = st.text_input('Aadhar card Number')
#         education = st.selectbox('Education', ['No formal education', 'Primary education', 'High School', "Bachelor's degree", "Master's degree", 'Doctorate'], help="Select your highest level of education.")
#         annual_income = st.number_input('Annual Income (INR)', min_value=0, step=1000, help="Enter your annual income in INR.")
        
#     with col2:
#         lname = st.text_input('Last Name')
#         emailid = st.text_input('E-mail ID')
#         fcontactno = st.text_input('Father Contact Number')
#         mcontactno = st.text_input('Mother Contact Number')
#         scontactno = st.text_input('Sibling Contact Number')
#         panc = st.text_input('Pan card Number')
#         employment = st.selectbox('Employment Status', ['Employed', 'Unemployed'], help="Select your employment status.")        
        
#     st.header('Proof')
#     col3, col4 = st.columns(2)
#     with col3:
#         paadharc = st.file_uploader(label='Address Card Proof', help="Front-side and Back-side of Your Aadhar Card")
#         peduc = st.file_uploader(label='Education Proof', help="Marksheet of Your Highest Qualification")
#     with col4:
#         ppanc = st.file_uploader(label='Pan Card Proof', help="Front-side of Your Pan Card")
#         pempc = st.file_uploader(label='Employement Proof', help="Employement Proof")
    
#     st.header('Loan Information')
#     col1, col2 = st.columns(2)
#     with col1:
#         loan_amount = st.number_input('Loan Amount', min_value=0, step=1000)
#         cibil_score = st.number_input('CIBIL Score', min_value=0, max_value=1000, step=1, help="Enter your CIBIL score.")
#     with col2:
#         num_dependents = st.number_input('Number of Dependents', min_value=0, max_value=10, step=1)
#         loan_term = st.number_input('Loan Term (Months)', min_value=0, step=1, help="Enter the loan term in months.")
        
#     st.header('Assets Information')
#     col3, col4 = st.columns(2)
#     with col3:
#         bank_asset = st.number_input('Bank Asset Value (INR)', min_value=0, step=1000, help="Enter the value of bank assets in INR.")
#         lux_asset = st.number_input('Luxury Asset Value (INR)', min_value=0, step=1000, help="Enter the value of luxury assets in INR.")
#     with col4:
#         residential = st.number_input('Residential Property Value (INR)', min_value=0, step=1000, help="Enter the value of residential property in INR.")
#         commercial = st.number_input('Commercial Property Value (INR)', min_value=0, step=1000, help="Enter the value of commercial property in INR.")
      
#     input_data = np.array([[num_dependents, 0 if education == 'No formal education' else 1, 1 if employment == 'Employed' else 0, annual_income, loan_amount, loan_term, cibil_score, bank_asset + lux_asset, residential + commercial]])

#     if st.button('Check Eligibility'):
#         result = check_eligibility(input_data)
#         if result == 0:
#             st.success('Congratulations! You are eligible for the loan.')
#             st.balloons()
#         else:
#             st.error('Sorry, you are not eligible for the loan.')

# if __name__ == '__main__':
#     main()













import streamlit as st
import numpy as np
import joblib
from interpret.blackbox import LimeTabular
import pandas as pd
import matplotlib.pyplot as plt

# Load the model and training data
model = joblib.load(open("./loan_model.pkl", "rb"))
X_train = pd.read_csv('./X_Train1.csv')

# Function to check eligibility and display explanations
def check_eligibility(data):
    prediction = model.predict(data)[0]
    lime = LimeTabular(model=model.predict_proba, data=X_train.values, random_state=1)
    
    # Get local explanations for the user-input data point
    lime_local = lime.explain_local(data, name='LIME')
    data3 = lime_local.data(key=0)
    dataofname = data3["scores"]
    
    # Feature names
    dum = ['cibil_score', 'loan_term', 'Immovable_assets', 'income_annum', 
           'Movable_assets', 'loan_amount', 'self_employed', 'no_of_dependents', 'education']
    
    # Create a bar graph with colors based on the sign of the scores
    colors = ['green' if score > 0 else 'red' for score in dataofname]
    fig, ax = plt.subplots()
    ax.barh(dum, dataofname, color=colors)
    ax.set_xlabel('Importance Score')
    ax.set_title('Feature Importance for Loan Eligibility')
    
    # Display the bar graph in Streamlit
    st.pyplot(fig)
    
    return prediction

# Main function to run the Streamlit app
def main():
    st.title('Loan Eligibility Checker')
    st.write('Enter your details below to check your eligibility for a loan.')

    st.header('Personal Information')
    col1, col2 = st.columns(2)
    with col1:
        fname = st.text_input('First Name')
        contactno = st.text_input('Contact Number')
        fathername = st.text_input('Father Name')
        mothername = st.text_input('Mother Name')
        sathername = st.text_input('Sibling Name')
        aadharc = st.text_input('Aadhar card Number')
        education = st.selectbox('Education', ['No formal education', 'Primary education', 'High School', "Bachelor's degree", "Master's degree", 'Doctorate'], help="Select your highest level of education.")
        annual_income = st.number_input('Annual Income (INR)', min_value=0, step=1000, help="Enter your annual income in INR.")
        
    with col2:
        lname = st.text_input('Last Name')
        emailid = st.text_input('E-mail ID')
        fcontactno = st.text_input('Father Contact Number')
        mcontactno = st.text_input('Mother Contact Number')
        scontactno = st.text_input('Sibling Contact Number')
        panc = st.text_input('Pan card Number')
        employment = st.selectbox('Employment Status', ['Employed', 'Unemployed'], help="Select your employment status.")        
        
    st.header('Proof')
    col3, col4 = st.columns(2)
    with col3:
        paadharc = st.file_uploader(label='Address Card Proof', help="Front-side and Back-side of Your Aadhar Card")
        peduc = st.file_uploader(label='Education Proof', help="Marksheet of Your Highest Qualification")
    with col4:
        ppanc = st.file_uploader(label='Pan Card Proof', help="Front-side of Your Pan Card")
        pempc = st.file_uploader(label='Employement Proof', help="Employement Proof")
    
    st.header('Loan Information')
    col1, col2 = st.columns(2)
    with col1:
        loan_amount = st.number_input('Loan Amount', min_value=0, step=1000)
        cibil_score = st.number_input('CIBIL Score', min_value=0, max_value=1000, step=1, help="Enter your CIBIL score.")
    with col2:
        num_dependents = st.number_input('Number of Dependents', min_value=0, max_value=10, step=1)
        loan_term = st.number_input('Loan Term (Months)', min_value=0, step=1, help="Enter the loan term in months.")
        
    st.header('Assets Information')
    col3, col4 = st.columns(2)
    with col3:
        bank_asset = st.number_input('Bank Asset Value (INR)', min_value=0, step=1000, help="Enter the value of bank assets in INR.")
        lux_asset = st.number_input('Luxury Asset Value (INR)', min_value=0, step=1000, help="Enter the value of luxury assets in INR.")
    with col4:
        residential = st.number_input('Residential Property Value (INR)', min_value=0, step=1000, help="Enter the value of residential property in INR.")
        commercial = st.number_input('Commercial Property Value (INR)', min_value=0, step=1000, help="Enter the value of commercial property in INR.")
      
    input_data = np.array([[num_dependents, 0 if education == 'No formal education' else 1, 1 if employment == 'Employed' else 0, annual_income, loan_amount, loan_term, cibil_score, bank_asset + lux_asset, residential + commercial]])

    if st.button('Check Eligibility'):
        result = check_eligibility(input_data)
        if result == 0:
            st.success('Congratulations! You are eligible for the loan.')
            st.balloons()
        else:
            st.error('Sorry, you are not eligible for the loan.')

if __name__ == '__main__':
    main()
