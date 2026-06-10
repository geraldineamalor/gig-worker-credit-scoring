# Gig Worker Credit Risk Prediction

## Project Overview

This project predicts the credit risk category of gig workers using Machine Learning techniques. The model analyzes worker information such as income, work history, customer ratings, and loan repayment behavior to determine the credit risk category.

The project includes:

- Data Preprocessing
- Exploratory Data Analysis (EDA)
- Machine Learning Model Training
- Credit Risk Prediction
- Streamlit Web Application

---

## Dataset

The dataset contains information about gig workers, including:

- Age
- Gender
- Monthly Income
- City Tier
- Gig Platform
- Hours Worked Per Week
- Jobs Completed
- Customer Rating
- Account Balance Trend
- Previous Microloan Taken
- Previous Microloan Repaid
- Credit Risk Category (Target Variable)

---

## Technologies Used

- Python
- Pandas
- Scikit-learn
- XGBoost
- Streamlit

---

## Machine Learning Models

The following models were trained and evaluated:

1. Logistic Regression
2. Random Forest Classifier
3. XGBoost Classifier

Performance was compared using accuracy scores and classification reports.

---

## Project Structure

```text
├── app.py
├── requirements.txt
├── gig_worker_credit_dataset.csv
├── gig_worker_credit_scoring.ipynb
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <repository-link>
cd <repository-name>
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## Features

- User-friendly Streamlit interface
- Real-time credit risk prediction
- Automatic data preprocessing
- Machine learning-based prediction
- Easy deployment using Streamlit Cloud

---

## Workflow

1. Load Dataset
2. Data Cleaning and Preprocessing
3. Encode Categorical Variables
4. Split Dataset into Training and Testing Sets
5. Train Machine Learning Models
6. Evaluate Model Performance
7. Predict Credit Risk Category
8. Deploy using Streamlit

---

## Results

The trained models were evaluated using:

- Accuracy Score
- Confusion Matrix
- Classification Report

The Random Forest model was selected for deployment due to its strong predictive performance.

---

## Future Improvements

- Hyperparameter Tuning
- Feature Engineering
- Advanced Ensemble Models
- Cloud Database Integration
- Real-Time Data Collection

---

## License

This project is created for educational and academic purposes.
