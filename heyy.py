import streamlit as st
import numpy as np
import joblib 
from interpret.blackbox import LimeTabular
from googletrans import Translator

model = joblib.load(open("./loan_model.pkl","rb"))

def check_eligibility(data):
    prediction = model.predict(data)[0]
    return prediction

# Function to translate text
def translate_text(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

# Define labels for fields
field_labels = {
    'First Name': {'en': 'First Name', 'fr': 'Prénom', 'es': 'Nombre de pila'},
    'Last Name': {'en': 'Last Name', 'fr': 'Nom de famille', 'es': 'Apellido'},
    'Contact Number': {'en': 'Contact Number', 'fr': 'Numéro de contact', 'es': 'Número de contacto'},
    'Father Name': {'en': 'Father Name', 'fr': 'Nom du père', 'es': 'Nombre del padre'},
    'Mother Name': {'en': 'Mother Name', 'fr': 'Nom de la mère', 'es': 'Nombre de la madre'},
    'Sibling Name': {'en': 'Sibling Name', 'fr': 'Nom du frère/soeur', 'es': 'Nombre del hermano/hermana'},
    'Aadhar card Number': {'en': 'Aadhar card Number', 'fr': 'Numéro de carte Aadhar', 'es': 'Número de tarjeta Aadhar'},
    'Education': {'en': 'Education', 'fr': 'Éducation', 'es': 'Educación'},
    'Annual Income (INR)': {'en': 'Annual Income (INR)', 'fr': 'Revenu annuel (INR)', 'es': 'Ingresos anuales (INR)'},
    'E-mail ID': {'en': 'E-mail ID', 'fr': 'Identifiant e-mail', 'es': 'ID de correo electrónico'},
    'Father Contact Number': {'en': 'Father Contact Number', 'fr': 'Numéro de contact du père', 'es': 'Número de contacto del padre'},
    'Mother Contact Number': {'en': 'Mother Contact Number', 'fr': 'Numéro de contact de la mère', 'es': 'Número de contacto de la madre'},
    'Sibling Contact Number': {'en': 'Sibling Contact Number', 'fr': 'Numéro de contact du frère/soeur', 'es': 'Número de contacto del hermano/hermana'},
    'Pan card Number': {'en': 'Pan card Number', 'fr': 'Numéro de carte Pan', 'es': 'Número de tarjeta Pan'},
    'Employment Status': {'en': 'Employment Status', 'fr': 'Statut d\'emploi', 'es': 'Estado laboral'},
    'Address Card Proof': {'en': 'Address Card Proof', 'fr': 'Preuve de carte d\'adresse', 'es': 'Prueba de tarjeta de dirección'},
    'Education Proof': {'en': 'Education Proof', 'fr': 'Preuve d\'éducation', 'es': 'Prueba de educación'},
    'Pan Card Proof': {'en': 'Pan Card Proof', 'fr': 'Preuve de la carte Pan', 'es': 'Prueba de la tarjeta Pan'},
    'Employement Proof': {'en': 'Employement Proof', 'fr': 'Preuve d\'emploi', 'es': 'Prueba de empleo'},
    'Loan Amount': {'en': 'Loan Amount', 'fr': 'Montant du prêt', 'es': 'Cantidad del préstamo'},
    'CIBIL Score': {'en': 'CIBIL Score', 'fr': 'Score CIBIL', 'es': 'Puntuación CIBIL'},
    'Number of Dependents': {'en': 'Number of Dependents', 'fr': 'Nombre de personnes à charge', 'es': 'Número de dependientes'},
    'Loan Term (Months)': {'en': 'Loan Term (Months)', 'fr': 'Durée du prêt (mois)', 'es': 'Plazo del préstamo (meses)'},
    'Bank Asset Value (INR)': {'en': 'Bank Asset Value (INR)', 'fr': 'Valeur de l\'actif bancaire (INR)', 'es': 'Valor del activo bancario (INR)'},
    'Luxury Asset Value (INR)': {'en': 'Luxury Asset Value (INR)', 'fr': 'Valeur de l\'actif de luxe (INR)', 'es': 'Valor del activo de lujo (INR)'},
    'Residential Property Value (INR)': {'en': 'Residential Property Value (INR)', 'fr': 'Valeur de la propriété résidentielle (INR)', 'es': 'Valor de la propiedad residencial (INR)'},
    'Commercial Property Value (INR)': {'en': 'Commercial Property Value (INR)', 'fr': 'Valeur de la propriété commerciale (INR)', 'es': 'Valor de la propiedad comercial (INR)'},
    'Check Eligibility': {'en': 'Check Eligibility', 'fr': 'Vérifier l\'éligibilité', 'es': 'Comprobar elegibilidad'},
    'Congratulations! You are eligible for the loan.': {'en': 'Congratulations! You are eligible for the loan.', 'fr': 'Félicitations! Vous êtes éligible pour le prêt.', 'es': '¡Felicidades! Eres elegible para el préstamo.'},
    'Sorry, you are not eligible for the loan.': {'en': 'Sorry, you are not eligible for the loan.', 'fr': 'Désolé, vous n\'êtes pas éligible pour le prêt.', 'es': 'Lo siento, no eres elegible para el préstamo.'},
}

def main():
    # Dropdown for language selection
    target_language = st.sidebar.selectbox('Select Target Language', ['en', 'French', 'Spanish'])

    st.title('Loan Eligibility Checker')
    st.write('Enter your details below to check your eligibility for a loan.')

    st.header('Personal Information')
    col1, col2 = st.columns(2)
    with col1:
        fname = st.text_input(translate_text(field_labels['First Name'][target_language], target_language))
        contactno = st.text_input(translate_text(field_labels['Contact Number'][target_language], target_language))
        fathername = st.text_input(translate_text(field_labels['Father Name'][target_language], target_language))
        mothername = st.text_input(translate_text(field_labels['Mother Name'][target_language], target_language))
        sathername = st.text_input(translate_text(field_labels['Sibling Name'][target_language], target_language))
        aadharc = st.text_input(translate_text(field_labels['Aadhar card Number'][target_language], target_language))             
        education = st.selectbox(translate_text(field_labels['Education'][target_language], target_language), ['No formal education', 'Primary education', 'High School', 'Bachelor\'s degree', 'Master\'s degree', 'Doctorate'], help=translate_text(field_labels['Select your highest level of education.'][target_language], target_language))
        annual_income = st.number_input(translate_text(field_labels['Annual Income (INR)'][target_language], target_language), min_value=0, step=1000, help=translate_text(field_labels['Enter your annual income in INR.'][target_language], target_language))
        
    with col2:
        lname = st.text_input(translate_text(field_labels['Last Name'][target_language], target_language))        
        emailid = st.text_input(translate_text(field_labels['E-mail ID'][target_language], target_language))        
        fcontactno = st.text_input(translate_text(field_labels['Father Contact Number'][target_language], target_language))
        mcontactno = st.text_input(translate_text(field_labels['Mother Contact Number'][target_language], target_language))
        scontactno = st.text_input(translate_text(field_labels['Sibling Contact Number'][target_language], target_language))
        panc = st.text_input(translate_text(field_labels['Pan card Number'][target_language], target_language))
        employment = st.selectbox(translate_text(field_labels['Employment Status'][target_language], target_language), ['Employed', 'Unemployed'], help=translate_text(field_labels['Select your employment status.'][target_language], target_language))        
        
    st.header('Proof')
    col3, col4 = st.columns(2)
    with col3:
        paadharc = st.file_uploader(label=translate_text(field_labels['Address Card Proof'][target_language], target_language), help=translate_text(field_labels['Front-side and Back-side of Your Aadhar Card'][target_language], target_language))        
        peduc = st.file_uploader(label=translate_text(field_labels['Education Proof'][target_language], target_language), help=translate_text(field_labels['Marksheet of Your Highest Qualification'][target_language], target_language))
    with col4:
        ppanc = st.file_uploader(label=translate_text(field_labels['Pan Card Proof'][target_language], target_language), help=translate_text(field_labels['Front-side of Your Pan Card'][target_language], target_language))
        pempc = st.file_uploader(label=translate_text(field_labels['Employement Proof'][target_language], target_language), help=translate_text(field_labels['Employement Proof'][target_language], target_language))
    
    st.header('Loan Information')
    col1, col2 = st.columns(2)
    with col1:
        loan_amount = st.number_input(translate_text(field_labels['Loan Amount'][target_language], target_language), min_value=0, step=1000)        
        cibil_score = st.number_input(translate_text(field_labels['CIBIL Score'][target_language], target_language), min_value=0, max_value=1000, step=1, help=translate_text(field_labels['Enter your CIBIL score.'][target_language], target_language))
    with col2:
        num_dependents = st.number_input(translate_text(field_labels['Number of Dependents'][target_language], target_language), min_value=0, max_value=10, step=1)
        loan_term = st.number_input(translate_text(field_labels['Loan Term (Months)'][target_language], target_language), min_value=0, step=1, help=translate_text(field_labels['Enter the loan term in months.'][target_language], target_language))
        

    st.header('Assets Information')
    col3, col4 = st.columns(2)
    with col3:
        bank_asset = st.number_input(translate_text(field_labels['Bank Asset Value (INR)'][target_language], target_language), min_value=0, step=1000, help=translate_text(field_labels['Enter the value of bank assets in INR.'][target_language], target_language))
        lux_asset = st.number_input(translate_text(field_labels['Luxury Asset Value (INR)'][target_language], target_language), min_value=0, step=1000, help=translate_text(field_labels['Enter the value of luxury assets in INR.'][target_language], target_language))
    with col4:
        residential = st.number_input(translate_text(field_labels['Residential Property Value (INR)'][target_language], target_language), min_value=0, step=1000, help=translate_text(field_labels['Enter the value of residential property in INR.'][target_language], target_language))
        commercial = st.number_input(translate_text(field_labels['Commercial Property Value (INR)'][target_language], target_language), min_value=0, step=1000, help=translate_text(field_labels['Enter the value of commercial property in INR.'][target_language], target_language))
      
    input_data = np.array([[num_dependents, 0 if education == 'No formal education' else 1, 1 if employment == 'Employed' else 0, annual_income, loan_amount, loan_term, cibil_score, bank_asset+lux_asset, residential+commercial]])

    if st.button(translate_text(field_labels['Check Eligibility'][target_language], target_language)):
        result = check_eligibility(input_data)
        if result == 0:
            st.success(translate_text(field_labels['Congratulations! You are eligible for the loan.'][target_language], target_language))
            st.balloons()
        else:
            st.error(translate_text(field_labels['Sorry, you are not eligible for the loan.'][target_language], target_language))

if __name__ == '__main__':
    main()

