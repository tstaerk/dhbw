import os
import streamlit as st
st.write("Streamlit version:", st.__version__)
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage

# Set your OpenAI API key (you can also load it from a .env file)
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# Initialize the LangChain chat model (using GPT-3.5 Turbo in this example)
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

# Initialize conversation history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("LangChain Chatbot")

# Input box for the user's message
user_input = st.text_input("You:", "")

if st.button("Send") and user_input:
    # Append the user's message to the conversation history
    st.session_state.chat_history.append(HumanMessage(content=user_input))

    # Generate a response from the LLM using LangChain
    response = llm.invoke([HumanMessage(content=user_input)])

    # Append the LLM's response to the conversation history
    st.session_state.chat_history.append(response)

    # Rerun to update the display
    import random
    st.experimental_set_query_params(rerun=str(random.random()))


# Display the conversation history
for message in st.session_state.chat_history:
    if message.__class__.__name__ == "HumanMessage":
        st.markdown(f"**You:** {message.content}")
    else:
        st.markdown(f"**LLM:** {message.content}")
