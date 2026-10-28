from flask import Flask, request, render_template
import pandas as pd
import pickle
import os
import mysql.connector
from dotenv import load_dotenv

app = Flask(__name__)

# Scaler yüklə
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Model yüklə
with open("rf.pkl", "rb") as f:
    model = pickle.load(f)

# Model üçün sütunlar
columns = [
    'person_age',
    'person_income',
    'person_emp_exp',
    'loan_int_rate',
    'loan_percent_income',
    'cb_person_cred_hist_length',
    'credit_score',
    'person_gender_male',
    'person_education_Bachelor',
    'person_education_Doctorate',
    'person_education_High School',
    'person_education_Master',
    'person_home_ownership_OTHER',
    'person_home_ownership_OWN',
    'person_home_ownership_RENT',
    'loan_intent_EDUCATION',
    'loan_intent_HOMEIMPROVEMENT',
    'loan_intent_MEDICAL',
    'loan_intent_PERSONAL',
    'loan_intent_VENTURE',
    'previous_loan_defaults_on_file_Yes',
    'Bank_Access bank',
    'Bank_Azer-Turk bank',
    'Bank_Bank Respublika',
    'Bank_Kapital bank',
    'Bank_Pasha bank',
    'Bank_Unibank',
    'Bank_Xalq bank',
    'Bank_Ziraat bank'
]

