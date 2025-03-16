import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA

# to get this running,
# start a venv: python -m venv venv; source venv/bin/activate
# set the environment variable OPENAI_API_KEY to your openai api_key
# put the PDF you want to examine into your_pdf.pdf
# run pip install langchain-openai langchain-community pypdf faiss-cpu
# run the program with the command python rag.py

def create_retrieval_chain(pdf_path, openai_api_key):
    """Creates and returns a RetrievalQA chain."""
    try:
        os.environ["OPENAI_API_KEY"] = openai_api_key

        loader = PyPDFLoader(pdf_path)
        documents = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        texts = text_splitter.split_documents(documents)

        embeddings = OpenAIEmbeddings()

        vectorstore = FAISS.from_documents(texts, embeddings)

        llm = ChatOpenAI()
        qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever())

        return qa

    except Exception as e:
        print(f"Error creating retrieval chain: {e}")
        return None

if __name__ == "__main__":
    pdf_file = "your_pdf.pdf"
    api_key = os.getenv("OPENAI_API_KEY")

    if os.path.exists(pdf_file) and api_key != "YOUR_OPENAI_API_KEY":
        qa_chain = create_retrieval_chain(pdf_file, api_key)

        if qa_chain: #if chain was created successfully.
            while True:
                user_query = input("Ask a question about the PDF (or press Enter to exit): ")

                if user_query == "":
                    print("Exiting...")
                    break

                result = qa_chain.invoke(user_query)['result']
                print(f"Answer: {result}")
        else:
            print("Error: Retrieval chain could not be created.")

    elif not os.path.exists(pdf_file):
        print(f"Error: PDF file '{pdf_file}' not found.")
    else:
        print("Error: Please replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key.")
