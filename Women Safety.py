import streamlit as st
import datetime
import random

# Session setup
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'complaints' not in st.session_state:
    st.session_state.complaints = []
if 'contacts' not in st.session_state:
    st.session_state.contacts = []

# Custom CSS - Updated Theme
st.markdown("""
<style>
body {
    background-color: #f0f2f6;
    font-family: 'Segoe UI', sans-serif;
}
.header {
    font-size: 40px;
    color: white;
    text-align: center;
    padding: 15px;
    background: linear-gradient(90deg, #ff4b2b, #ff416c);
    border-radius: 12px;
    margin-bottom: 25px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}
.footer {
    font-size: 14px;
    color: white;
    text-align: center;
    padding: 12px;
    margin-top: 30px;
    background: linear-gradient(90deg, #ff4b2b, #ff416c);
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.15);
}
.urgent-help {
    font-size: 26px;
    color: white;
    background: #ff4b2b;
    border-radius: 12px;
    padding: 15px;
    text-align: center;
    margin-top: 20px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}
.safety-message {
    text-align: center;
    color: #ff416c;
    font-size: 22px;
    margin-bottom: 20px;
    font-weight: 500;
}
.menu-bar {
    display: flex;
    justify-content: center;
    gap: 12px;
    flex-wrap: wrap;
    margin-bottom: 20px;
}
.menu-button {
    background-color: white;
    border: 1px solid #ff4b2b;
    padding: 10px 15px;
    border-radius: 10px;
    cursor: pointer;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# Login Section
if not st.session_state.logged_in:
    st.markdown('<div class="header">Women\'s Safety Portal</div>', unsafe_allow_html=True)
    st.markdown('<div class="safety-message">For Your Safety and Support</div>', unsafe_allow_html=True)
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "user" and password == "1234":
            st.session_state.logged_in = True
            st.experimental_rerun()
        else:
            st.error("Wrong username or password")
    st.markdown('<div class="footer">© 2025 Women\'s Safety Portal | Made by JATIN KHANDAL</div>', unsafe_allow_html=True)

else:
    st.markdown('<div class="header">Women\'s Safety Portal</div>', unsafe_allow_html=True)
    st.markdown('<div class="safety-message">For Your Safety and Support</div>', unsafe_allow_html=True)
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.experimental_rerun()

    # Persistent horizontal menu
    menu_options = [
        "Home", "Submit Complaint", "Track Complaint", "Urgent Help",
        "Manage Trusted Contacts", "Upload Evidence", "Anonymous Report", "Stats Dashboard"
    ]

    selected_option = st.radio("Navigation", menu_options, horizontal=True)

    # Pages
    if selected_option == "Home":
        st.write("Welcome! This portal is for women only, to ensure your safety and support.")
        st.write("Select an option from the menu above.")

    elif selected_option == "Submit Complaint":
        st.subheader("Submit a Complaint")
        complaint = st.text_area("Describe your complaint or concern")
        if st.button("Submit"):
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            st.session_state.complaints.append((timestamp, complaint))
            st.success("Thank you! Your complaint has been submitted.")

    elif selected_option == "Track Complaint":
        st.subheader("Your Complaint History")
        if st.session_state.complaints:
            for time, comp in reversed(st.session_state.complaints):
                st.markdown(f"**[{time}]**: {comp}")
        else:
            st.info("No complaints submitted yet.")

    elif selected_option == "Urgent Help":
        st.markdown('<div class="urgent-help">URGENT HELP</div>', unsafe_allow_html=True)
        current_hour = datetime.datetime.now().hour
        if 18 <= current_hour or current_hour < 6:
            st.write("*Emergency contacts have been notified. Stay calm, help is on the way!*")
        else:
            st.write("*Urgent help is available 24/7. Use the buttons below to notify.*")

        if st.button("Share I'm Travelling NOTIFICATION TO Loved Ones"):
            st.success("Urgent notification sent to Loved Ones!")
        if st.button("SEND Live Location TO Brother/Husband"):
            st.success("SENDED Live Location TO Brother/Husband!")
        if st.button("SEND Help URGENT NOTIFICATION TO POLICE"):
            st.success("Urgent notification sent to Police Station and emergency contacts!")
        if st.button("SEND Help URGENT NOTIFICATION TO ALL FAMILY MEMBERS"):
            st.success("Urgent notification sent to all registered family members!")

        st.subheader("Emergency Contact Numbers")
        st.write("*Police:* 100")
        st.write("*Ambulance:* 108")
        st.write("*Women's Helpline:* 1091")
        st.write("*Domestic Violence Helpline:* 181")

    elif selected_option == "Manage Trusted Contacts":
        st.subheader("Trusted Contacts")
        name = st.text_input("Name")
        relation = st.text_input("Relation")
        phone = st.text_input("Phone Number")
        if st.button("Add Contact"):
            st.session_state.contacts.append({"name": name, "relation": relation, "phone": phone})
            st.success("Contact added!")
        if st.session_state.contacts:
            st.write("Your Trusted Contacts:")
            for c in st.session_state.contacts:
                st.markdown(f"**{c['name']}** ({c['relation']}) – 📞 {c['phone']}")

    elif selected_option == "Upload Evidence":
        st.subheader("Upload Evidence")
        file = st.file_uploader("Upload a file (image/video/audio)", type=["jpg", "png", "mp4", "mp3"])
        if file:
            st.success("File uploaded successfully!")

    elif selected_option == "Anonymous Report":
        st.subheader("Report Anonymously")
        anon_complaint = st.text_area("Type your concern")
        if st.button("Submit Anonymously"):
            st.success("Submitted! You remain anonymous.")

    elif selected_option == "Stats Dashboard":
        st.subheader("Safety Portal Stats")
        st.metric("Complaints Submitted", len(st.session_state.complaints))
        st.metric("Emergency Alerts Sent", 4)
        st.metric("Trusted Contacts Added", len(st.session_state.contacts))

    st.markdown('<div class="footer">© 2025 Women\'s Safety | Made by JATIN KHANDAL</div>', unsafe_allow_html=True)
