import streamlit as st

st.write("Streamlit version:", st.__version__)
import google.generativeai as ai
import os

# This program lets AI tell a joke
# It is useful not only to put a smile on your face, but also to check if you have set up libraries and API keys correctly
# It expects to find an operating system environment variable API_KEY containing the API key.

ai.configure(api_key=os.environ['API_KEY'])
model = ai.GenerativeModel("gemini-2.0-flash-001") # to find out what models are available, go to https://console.cloud.google.com -> vertex AI -> freeform and have a look at the right-hand-side panel which has a selection for "Model"

st.write(model.generate_content("tell a random joke").candidates[0].content.parts[0].text)
