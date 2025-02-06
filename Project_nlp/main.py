import streamlit as st
import requests
import plotly.express as px
import pandas as pd

API_URL = "http://127.0.0.1:8000/analyze_symptoms"

st.title("💊 Diagnostic & Traitement Médical")
st.write("Décrivez vos symptômes en texte libre pour obtenir un diagnostic.")

# Text input field
symptoms_text = st.text_area("🩺 Décrivez vos symptômes")

# Fetch results when button is clicked
if st.button("🔍 Obtenir le diagnostic"):
    if symptoms_text:
        response = requests.get(API_URL, params={"text": symptoms_text})

        if response.status_code == 200:
            data = response.json()

            # Display extracted symptoms
            st.subheader("📝 Symptômes Identifiés")
            symptoms = [symptom for symptom in data.get("extracted_symptoms", []) if symptom]  # Filter out empty values
            if symptoms:
                for symptom in symptoms:
                    st.write(f"- {symptom}")
            else:
                st.write("Aucun symptôme identifié.")

            # Display diagnosis
            st.subheader("🦠 Diagnostic Préliminaire")
            diagnosis = [disease for disease in data.get("diagnosis", []) if disease]  # Filter out empty values
            if diagnosis:
                for disease in diagnosis:
                    st.write(f"- **{disease}**")
            else:
                st.write("Aucun diagnostic disponible.")

            # Display medications
            st.subheader("💊 Médicaments Recommandés")
            medications = [med for med in data.get("medications", []) if med and med.get("brand_name") and med.get("generic_name")]
            if medications:
                for med in medications:
                    st.write(f"**{med['brand_name']}** ({med['generic_name']}) -  {med['dosage_and_administration']}")
            else:
                st.write("Aucun médicament recommandé.")

            # Add charts
            st.subheader("📊 Statistiques des Symptômes")
            if symptoms:
                # Create a DataFrame for symptoms
                symptoms_df = pd.DataFrame({
                    "Symptômes": symptoms,
                    "Fréquence": [1] * len(symptoms)  # Assuming each symptom appears once
                })

            if diagnosis:
                # Create a DataFrame for diagnosis
                diagnosis_df = pd.DataFrame({
                    "Diagnostics": diagnosis,
                    "Fréquence": [1] * len(diagnosis)  # Assuming each diagnosis appears once
                })

                # Pie chart for diagnosis
                fig = px.pie(diagnosis_df, names="Diagnostics", values="Fréquence", title="Répartition des Diagnostics")
                st.plotly_chart(fig)

        else:
            st.error("Erreur lors de la récupération des données. Veuillez réessayer.")

    else:
        st.warning("⚠️ Veuillez entrer une description de vos symptômes.")