# Numeric sütunlar
numeric_cols = [
    "person_age",
    "person_income",
    "person_emp_exp", 
    "loan_int_rate",
    "loan_percent_income",
    "cb_person_cred_hist_length",
    'credit_score'
]

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = ''
    error_msg = ''
    if request.method == 'POST':
        try:
            age = float(request.form['person_age'])
            income = float(request.form['person_income'])
            emp_exp = float(request.form['person_emp_exp'])
            loan_percent_income = float(request.form['loan_percent_income'])
            cred_hist_length = float(request.form['cb_person_cred_hist_length'])
            credit_score = float(request.form['credit_score'])

            gender = request.form['person_gender']
            gender_male = 1 if gender == "Male" else 0

            education = request.form['person_education']
            edu_Bachelor = 1 if education == "Bachelor" else 0
            edu_Doctorate = 1 if education == "Doctorate" else 0
            edu_HighSchool = 1 if education == "High School" else 0
            edu_Master = 1 if education == "Master" else 0
            # Reference: Associate → hamısı 0

            home = request.form['person_home_ownership']
            home_OTHER = 1 if home == "OTHER" else 0
            home_OWN = 1 if home == "OWN" else 0
            home_RENT = 1 if home == "RENT" else 0
            # Reference: MORTGAGE → hamısı 0

            intent = request.form['loan_intent']
            intent_EDUCATION = 1 if intent == "EDUCATION" else 0
            intent_HOMEIMPROVEMENT = 1 if intent == "HOMEIMPROVEMENT" else 0
            intent_MEDICAL = 1 if intent == "MEDICAL" else 0
            intent_PERSONAL = 1 if intent == "PERSONAL" else 0
            intent_VENTURE = 1 if intent == "VENTURE" else 0
            # Reference: DEBTCONSOLIDATION → hamısı 0

            prev_default = request.form['previous_loan_defaults_on_file']
            prev_yes = 1 if prev_default == "Yes" else 0

            bank = request.form['Bank']
            # Hamısı 0 ilə başlayır
            bank_Access = 0
            bank_AzerTurk = 0
            bank_BankRespublika = 0
            bank_Kapital = 0
            bank_Pasha = 0
            bank_Unibank = 0
            bank_Xalq = 0
            bank_Ziraat = 0
            loan_int_rate = 0
            # Reference: ABB bank → hamısı 0
            if bank == "Access bank":
                loan_int_rate = 4
                bank_Access = 1
            elif bank == "Azer-Turk bank":
                bank_AzerTurk = 1
                loan_int_rate =11
            elif bank == "Bank Respublika":
                bank_BankRespublika = 1
                loan_int_rate =6
            elif bank == "Kapital bank":
                bank_Kapital = 1
                loan_int_rate =10
            elif bank == "Pasha bank":
                bank_Pasha = 1
                loan_int_rate =12
            elif bank == "Unibank":
                bank_Unibank = 1
                loan_int_rate =8
            elif bank == "Xalq bank":
                bank_Xalq = 1
                loan_int_rate =1
            elif bank == "Ziraat bank":
                bank_Ziraat = 1
                loan_int_rate =2
            else:
                loan_int_rate = 20  # ABB bank üçün ortalama faiz dərəcəsi

            user_data = {
            'person_age': age,
            'person_income': income,
            'person_emp_exp': emp_exp,
            'loan_int_rate': loan_int_rate,
            'loan_percent_income': loan_percent_income,
            'cb_person_cred_hist_length': cred_hist_length,
            'credit_score':credit_score,
            'person_gender_male': gender_male,
            'person_education_Bachelor': edu_Bachelor,
            'person_education_Doctorate': edu_Doctorate,
            'person_education_High School': edu_HighSchool,
            'person_education_Master': edu_Master,
            'person_home_ownership_OTHER': home_OTHER,
            'person_home_ownership_OWN': home_OWN,
            'person_home_ownership_RENT': home_RENT,
            'loan_intent_EDUCATION': intent_EDUCATION,
            'loan_intent_HOMEIMPROVEMENT': intent_HOMEIMPROVEMENT,
            'loan_intent_MEDICAL': intent_MEDICAL,
            'loan_intent_PERSONAL': intent_PERSONAL,
            'loan_intent_VENTURE': intent_VENTURE,
            'previous_loan_defaults_on_file_Yes': prev_yes,
            'Bank_Access bank': bank_Access,
            'Bank_Azer-Turk bank': bank_AzerTurk,
            'Bank_Bank Respublika': bank_BankRespublika,
            'Bank_Kapital bank': bank_Kapital,
            'Bank_Pasha bank': bank_Pasha,
            'Bank_Unibank': bank_Unibank,
            'Bank_Xalq bank': bank_Xalq,
            'Bank_Ziraat bank': bank_Ziraat
        }

            df_user = pd.DataFrame([user_data])
            df_user = df_user[columns]
            
            df_user[numeric_cols] = scaler.transform(df_user[numeric_cols])

            y_pred = model.predict(df_user)
            prediction = f"Prediction: {y_pred[0]:.2f}"

            try:
                load_dotenv()
                
                conn = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME")
                )
                cursor = conn.cursor()

                cursor.execute("""
                CREATE TABLE IF NOT EXISTS loan_predictions (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    person_age INT,
                    person_income FLOAT,  
                    employment_experience_years INT,   
                    loan_percent_income FLOAT, 
                    credit_history_length INT,
                    credit_score INT,                         
                    person_gender VARCHAR(20),
                    person_education VARCHAR(50),
                    person_home_ownership VARCHAR(50),
                    loan_intent VARCHAR(50),
                    previous_loan_defaults_on_file VARCHAR(10),
                    Bank VARCHAR(50),
                    predicted_loan_amount FLOAT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """)

                gender_val = gender  # Male/Female
                # Education
                if edu_Bachelor: education_val = "Bachelor"
                elif edu_Doctorate: education_val = "Doctorate"
                elif edu_HighSchool: education_val = "High School"
                elif edu_Master: education_val = "Master"
                else: education_val = "Associate"
                # Home ownership
                if home_OTHER: home_val = "OTHER"
                elif home_OWN: home_val = "OWN"
                elif home_RENT: home_val = "RENT"
                else: home_val = "MORTGAGE"
                # Loan intent
                if intent_EDUCATION: intent_val = "EDUCATION"
                elif intent_HOMEIMPROVEMENT: intent_val = "HOMEIMPROVEMENT"
                elif intent_MEDICAL: intent_val = "MEDICAL"
                elif intent_PERSONAL: intent_val = "PERSONAL"
                elif intent_VENTURE: intent_val = "VENTURE"
                else: intent_val = "DEBTCONSOLIDATION"
                # Previous loan defaults
                prev_val = "Yes" if prev_yes else "No"

                # 4️⃣ Insert
                sql = """
                INSERT INTO loan_predictions (
                    person_age,
                    person_income,
                    employment_experience_years,
                    loan_percent_income, 
                    credit_history_length,
                    credit_score,
                    person_gender,
                    person_education,
                    person_home_ownership,
                    loan_intent,
                    previous_loan_defaults_on_file,
                    Bank,
                    predicted_loan_amount
                ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """
                values = (
                    age, income, emp_exp, loan_percent_income, cred_hist_length,credit_score,
                    gender_val, education_val,
                    home_val, intent_val,
                    prev_val, bank, float(y_pred[0])
                )

                cursor.execute(sql, values)
                conn.commit()
                cursor.close()
                conn.close()

            except Exception as e_mysql:
                print("MySQL save error:", e_mysql)

        except Exception as e:
            error_msg = str(e)

    return render_template('project2.html', prediction=prediction, error_msg=error_msg)


if __name__ == '__main__':
    app.run(debug=True)
