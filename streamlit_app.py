import streamlit as st

st.title('JOE FARAD MINI ATM')

st.write("Welcome to Joe Farad ATM Menu")
# --- Initialize balance in session state ---
if "balance" not in st.session_state:
    st.session_state.balance = 1000

st.subheader("ATM")

option = st.radio(
    "Choose an action:",
    ["Check Balance", "Deposit Money", "Withdraw Money", "Exit"]
)
# Check Balance
if option == "Check Balance":
    st.info(f"Your current balance is: ₦{st.session_state.balance}")

# Deposit Money
elif option == "Deposit Money":
    deposit_amount = st.number_input("Enter amount to deposit:", min_value=0.0)
    if st.button("Deposit"):
        st.session_state.balance += deposit_amount
        st.success(f"You deposited ₦{deposit_amount}. New balance is ₦{st.session_state.balance}")

# Withdraw Money
elif option == "Withdraw Money":
    withdraw_amount = st.number_input("Enter amount to withdraw:", min_value=0.0)
    if st.button("Withdraw"):
        if withdraw_amount <= st.session_state.balance:
            st.session_state.balance -= withdraw_amount
            st.success(f"You withdrew ₦{withdraw_amount}. New balance is ₦{st.session_state.balance}")
        else:
            st.error("Insufficient balance!")
            
# Exit / Reset
elif option == "Exit":
    if st.button("End Session"):
        st.session_state.balance = 1000
        st.warning("Session ended. Balance reset to ₦1000.")
