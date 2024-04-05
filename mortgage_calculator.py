import streamlit as st
import math
import pandas as pd

def calculate_mortgage(home_value, deposit, interest_rate, loan_term):
    loan_amount = home_value - deposit
    monthly_interest_rate = (interest_rate / 100) / 12
    number_of_payments = loan_term * 12
    monthly_payment = (
        loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments)
        / ((1 + monthly_interest_rate) ** number_of_payments - 1)
    )

    total_payments = monthly_payment * number_of_payments
    total_interest = total_payments - loan_amount

    return monthly_payment, total_payments, total_interest

def generate_payment_schedule(loan_amount, monthly_payment, monthly_interest_rate, number_of_payments):
    schedule = []
    remaining_balance = loan_amount

    for i in range(1, number_of_payments + 1):
        interest_payment = remaining_balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment
        remaining_balance -= principal_payment
        year = math.ceil(i / 12)
        schedule.append(
            [
                i,
                monthly_payment,
                principal_payment,
                interest_payment,
                remaining_balance,
                year,
            ]
        )

    return pd.DataFrame(
        schedule,
        columns=["Month", "Payment", "Principal", "Interest", "Remaining Balance", "Year"],
    )

def main():
    st.title("Mortgage Repayments Calculator APP")
    st.write("### Input Data")

    col1, col2 = st.columns(2)
    home_value = col1.number_input("Home Value", min_value=0, value=500000)
    deposit = col1.number_input("Deposit", min_value=0, value=100000)
    interest_rate = col2.number_input("Interest Rate (in%)", min_value=0.0, value=5.5)
    loan_term = col2.number_input("Loan Term (in years)", min_value=0, value=30)

    monthly_payment, total_payments, total_interest = calculate_mortgage(home_value, deposit, interest_rate, loan_term)

    st.write("### Repayments")

    col1, col2, col3 = st.columns(3)
    col1.metric(label="Monthly Repayments", value=f"${monthly_payment:,.2f}")
    col2.metric(label="Total Repayments", value=f"${total_payments:,.0f}")
    col3.metric(label="Total Interest", value=f"${total_interest:,.0f}")

    payment_schedule_df = generate_payment_schedule(
        home_value - deposit,
        monthly_payment,
        (interest_rate / 100) / 12,
        loan_term * 12
    )

    st.write("### Payment Schedule")
    payments_df = payment_schedule_df.groupby("Year").agg({"Remaining Balance": "last"})
    st.line_chart(payments_df)

    st.write("### Detailed Payment Schedule")
    st.write(payment_schedule_df)

if __name__ == "__main__":
    main()
