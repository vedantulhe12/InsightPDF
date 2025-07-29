import streamlit as st
from utils.pdf_helper import extract_text_from_pdf
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
import os

# 👉 Set your API key securely
openai_api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="PDF Insight Agent")
st.title("📄🤖 PDF Insight Agent")

uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)

    # Split text into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_text(text)

    # Embeddings + Vector DB
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    vectordb = FAISS.from_texts(chunks, embedding=embeddings)

    # LLM
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectordb.as_retriever())

    # Ask a question
    query = st.text_input("Ask a question about the PDF:")

    if query:
        with st.spinner("Thinking..."):
            result = qa_chain.run(query)
        st.markdown("**Answer:**")
        st.success(result)
