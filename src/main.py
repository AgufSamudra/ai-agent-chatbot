import streamlit as st
from streamlit import session_state as ss

if "chat" not in ss:
    ss["chat"] = []


with st.sidebar:
    select_role = st.selectbox("Choose Role",
                               ["Customer Service",
                                "Docter",
                                "Teacher"])
    
    button_select_role = st.button("Submit", type="primary")
    

prompt = st.chat_input("Input Here")
if prompt:
    pass