import streamlit as st
import requests

st.title("🧾 Finance Monitor AI")

with st.form("txn_form"):
    date = st.date_input("Transaction Date")
    amount = st.number_input("Amount", min_value=0.01)
    purpose = st.text_input("Purpose")
    submit = st.form_submit_button("Submit")

    if submit:
        data = {"date": str(date), "amount": amount, "purpose": purpose}
        res = requests.post(
            "http://localhost:8000/add_transaction/", json=data)
        st.success(f"AI Insight: {res.json()['analysis']}")

if st.button("View All Transactions"):
    txns = requests.get("http://localhost:8000/transactions/").json()
    st.write(txns)
