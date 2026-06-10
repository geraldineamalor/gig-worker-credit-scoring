import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("models/credit_model.pkl")

st.title("Alternative Credit Scoring for Gig Workers")

st.subheader("Enter Worker Details")

age = st.number_input("Age", 18, 60, 25)

gender = st.selectbox("Gender", ["Female", "Male"])

city_tier = st.selectbox(
    "City Tier",
    ["Tier1", "Tier2", "Tier3"]
)

gig_platform = st.selectbox(
    "Gig Platform",
    ["Zomato", "Swiggy", "Uber", "Ola", "Freelancer", "Urban Company"]
)

months_active = st.number_input("Months Active", 1, 120, 12)

monthly_income = st.number_input(
    "Monthly Income",
    10000,
    100000,
    30000
)

income_consistency_score = st.slider(
    "Income Consistency Score",
    0,
    100,
    70
)

upi_transaction_count = st.number_input(
    "UPI Transaction Count",
    0,
    1000,
    100
)

average_transaction_value = st.number_input(
    "Average Transaction Value",
    0,
    10000,
    500
)

monthly_inflow = st.number_input(
    "Monthly Inflow",
    0,
    200000,
    35000
)

monthly_outflow = st.number_input(
    "Monthly Outflow",
    0,
    200000,
    25000
)

savings_ratio = st.slider(
    "Savings Ratio",
    0.0,
    100.0,
    20.0
)

utility_bill_payment_rate = st.slider(
    "Utility Bill Payment Rate",
    0,
    100,
    90
)

mobile_recharge_frequency = st.number_input(
    "Mobile Recharge Frequency",
    0,
    30,
    4
)

customer_rating = st.slider(
    "Customer Rating",
    1.0,
    5.0,
    4.0
)

task_completion_rate = st.slider(
    "Task Completion Rate",
    0,
    100,
    90
)

active_days_per_month = st.number_input(
    "Active Days Per Month",
    1,
    31,
    25
)

working_hours_per_week = st.number_input(
    "Working Hours Per Week",
    1,
    80,
    40
)

account_balance_trend = st.selectbox(
    "Account Balance Trend",
    ["Decreasing", "Stable", "Increasing"]
)

previous_microloan_taken = st.selectbox(
    "Previous Microloan Taken",
    ["No", "Yes"]
)

previous_microloan_repaid = st.selectbox(
    "Previous Microloan Repaid",
    ["No", "Yes"]
)

financial_stability_score = st.slider(
    "Financial Stability Score",
    0.0,
    100.0,
    70.0
)

# Manual encoding
gender_map = {"Female": 0, "Male": 1}
city_map = {"Tier1": 0, "Tier2": 1, "Tier3": 2}
platform_map = {
    "Freelancer": 0,
    "Ola": 1,
    "Swiggy": 2,
    "Uber": 3,
    "Urban Company": 4,
    "Zomato": 5
}
trend_map = {
    "Decreasing": 0,
    "Increasing": 1,
    "Stable": 2
}
loan_map = {"No": 0, "Yes": 1}

if st.button("Predict Credit Risk"):

    input_data = pd.DataFrame([{
        "age": age,
        "gender": gender_map[gender],
        "city_tier": city_map[city_tier],
        "gig_platform": platform_map[gig_platform],
        "months_active": months_active,
        "monthly_income": monthly_income,
        "income_consistency_score": income_consistency_score,
        "upi_transaction_count": upi_transaction_count,
        "average_transaction_value": average_transaction_value,
        "monthly_inflow": monthly_inflow,
        "monthly_outflow": monthly_outflow,
        "savings_ratio": savings_ratio,
        "utility_bill_payment_rate": utility_bill_payment_rate,
        "mobile_recharge_frequency": mobile_recharge_frequency,
        "customer_rating": customer_rating,
        "task_completion_rate": task_completion_rate,
        "active_days_per_month": active_days_per_month,
        "working_hours_per_week": working_hours_per_week,
        "account_balance_trend": trend_map[account_balance_trend],
        "previous_microloan_taken": loan_map[previous_microloan_taken],
        "previous_microloan_repaid": loan_map[previous_microloan_repaid],
        "financial_stability_score": financial_stability_score
    }])

    prediction = model.predict(input_data)[0]

    risk_map = {
        0: "High Risk",
        1: "Low Risk",
        2: "Medium Risk"
    }

    st.success(
        f"Predicted Credit Risk: {risk_map[prediction]}"
    )
