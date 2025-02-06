from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector
import joblib
import numpy as np
from typing import Dict,List

# Load saved models
svm_model = joblib.load("svm_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")
le = joblib.load("label_encoder.pkl")

app = FastAPI()

class SymptomInput(BaseModel):
    text: str

@app.post("/predict")
def predict_disease(input_data: SymptomInput):
    # Transform input text
    text_tfidf = tfidf.transform([input_data.text])

    # Predict
    prediction = svm_model.predict(text_tfidf)
    predicted_label = le.inverse_transform(prediction)[0]
    # Extract feature names (symptom terms)
    feature_names = tfidf.get_feature_names_out()

    # Find indices of non-zero features (symptoms present in the input)
    non_zero_indices = text_tfidf.nonzero()[1]  # get indices of non-zero values

    # Get the corresponding symptom names (features)
    symptoms_list = [feature_names[index] for index in non_zero_indices]
    medications = get_medications(symptoms_list)
    return {"predicted_disease": predicted_label,"symptoms_list":symptoms_list,"medications":medications}
# Fetch medications based on symptoms
def get_medications(symptoms: List[str]):
    if not symptoms:  # Handle empty symptoms list
        return [{"brand_name": "Consulter un médecin", "generic_name": "", "usage": "", "dosage_and_administration": ""}]
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    # Make the symptoms list safe for SQL query (escape quotes)
    symptoms_str = "', '".join([symptom.replace("'", "''") for symptom in symptoms])
    print(symptoms_str)
    # Query to get medications based on symptoms
    query = f"""
        SELECT DISTINCT p.MEDICATIONS, p.SYMPTOMS, d.brand_name, d.generic_name, d.dosage_and_administration
        FROM prescription_data p
        JOIN medication_data d ON p.MEDICATIONS = d.brand_name
        WHERE p.SYMPTOMS IN ('{symptoms_str}')
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()


    return result if result else [{"brand_name": "Consulter un médecin", "generic_name": "", "usage": "", "dosage_and_administration": ""}]
# Database connection function
def get_db_connection():
    return mysql.connector.connect(
        user='NLPUSER',
        password='Nlpuser@2025',
        host='SG-Mysql-DB-11663-mysql-master.servers.mongodirector.com',
        database='NLP-MEDIC-DB',
        charset="utf8mb4",
        collation="utf8mb4_unicode_ci"
    )

