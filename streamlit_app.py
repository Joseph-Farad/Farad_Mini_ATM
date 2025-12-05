import streamlit as st

st.title('JOE FARAD MINI ATM')
st.set_page_config(page_title="JOE FARAD MINI ATM", page_icon="💳", layout="centered")

st.write("Welcome to Joe Farad ATM")
# --- Initialize balance in session state ---
if "balance" not in st.session_state:
    st.session_state.balance = 1000
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "session_ended" not in st.session_state:
    st.session_state.session_ended = False
if "stored_pin" not in st.session_state:
    st.session_state.stored_pin = "1234"   # Default PIN for demo

if "entered_pin" not in st.session_state:
    st.session_state.entered_pin = ""

# UI Customization
st.markdown("""
<style>
    .atm-box {
        background-color: #E8F1FF;
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #BFD7FF;
        box-shadow: 0px 4px 12px #c8d9f0;
    }
    .title {
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        color: #0A6EBD;
    }
    .pin-display {
        font-size: 32px;
        letter-spacing: 18px;
        text-align: center;
        padding: 10px;
        border: 2px solid #0A6EBD;
        border-radius: 10px;
        background: white;
        margin-bottom: 15px;
    }
    .key-btn {
        width: 90px !important;
        height: 70px !important;
        font-size: 28px !important;
        background-color: #0A6EBD !important;
        color: white !important;
        border-radius: 10px !important;
    }
    .key-btn-red {
        width: 90px !important;
        height: 70px !important;
        font-size: 24px !important;
        background-color: #CB2D3E !important;
        color: white !important;
        border-radius: 10px !important;
    }
</style>
""", unsafe_allow_html=True)

def is_valid_pin(pin):
    return len(pin) == 4 and pin.isdigit() and all(d in "123456789" for d in pin)

# TOUCHSCREEN NUMBER KEYPAD
def keypad():
    st.markdown(f"<div class='pin-display'>{'•'*len(st.session_state.entered_pin)}</div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    for i, num in enumerate(["1","2","3","4","5","6","7","8","9"]):
        if i % 3 == 0:
            col1, col2, col3 = st.columns(3)
            
        if col1.button(num, key=f"k{num}", help="Enter PIN", use_container_width=True):
            if len(st.session_state.entered_pin) < 4:
                st.session_state.entered_pin += num

        num2 = str(int(num)+1) if num != "9" else None

    col1, col2, col3 = st.columns(3)
    if col1.button("Clear", key="clear", use_container_width=True):
        st.session_state.entered_pin = ""

    if col2.button("0", key="zero", use_container_width=True):
        st.warning("Digit '0' not allowed in PIN!")
    
    if col3.button("Enter", key="enter", use_container_width=True):
        return True
    
    return False

# SESSION ENDED
if st.session_state.session_ended:
    st.success("Thank you for using ATM. Goodbye! ")
    st.stop()

# LOGIN PAGE

if not st.session_state.authenticated:
    st.markdown("<h1 class='title'>Enter Your 4-Digit PIN</h1>", unsafe_allow_html=True)
    st.markdown("<div class='atm-box'>", unsafe_allow_html=True)

    pressed = keypad()
    if pressed:
        pin = st.session_state.entered_pin

        if not is_valid_pin(pin):
            st.error("OOps! Invalid PIN, Please try again.")
            st.session_state.entered_pin = ""
            st.stop()
    if pin == st.session_state.stored_pin:
            st.success("PIN correct! Access granted")
            st.session_state.authenticated = True
            st.session_state.entered_pin = ""
    if pin == st.session_state.stored_pin:
        st.success("PIN correct! Access granted ✔")
        st.session_state.authenticated = True
        st.session_state.entered_pin = ""
    else:
        st.error("Wrong PIN! Try again.")
        st.session_state.entered_pin = ""
        
st.stop()

# MAIN ATM MENU
st.markdown("<h1 class='title'>Farad POS ATM</h1>", unsafe_allow_html=True)
st.markdown("<div class='atm-box'>", unsafe_allow_html=True)

menu = st.radio("Please choose an action to continue:", ["Check Balance", "Deposit", "Withdraw", "Change PIN", "Exit"])

# Check Balance
if menu == "Check Balance":
    st.info(f"Your balance is: ₦{st.session_state.balance}")
# Deposit
elif menu == "Deposit":
    amount = st.number_input("Enter deposit amount:", min_value=0.0)
    if st.button("Deposit"):
        st.session_state.balance += amount
        st.success(f"Deposited ₦{amount}. Your new balance is ₦{st.session_state.balance}")

# Withdraw
elif menu == "Withdraw":
    amount = st.number_input("Enter withdrawal amount:", min_value=0.0)
    if st.button("Withdraw"):
        if amount <= st.session_state.balance:
            st.session_state.balance -= amount
            st.success(f"Withdrew ₦{amount}. Your new balance is ₦{st.session_state.balance}")
        else:
            st.error("Sorry! You have insufficient balance")

# To Change PIN
elif menu == "Change PIN":
    st.subheader("Enter Your New 4 Digits PIN")

    new_pin = st.text_input("New PIN:", type="password", max_chars=4)

    if st.button("Update PIN"):
        if is_valid_pin(new_pin):
            st.session_state.stored_pin = new_pin
            st.success("PIN successfully changed! ✔")
        else:
            st.error("Invalid PIN! PIN Must be 4 digits.")
# Exit
elif menu == "Exit":
    if st.button("End Session"):
        st.session_state.session_ended = True
        st.success("Thank you for using ATM. Goodbye!")
        st.stop()

st.markdown("</div>", unsafe_allow_html=True)





"""
st.subheader("ATM Menu")

option = st.radio(
    "Please choose an action to continue:",
    ["Check Balance", "Deposit Money", "Withdraw Money", "Exit"]
)
# Check Balance
if option == "Check Balance":
    st.info(f"Your current balance is: ₦{st.session_state.balance}")
"""


"""
    # Deposit Money
    elif option == "Deposit Money":
        deposit_amount = st.number_input("Enter amount to deposit:", min_value=0.0)
        if st.button("Deposit"):
            st.session_state.balance += deposit_amount
            st.success(f"You deposited ₦{deposit_amount}. Your new balance is ₦{st.session_state.balance}")
    
    # Withdraw Money
    elif option == "Withdraw Money":
        withdraw_amount = st.number_input("Enter amount to withdraw:", min_value=0.0)
        if st.button("Withdraw"):
            if withdraw_amount <= st.session_state.balance:
                st.session_state.balance -= withdraw_amount
                st.success(f"You withdrew ₦{withdraw_amount}. Your new balance is ₦{st.session_state.balance}")
            else:
                st.error("Sorry! You have insufficient balance")
                
    # Exit
    elif option == "Exit":
        if st.button("End Session"):
            st.session_state.balance = 1000
            st.session_state.session_ended = True
            st.success("Goodbye!")
            st.stop()
"""
        
