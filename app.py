import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage

# Initialize chat model
llm = ChatOpenAI(model_name="gpt-3.5-turbo")

st.title("LangChain Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Use the new chat_input
user_input = st.chat_input("Type your message...")

if user_input:
    # Display user message
    st.session_state.messages.append(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.write(user_input)

    # Get response
    response = llm.invoke([HumanMessage(content=user_input)])
    st.session_state.messages.append(response)

    # Display LLM response
    with st.chat_message("assistant"):
        st.write(response.content)
