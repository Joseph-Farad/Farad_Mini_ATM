import streamlit as st

st.title('Farad Mini POS Machine')

st.write("Welcome to Farad's POS Menu")
# --- Initialize balance in session state ---
if "balance" not in st.session_state:
    st.session_state.balance = 1000

st.subheader("Please Select Option to Continue")

option = st.radio(
    "Choose an action:",
    ["Check Balance", "Deposit Money", "Withdraw Money", "Exit"]
)
