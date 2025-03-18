#/bin/bash

# This will download an LLM and create a chatbot to query it using llama-cpp

# download Llama LLM
wget -O llama.gguf \
https://huggingface.co/TheBloke/\
Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q5_K_M.gguf?download=true

# install developer tools
sudo apt install g++ git pip python3-venv

# set up venv
python3 -m venv venv
source venv/bin/activate
pip install langchain_community llama-cpp-python

# create chatbot
cat >llm_chatbot.py<<EOF
from langchain_community.llms import LlamaCpp
from langchain.prompts import PromptTemplate
import llama_cpp
from langchain_core.runnables import RunnableSequence

# Load the LlamaCpp language model, adjust GPU usage based on your hardware
llm = LlamaCpp(
    model_path="llama.gguf",
    n_gpu_layers=40,
    n_batch=512,  # Batch size for model processing
    verbose=False,  # Enable detailed logging for debugging
)

# Define the prompt template with a placeholder for the question
template = """
Question: {question}

Answer:
"""
prompt = PromptTemplate(template=template, input_variables=["question"])

# Create the RunnableSequence
chain = prompt | llm

print("Chatbot initialized, ready to chat...")
question = input("> ")
while question!="":
    answer = chain.invoke({"question": question})
    print(answer, '\n')
    question = input("> ")
EOF
