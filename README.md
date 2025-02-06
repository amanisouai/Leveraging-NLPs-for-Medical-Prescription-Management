# Medical Prescription Management System

## Overview

The **Medical Prescription Management System** is a web application designed to enhance the efficiency and accuracy of medical prescription handling. Leveraging **Natural Language Processing (NLP)**, the system provides preliminary diagnoses, suggests appropriate medications with standardized dosages, and offers clear guidance on treatment administration. This project addresses common issues in medical prescription management, such as unreliable information, over-prescription, and diagnostic errors, particularly in regions with limited access to medical expertise.

---

## Key Features

- **Preliminary Diagnosis**: Provides a preliminary diagnosis based on reported symptoms.
- **Medication Recommendation**: Suggests a list of appropriate medications with standardized dosages.
- **Treatment Guidance**: Offers clear advice on the proper administration of treatments.
- **User-Friendly Interface**: Built with **Streamlit**, the application provides an intuitive and interactive interface for healthcare providers and patients.
- **NLP Integration**: Utilizes **Named Entity Recognition (NER)** with **SpaCy** and **Symptom Classification** with **Support Vector Machines (SVM)** to extract and analyze medical information.

---

## Technologies and Tools

- **Data Collection**: OpenFDA API, HealthService API
- **NLP**: SpaCy
- **Machine Learning**: SVM (Support Vector Machines)
- **Data Visualization**: Matplotlib, Plotly
- **Backend**: FastAPI
- **Frontend**: Streamlit

---

## Project Structure

The project is structured as follows:

1. **Data Collection**: Data is collected using APIs such as OpenFDA and HealthService, which provide structured data on medications, symptoms, and treatment guidelines.
2. **Data Preprocessing**: The collected data is cleaned, normalized, and standardized to ensure consistency and relevance.
3. **NLP Module Development**:
   - **Named Entity Recognition (NER)**: Extracts key medical entities such as drug names, dosages, and symptoms.
   - **Symptom Classification**: Uses SVM to classify symptoms into predefined categories.
4. **Web Application Development**:
   - **Backend**: REST APIs built with FastAPI to serve NLP predictions.
   - **Frontend**: Streamlit-based interface for user interaction and visualization of results.
5. **Deployment**: The application is deployed on Streamlit Cloud for easy access.

---

## Data Fields

The dataset used in this project includes the following key fields:

- **Brand Name**: The commercial name of the medication.
- **Generic Name**: The standard name of the active pharmaceutical ingredient.
- **Manufacturer Name**: The company responsible for producing the medication.
- **Indications and Usage**: Describes the medical conditions or symptoms the medication is intended to treat.
- **Dosage and Administration**: Instructions for dosage and administration of the medication.
- **Cleaned Indications and Usage**: Refined and standardized version of the indications and usage data.
- **Cleaned Dosage and Administration**: Standardized dosage and administration instructions.

---

## Data Challenges

- **Inconsistencies in Text**: Variations in medical terminology require advanced text processing techniques.
- **Missing Data**: Some fields, such as manufacturer names and dosage instructions, may be incomplete.
- **Standardization**: Dosages and administration guidelines often lack uniformity, necessitating standardization.

---

## NLP Pipeline

The NLP pipeline consists of the following steps:

1. **Input**: Raw prescription text (e.g., "500mg acetaminophen for fever").
2. **Preprocessing**: Clean and tokenize the text.
3. **NER Extraction**: Identify and extract relevant entities (e.g., DOSAGE: 500mg, DRUG: acetaminophen, SYMPTOM: fever).
4. **Feature Generation**: Combine structured and text-based features.
5. **Classification**: Predict symptom severity using SVM.
6. **Post-processing**: Generate a structured report summarizing extracted entities and classification results.
7. **Deployment**: Integrate the pipeline into the web application for real-time analysis.

---

## Web Application

The web application is built using **Streamlit** for the frontend and **FastAPI** for the backend. Key features of the application include:

- **Interactive Interface**: Users can input prescription details and view results in real-time.
- **Data Visualization**: Results are displayed using tables and charts for easy interpretation.
- **API Integration**: The backend integrates with the NLP module to provide accurate predictions.

---

## Evaluation

The performance of the NLP models is evaluated using the following metrics:

- **Accuracy**: Measures the overall correctness of the model.
- **Precision**: Indicates the proportion of true positive predictions.
- **Recall**: Measures the model's ability to identify all relevant instances.
- **F1-Score**: Combines precision and recall into a single metric.

---

## Conclusion

The **Medical Prescription Management System** is a comprehensive solution that leverages NLP and machine learning to improve the accuracy and efficiency of medical prescription management. By providing preliminary diagnoses, medication recommendations, and treatment guidance, the system aims to assist healthcare providers and patients in making informed medical decisions. The project follows the **CRISP-DM** methodology, ensuring a structured and reliable approach to data collection, preprocessing, modeling, and deployment.

---

## Acknowledgements

We would like to express our gratitude to the following individuals and organizations for their support and contributions to this project:

- **Mr. Anis Belhadjhassin**: For his invaluable guidance and supervision throughout the project.
- **ESPRIT Professors**: For imparting the knowledge and skills necessary for our academic and personal development.
- **OpenFDA and HealthService APIs**: For providing the data necessary for this project.

---

## Future Work

- **Expand Dataset**: Incorporate additional data sources to improve the comprehensiveness of the system.
- **Enhance NLP Models**: Explore advanced NLP techniques such as transformer-based models (e.g., BERT) for improved accuracy.

---
## Contributors
- Amani Souai
- Mohamed Ali Boumnijel
- Rchid Baccouchi



## How to Run the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/amanisouai/Leveraging-NLPs-for-Medical-Prescription-Management.git
2. Install Dependencies:
     ```bash
    pip install -r requirements.txt
3. **Run the Streamlit App:**
     ```bash
    streamlit run app.py
4. **Access the Application: Open your browser and navigate to**
  ```bash
    http://localhost:8501
