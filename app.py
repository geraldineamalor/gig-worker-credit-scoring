import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
st.title("Gig Worker Credit Risk Prediction")
df = pd.read_csv("gig_worker_credit_dataset.csv")
df = df.drop("worker_id", axis=1)
categorical_cols = [
    "gender",
    "city_tier",
    "gig_platform",
    "account_balance_trend",
    "previous_microloan_taken",
    "previous_microloan_repaid",
    "credit_risk_category"
]
encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le
X = df.drop("credit_risk_category", axis=1)
y = df["credit_risk_category"]
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
model.fit(X, y)
st.header("Enter Worker Details")
age = st.number_input("Age", 18, 70, 30)
gender = st.selectbox(
    "Gender",
    encoders["gender"].classes_
)
monthly_income = st.number_input(
    "Monthly Income",
    min_value=0.0,
    value=20000.0
)
city_tier = st.selectbox(
    "City Tier",
    encoders["city_tier"].classes_
)
gig_platform = st.selectbox(
    "Gig Platform",
    encoders["gig_platform"].classes_
)
hours_worked_per_week = st.number_input(
    "Hours Worked Per Week",
    min_value=0,
    value=40
)
jobs_completed = st.number_input(
    "Jobs Completed",
    min_value=0,
    value=100
)
customer_rating = st.number_input(
    "Customer Rating",
    min_value=0.0,
    max_value=5.0,
    value=4.5
)
account_balance_trend = st.selectbox(
    "Account Balance Trend",
    encoders["account_balance_trend"].classes_
)
previous_microloan_taken = st.selectbox(
    "Previous Microloan Taken",
    encoders["previous_microloan_taken"].classes_
)
previous_microloan_repaid = st.selectbox(
    "Previous Microloan Repaid",
    encoders["previous_microloan_repaid"].classes_
)
if st.button("Predict Credit Risk"):

    input_data = pd.DataFrame({
        "age": [age],
        "gender": [
            encoders["gender"].transform([gender])[0]
        ],
        "monthly_income": [monthly_income],
        "city_tier": [
            encoders["city_tier"].transform([city_tier])[0]
        ],
        "gig_platform": [
            encoders["gig_platform"].transform([gig_platform])[0]
        ],
        "hours_worked_per_week": [hours_worked_per_week],
        "jobs_completed": [jobs_completed],
        "customer_rating": [customer_rating],
        "account_balance_trend": [
            encoders["account_balance_trend"].transform(
                [account_balance_trend]
            )[0]
        ],
        "previous_microloan_taken": [
            encoders["previous_microloan_taken"].transform(
                [previous_microloan_taken]
            )[0]
        ],
        "previous_microloan_repaid": [
            encoders["previous_microloan_repaid"].transform(
                [previous_microloan_repaid]
            )[0]
        ]
    })

    prediction = model.predict(input_data)[0]

    risk = encoders[
        "credit_risk_category"
    ].inverse_transform([prediction])[0]

    st.success(f"Predicted Credit Risk: {risk}")
