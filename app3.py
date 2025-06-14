import streamlit as st

st.set_page_config(page_title="Smart Credit Score & Loan Eligibility", layout="centered")
st.title("📊 AI-Based Credit Score & Loan Eligibility Checker")

st.markdown("Please fill in your details to calculate your credit score and check loan eligibility.")

# --- INPUTS ---
age = st.slider("Your Age", 18, 65, 30)
income = st.number_input("Monthly Salary (₹)", 10000, 1000000, 50000)
loan_amount = st.number_input("Requested Loan Amount (₹)", 1000, 3000000, 100000)
employment_years = st.slider("Years of Employment", 0, 40, 5)
credit_history = st.selectbox("Credit History", ["Excellent", "Good", "Average", "Poor", "Bad"])
existing_emis = st.slider("Number of Active EMIs", 0, 10, 1)
dependents = st.slider("Number of Financial Dependents", 0, 10, 2)

# --- SCORE FUNCTION ---
def calculate_credit_score(age, income, loan_amount, employment_years, credit_history, existing_emis, dependents):
    score = 0

    # Age Score (out of 50)
    if 25 <= age <= 45:
        score += 50
    elif 20 <= age <= 55:
        score += 35
    else:
        score += 20

    # Income Score (out of 150)
    if income >= 100000:
        score += 150
    elif income >= 70000:
        score += 120
    elif income >= 50000:
        score += 90
    elif income >= 30000:
        score += 60
    else:
        score += 30

    # Loan Amount Score (out of 100)
    if loan_amount <= income * 1:
        score += 100
    elif loan_amount <= income * 2:
        score += 75
    elif loan_amount <= income * 3:
        score += 50
    else:
        score += 20

    # Employment Score (out of 150)
    if employment_years >= 10:
        score += 150
    elif employment_years >= 5:
        score += 100
    elif employment_years >= 2:
        score += 60
    else:
        score += 30

    # Credit History Score (out of 250)
    credit_scores = {
        "Excellent": 250,
        "Good": 200,
        "Average": 150,
        "Poor": 80,
        "Bad": 30
    }
    score += credit_scores[credit_history]

    # Existing EMIs (out of 100)
    if existing_emis == 0:
        score += 100
    elif existing_emis == 1:
        score += 80
    elif existing_emis == 2:
        score += 60
    elif existing_emis == 3:
        score += 40
    else:
        score += 20

    # Dependents (out of 50)
    if dependents == 0:
        score += 50
    elif dependents <= 2:
        score += 40
    elif dependents <= 4:
        score += 30
    else:
        score += 10

    return round(score)

# --- BUTTON ---
if st.button("Calculate Credit Score & Check Eligibility"):
    score = calculate_credit_score(age, income, loan_amount, employment_years, credit_history, existing_emis, dependents)
    st.subheader(f"🧾 Your Credit Score: **{score} / 850**")

    # --- Eligibility Logic ---
    max_loan_allowed = 3 * income
    if score >= 700 and loan_amount <= max_loan_allowed:
        st.success(f"✅ You are eligible for the loan! 🎉\nMaximum allowed based on income: ₹{max_loan_allowed}")
    elif score < 700 and loan_amount <= max_loan_allowed:
        st.warning("⚠️ Your credit score is too low for eligibility.")
    elif score >= 700 and loan_amount > max_loan_allowed:
        st.warning(f"⚠️ Your requested loan exceeds the maximum allowed (₹{max_loan_allowed}).")
    else:
        st.error("❌ Not eligible for the loan due to both low score and high loan request.")

    st.markdown("---")
    st.info("📌 This is a simplified model. For official approval, banks consider more detailed credit reports.")
    st.info("💡 Always check with your bank for accurate eligibility criteria and loan terms.")

