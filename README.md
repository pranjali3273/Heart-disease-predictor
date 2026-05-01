Dashboard Screenshots:
src="https://github.com/user-attachments/assets/4acda7c9-60c5-47d5-9a8d-f69bf2936b63"

💓 Heart Disease Prediction App

A simple and interactive Machine Learning web application built using Streamlit that predicts whether a person is likely to have heart disease based on medical parameters.

🚀 Project Overview

This project uses a trained Machine Learning model to analyze user-provided health data and predict the risk of heart disease.

The app provides an easy-to-use interface where users can input their medical details and instantly get predictions.

🧠 Features
User-friendly interface built with Streamlit
Real-time heart disease prediction
Takes multiple medical parameters as input
Instant result display with clear indication
Lightweight and easy to run locally
📊 Input Parameters

The model uses the following health attributes:

Age
Sex
Chest Pain Type (0–3)
Resting Blood Pressure
Serum Cholesterol (mg/dl)
Fasting Blood Sugar (>120 mg/dl)
Resting ECG Results
Maximum Heart Rate Achieved
Exercise Induced Angina
ST Depression (Oldpeak)
Slope of ST Segment
Number of Major Vessels (0–3)
Thalassemia (1 = normal, 2 = fixed defect, 3 = reversible defect)
🛠️ Tech Stack
Python
Streamlit
NumPy
Pickle (for loading trained model)
Machine Learning Model (pre-trained)
📂 Project Structure
├── app.py                      # Main Streamlit application
├── heart_disease_model.pkl    # Trained ML model
├── README.md                  # Project documentation
⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/your-username/heart-disease-prediction.git
cd heart-disease-prediction
2. Install Dependencies
pip install -r requirements.txt

(If requirements.txt is not available, install manually)

pip install streamlit numpy
▶️ Run the Application
streamlit run app.py
📸 How It Works
Enter the required medical details
Click on the Predict button
The app will display:
⚠️ High risk of heart disease
✅ Low risk of heart disease
⚠️ Disclaimer

This application is for educational purposes only and should not be used as a substitute for professional medical advice, diagnosis, or treatment.

📌 Future Improvements
Add model accuracy and evaluation metrics
Improve UI/UX design
Deploy the app online (Streamlit Cloud / AWS / Render)
Add data visualization and reports
