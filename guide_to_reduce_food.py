# 3R Practices Guide
import streamlit as st
import requests
import toml
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.schema import Document
import tiktoken

def show():
    # Load secrets
    openai_api_key = secrets["openai"]["api_key"]

    # Function to load documents from GitHub
    def load_documents_from_github(file_urls):
        documents = []
        for url in file_urls:
            raw_url = url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
            response = requests.get(raw_url)
            if response.status_code == 200:
                documents.append(Document(page_content=response.text, metadata={"source": url}))
            else:
                st.warning(f"Failed to fetch document from {url}")
        return documents

    # Example list of raw GitHub file URLs
    file_urls = ["https://github.com/yippie-star/recycle/blob/main/guide_to_reduce_food_waste.txt"]

    # Load documents
    documents = load_documents_from_github(file_urls)

    if not documents:
        st.error("No documents loaded. Please check the URLs.")
        return

    # Set up embeddings and vector store
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    vector_store = FAISS.from_documents(documents, embeddings)

    # Set up the language model and RetrievalQA chain
    llm = OpenAI(openai_api_key=openai_api_key)
    retrieval_qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vector_store.as_retriever())

    st.markdown("<h1 style='color: #FF69B4;'>Guide to Reducing Food Wastage & Saving Money</h1>", unsafe_allow_html=True)

    # User input for the prompt with character limit
    max_prompt_length = 300
    user_prompt = st.text_area("What do you want to know about Reducing Food Wastage & Saving Money? (max 300 characters):", "", max_chars=max_prompt_length)

    # Button to submit the prompt
    if st.button("Get Response"):
        if user_prompt:
            encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
            prompt_tokens = len(encoding.encode(user_prompt))
            token_limit = 256
            
            if prompt_tokens > token_limit:
                st.error(f"Prompt exceeds {token_limit} tokens. Please shorten it.")
            else:
                retrieved_docs = retrieval_qa.retriever.get_relevant_documents(user_prompt)[:3]
                combined_content = "\n".join(doc.page_content for doc in retrieved_docs)

                total_tokens = len(encoding.encode(user_prompt + "\n" + combined_content))
                max_tokens = 4096
                
                if total_tokens > max_tokens:
                    st.warning("The combined prompt and document context is too long. Please try a shorter prompt.")
                else:
                    response = retrieval_qa.run(user_prompt + "\n" + combined_content)
                    st.subheader("Response:")
                    st.write(response)
        else:
            st.error("Please enter a prompt.")

# Call the show function to run the app
if __name__ == "__main__":
    show()