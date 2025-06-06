import streamlit as st
import datetime

# Custom CSS for header and footer
st.markdown("""
<style>
.header {
    font-size: 40px;
    color: #e83e8c;
    text-align: center;
    padding: 10px;
    background: #fff0f6;
    border-radius: 10px;
    margin-bottom: 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}
.footer {
    font-size: 16px;
    color: #adb5bd;
    text-align: center;
    padding: 10px;
    margin-top: 20px;
    background: #fff0f6;
    border-radius: 10px;
}
.urgent-help {
    font-size: 26px;
    color: #ff0000;
    background: #ffe6e6;
    border-radius: 10px;
    padding: 10px;
    text-align: center;
    margin-top: 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}
.safety-message {
    text-align: center;
    color: #e83e8c;
    font-size: 20px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# Simple login/logout logic
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown('<div class="header">Women\'s Safety Portal</div>', unsafe_allow_html=True)
    st.markdown('<div class="safety-message">For Your Safety and Support</div>', unsafe_allow_html=True)
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        # Very simple check (not secure!)
        if username == "user" and password == "1234":
            st.session_state.logged_in = True
            st.experimental_rerun()
        else:
            st.error("Wrong username or password")
    st.markdown('<div class="footer">© 2025 Women\'s Safety Portal</div>', unsafe_allow_html=True)
else:
    # Header and welcome message
    st.markdown('<div class="header">Women\'s Safety Portal</div>', unsafe_allow_html=True)
    st.markdown('<div class="safety-message">For Your Safety and Support</div>', unsafe_allow_html=True)
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.experimental_rerun()

    # Menu
    option = st.selectbox("Choose an option:", ["Home", "Submit Complaint", "Track Complaint", "Urgent Help"])

    # Home Page
    if option == "Home":
        st.write("Welcome! This portal is for women only, to ensure your safety and support.")
        st.write("Select an option from the menu above.")

    # Submit Complaint
    elif option == "Submit Complaint":
        st.subheader("Submit a Complaint")
        complaint = st.text_area("Describe your complaint or concern")
        if st.button("Submit"):
            st.success("Thank you! Your complaint has been submitted.")

    # Track Complaint
    elif option == "Track Complaint":
        st.subheader("Track Your Complaint")
        st.write("Complaint Status: In Progress")
        st.write("We are working on your issue. Thank you for your patience.")

    # Urgent Help (Night Mode)
    elif option == "Urgent Help":
        st.markdown('<div class="urgent-help">URGENT HELP</div>', unsafe_allow_html=True)
        current_hour = datetime.datetime.now().hour
        if 18 <= current_hour or current_hour < 6:  # Night hours (6pm to 6am)
            st.write("*You are using the urgent help feature during night hours.*")
            st.write("*Emergency contacts have been notified.*")
            st.write("*Stay calm, help is on the way!*")
        else:
            st.write("*Urgent help is available 24/7.*")
            st.write("*If you are in danger, use the buttons below to notify authorities and family members.*")

                # Button to send notification to loved ones (address) (simulated)
        if st.button("Share I'm Travelling NOTIFICATION TO Loved Ones"):
            st.success("Urgent notification sent to Loved Ones!")

        # Button to send Live location (simulated)
        if st.button("SEND Live Location TO Brother/Husband"):
            st.success("SENDED Live Location TO Brother/Husband!")
         
        # Single button to send urgent notification to police (simulated)
        if st.button("SEND Help URGENT NOTIFICATION TO POLICE"):
            st.success("Urgent notification sent to the nearest police station and emergency contacts!")

        # Button to send urgent notification to all family members (simulated)
        if st.button("SEND Help URGENT NOTIFICATION TO ALL FAMILY MEMBERS"):
            st.success("Urgent notification sent to all registered family members!")




        # Display emergency contact numbers
        st.subheader("Emergency Contact Numbers")
        st.write("*Police:* 100")
        st.write("*Ambulance:* 108")
        st.write("*Women's Helpline:* 1091")
        st.write("*Domestic Violence Helpline:* 181")

    # Footer
    st.markdown('<div class="footer">© 2025 Women\'s Safety</div>', unsafe_allow_html=True)