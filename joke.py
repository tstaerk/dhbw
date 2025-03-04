import streamlit as st

st.write("Streamlit version:", st.__version__)
import google.generativeai as ai
import os

# This program lets AI tell a joke
# It is useful not only to put a smile on your face, but also to check if you have set up libraries and API keys correctly

st.write(os.environ['API_KEY'])
ai.configure(api_key=os.environ['API_KEY'])
model = ai.GenerativeModel("gemini-1.5-pro-002")

st.write(model.generate_content("tell a joke").candidates[0].content.parts[0].text)
