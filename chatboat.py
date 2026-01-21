import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain

OPEN_API_KEY = "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"

# Upload PDF files
st.header("First Chatbot")

with st.sidebar:
    st.title("Your Documents")
    file=st.file_uploader("Upload PDF file and start asking questions", type="pdf")

#Extract the text
if file is not None:
    pdf_reader = PdfReader(file)
    text=""
    for page in pdf_reader.pages:
        text += page.extract_text()
        # st.write(text)

#Break it into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", " ", ""],
        chunk_size=1000,
        length_function=len,
        chunk_overlap=200
        
    )
    chunks = text_splitter.split_text(text)
    # st.write(chunks)

    # generating embeddings
    embeddings = OpenAIEmbeddings(openai_api_key=OPEN_API_KEY)


    #creating vector store -FAISS
    vector_store = FAISS.from_texts(chunks, embeddings)

    # accepting user questions
    user_question = st.text_input("Ask your question here")

    #do similarity search
    if user_question:
        match = vector_store.similarity_search(user_question)
        # st.write(match)

        #define the LLM model
        llm = chatOpenAI(openai_api_key=OPEN_API_KEY, 
        temperature=0,
        max_tokens=1000,
        model_name="gpt-3.5-turbo"
        )

    #output results
        # explain chain -> take the question, get relevant document, pass it to the LLM, generate the output
        chain =load_qa_chain(llm, chain_type="stuff")
        response = chain.run(input_documents=match, question=user_question)
        st.write(response)
