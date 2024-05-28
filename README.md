# Loan Eligibility Checker

This Streamlit application allows users to check their eligibility for a loan based on various personal, financial, and asset-related details. The application also provides a visual representation of feature importance using LIME (Local Interpretable Model-agnostic Explanations).

## Features

- **Personal Information Input**: Users can enter their personal details such as name, contact information, and educational background.
- **Proof Upload**: Users can upload documents for address proof, education proof, PAN card proof, and employment proof.
- **Loan Information Input**: Users can enter the desired loan amount, CIBIL score, number of dependents, and loan term.
- **Assets Information Input**: Users can input values of their bank assets, luxury assets, residential property, and commercial property.
- **Eligibility Check**: The application predicts loan eligibility based on the input data using a pre-trained machine learning model.
- **Feature Importance Visualization**: The application uses LIME to explain the model's prediction and displays the feature importance in a bar chart with positive impacts shown in green and negative impacts shown in red.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/your-repo/loan-eligibility-checker.git
    cd loan-eligibility-checker
    ```

2. **Install the required dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Ensure you have the pre-trained model (`loan_model.pkl`) and training data (`X_Train1.csv`) in the root directory**.

## Usage

1. **Run the Streamlit app**:
    ```sh
    streamlit run app.py
    ```

2. **Open your web browser** and go to `http://localhost:8501` to access the application.

3. **Fill in the required details** in the personal information, proof, loan information, and assets information sections.

4. **Click the 'Check Eligibility' button** to get the prediction result and view the feature importance bar chart.

## File Structure

- `app.py`: Main application file containing the Streamlit code.
- `loan_model.pkl`: Pre-trained machine learning model for loan eligibility prediction.
- `X_Train1.csv`: Training data used for LIME explanations.
- `requirements.txt`: List of Python dependencies required to run the application.

## Dependencies

- streamlit
- numpy
- joblib
- interpret
- pandas
- matplotlib

## Example


## Team

**Team Name**: Fabino

**Team Members**:
- Sumresh Nuresh
- Yogesh SJ
- Abhilash R

## Acknowledgments

- The `interpret` library for providing LIME explanations.
- The Streamlit team for making it easy to build web applications for machine learning.
