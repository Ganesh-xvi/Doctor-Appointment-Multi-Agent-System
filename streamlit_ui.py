import streamlit as st
import requests

API_URL = "http://127.0.0.1:8003/execute"  

st.title("🩺 Doctor Appointment System")

query = st.text_area("Enter your query:", "Can you check if a dentist is available tomorrow at 10 AM?")

if st.button("Submit Query"):
    if query:
        try:
            response = requests.post(API_URL, json={'messages': query}, verify=False)
            if response.status_code == 200:
                data = response.json()
                st.success("Response Received:")
                st.write(data["last_message"])
            else:
                st.error(f"Error {response.status_code}: Could not process the request.")
        except Exception as e:
            st.error(f"Exception occurred: {e}")
    else:
        st.warning("Please enter your query.")