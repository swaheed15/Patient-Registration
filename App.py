import streamlit as st
import pandas as pd
import numpy as np


import streamlit as st
import pandas as pd

# -----------------------
# Initialize Patient Database (if not already in session state)
if "patients" not in st.session_state:
    st.session_state.patients = pd.DataFrame(columns=["Full Name", "Age", "Gender", "Contact", "Medical History"])

# Function to Add Patient to DataFrame
def add_patient(name, age, gender, contact, history):
    new_patient = pd.DataFrame(
        [[name, age, gender, contact, history]],
        columns=["Full Name", "Age", "Gender", "Contact", "Medical History"]
    )
    st.session_state.patients = pd.concat([st.session_state.patients, new_patient], ignore_index=True)

# -----------------------
# Streamlit UI
st.title("🏥 Patient Data Collection System")

# Sidebar Navigation
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Select an option", ["Register Patient", "View Patients", "Search Patient", "Upload Reports"])

# -----------------------
# Patient Registration Form
if menu == "Register Patient":
    st.subheader("📝 Register a New Patient")
    
    with st.form("patient_form"):
        full_name = st.text_input("Full Name")
        age = st.number_input("Age", min_value=0, max_value=120, step=1)
        gender = st.radio("Gender", ["Male", "Female", "Other"])
        contact = st.text_input("Contact Number")
        medical_history = st.text_area("Medical History")
        
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            if full_name and contact:
                add_patient(full_name, age, gender, contact, medical_history)
                st.success(f"✅ Patient '{full_name}' added successfully!")
            else:
                st.warning("⚠️ Please fill in the required fields!")

# -----------------------
# View All Registered Patients
elif menu == "View Patients":
    st.subheader("📋 Registered Patients")
    
    if not st.session_state.patients.empty:
        st.dataframe(st.session_state.patients)
        csv = st.session_state.patients.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download Patient Data", data=csv, file_name="patients.csv", mime="text/csv")
    else:
        st.info("No patients registered yet.")

# -----------------------
# Search for a Patient
elif menu == "Search Patient":
    st.subheader("🔍 Search for a Patient")
    
    search_query = st.text_input("Enter Patient Name")
    
    if search_query:
        filtered_df = st.session_state.patients[
            st.session_state.patients["Full Name"].str.contains(search_query, case=False, na=False)
        ]
        
        if not filtered_df.empty:
            st.dataframe(filtered_df)
        else:
            st.warning("No matching patient found.")

# -----------------------
# Upload Medical Reports
elif menu == "Upload Reports":
    st.subheader("📂 Upload Medical Reports")
    
    uploaded_file = st.file_uploader("Upload a medical report (PDF, JPG, PNG)", type=["pdf", "jpg", "png"])
    
    if uploaded_file:
        st.success(f"✅ File '{uploaded_file.name}' uploaded successfully!")

# -----------------------
# Footer
st.markdown("---")
st.markdown("📌 **Built with Streamlit** | 🏥 Patient Management System")
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/swaheed15/Patient Registration.git
git push -u origin main