from fastapi import FastAPI
import mysql.connector
import spacy
import pandas as pd
from typing import Dict

app = FastAPI()

# Load spaCy NLP model
nlp = spacy.load("en_ner_bc5cdr_md")


@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}


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

# Fetch symptoms from MySQL
def get_all_symptoms():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT DISTINCT SYMPTOMS FROM prescription_data")
    symptoms_data = cursor.fetchall()
    cursor.close()
    connection.close()
    return [row["SYMPTOMS"].lower() for row in symptoms_data]

# Extract symptoms, diseases, and medications using NER
def extract_entities(text: str):
    doc = nlp(text)
    symptoms_db = get_all_symptoms()

    entities = {"SYMPTOMS": [], "DISEASES": [], "MEDICATIONS": []}

    for ent in doc.ents:
        if ent.label_ == "DISEASE":  
            entities["DISEASES"].append(ent.text)
        elif ent.label_ == "CHEMICAL":  
            entities["MEDICATIONS"].append(ent.text)

    # Match symptoms from database
    for symptom in symptoms_db:
        if symptom in text.lower():
            entities["SYMPTOMS"].append(symptom)
        # Ensure no empty strings in the lists
    entities["SYMPTOMS"] = [symptom for symptom in entities["SYMPTOMS"] if symptom]
    entities["DISEASES"] = [disease for disease in entities["DISEASES"] if disease]
    entities["MEDICATIONS"] = [med for med in entities["MEDICATIONS"] if med]
    return entities
    

# Fetch diseases based on symptoms
def get_disease(symptoms):
    if not symptoms:  # Handle empty symptoms list
        return []
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    symptoms_str = "', '".join(symptoms)
    query = f"""
        SELECT DISTINCT DISEASES FROM prescription_data
        WHERE SYMPTOMS IN ('{symptoms_str}')
        LIMIT 10
    """
    cursor.execute(query)
    result = cursor.fetchall()
    print(symptoms)
    cursor.close()
    connection.close()

    return [row["DISEASES"] for row in result] if result else ["Aucune maladie trouvée"]

# Fetch medications based on symptoms
def get_medications(symptoms):
    if not symptoms:  # Handle empty symptoms list
        return []
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    symptoms_str = "', '".join(symptoms)
    query = f"""
        SELECT DISTINCT p.MEDICATIONS,p.SYMPTOMS, d.brand_name, d.generic_name, d.dosage_and_administration  
        FROM prescription_data p
        JOIN medication_data d ON p.MEDICATIONS = d.brand_name
        WHERE p.SYMPTOMS IN ('{symptoms_str}') 
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()


    return result if result else [{"brand_name": "Consulter un médecin", "generic_name": "", "usage": "", "dosage_and_administration": ""}]

# API Endpoint to process input text
@app.get("/analyze_symptoms")
def analyze_symptoms(text: str):
    entities = extract_entities(text)
    diseases = get_disease(entities["SYMPTOMS"])
    medications = get_medications(entities["SYMPTOMS"])

    return {
        "extracted_symptoms": entities["SYMPTOMS"],
        "diagnosis": diseases,
        "medications": medications
    }
    
