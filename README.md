🧠 Parkinson Detection App

An AI-powered Streamlit application that analyzes voice biomarkers to detect early signs of Parkinson’s disease. Built with XGBoost, SHAP for explainability, and MLflow for experiment tracking. Designed for educational and prototyping purposes, with future potential for real-time monitoring.

🚀 Features

Upload .csv files containing voice biomarker data

Predict Parkinson’s status with confidence scores

Visualize feature importance using SHAP (XAI)

Log user sessions anonymously for traceability

Track model metrics and artifacts with MLflow

🧪 Technologies Used

Programming: Python

ML Models: XGBoost

Explainability: SHAP

MLOps: MLflow

Web App: Streamlit

Utilities: Pandas, NumPy, Scikit-learn, Joblib

# parkinsons_project/

📊 Input Format

Upload a .csv file with the following columns (excluding name):

MDVP:Fo(Hz), MDVP:Fhi(Hz), MDVP:Flo(Hz)
Jitter(%), Shimmer(dB), HNR
RPDE, DFA, spread1, spread2, D2, PPE
status (0 = healthy, 1 = Parkinson’s)

Sample dataset: UCI Parkinson’s Data

🧠 Explainable AI (XAI)

Global Explanation: SHAP summary plot shows which features most influence predictions.

Individual Prediction: SHAP waterfall plot explains why a specific prediction was made.

🔄 Reliability Features

Confidence scores displayed for each prediction

Accuracy and classification metrics logged via MLflow

Optional calibration methods available for future extension

🧾 Session Logging
Each user session is tracked anonymously using a unique ID. Logged data includes:

Timestamp

Uploaded file name

Prediction result

Confidence score

Saved to: logs/user_sessions.csv

📌 Ethical Considerations

This app uses voice biomarkers for educational purposes and is not a certified diagnostic tool. It does not include demographic attributes (e.g., age, gender, ethnicity), and fairness audits are not applicable. Future versions may include real-time audio input and continuous monitoring features.
