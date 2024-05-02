import streamlit as st
import json
import requests


st.title('Test App')

text = st.text_input("Type your name")

text_input_dict = {'name':text}

if text:
    res = requests.post(url ="http://backend:8000/print", data = json.dumps(text_input_dict) )
    st.write(res.text)