import streamlit as st
from PIL import Image

def show():
    # Set the title of the app
    st.title("Methodology")

    # Display the flowchart image
    st.image("flowchart.png", caption="Methodology Flowchart", use_column_width=True)

    # Section for Flowchart Explanation
    st.header("Flowchart Explanation")

    # Blue Recycling Bin Checker
    with st.expander("Blue Recycling Bin Checker"):
        st.write("Objective: To help households identify items suitable for the Blue Recycling Bin and not use it as a dustbin.")
        st.write("We check the user input against the list of 'ok items' and display message if item is suitable for blue recycling bin.")

    # RAG Chatbot on 3R Practices for Household
    with st.expander("RAG Chatbot on 3Rs Practices for Household"):
        st.write("Objective: To enable households to learn about the 3Rs practices in a engaging and conversational manner.")
        st.write("We load the knowledge base, set up the embeddings, vector store, language model and retrievalQA Chain, ensure total tokens from prompt and response do not exceed model limit and return the response to the prompt.")

    # RAG Chatbot on Reducing Food Wastage & Saving Money
    with st.expander("RAG Chatbot on Reducing Food Wastage & Saving Money"):
        st.write("Objective:To enable households to learn about reducing food wastage & saving money in a engaging and conversational manner.")
        st.write("We load the knowledge base, set up the embeddings, vector store, language model and retrievalQA Chain, ensure total tokens from prompt and response do not exceed model limit and return the response to the prompt.")

    # Recipe Suggestion for your Food Excesses
    with st.expander("Recipe Suggestion for your Food Excesses"):
        st.write("Objective: To help households re-purpose their food excesses with the recipe suggestions.")
        st.write("We initialise the LLM, create the prompt template for recipe suggestions, create the LLM chain to execute the prompt with the LLM, run the input prompt to the chain and return the recipe suggestion.")

    # Waste Generated and Waste Recycling Statistics
    with st.expander("Waste Generated and Waste Recycling Statistics"):
        st.write("Objective: To increase awareness of the Waste Generated and Waste Recycling Trends in Singapore") 
        st.write("We read the data and display charts. For data enquiry, users can enter their prompts and if the prompts contain ‘total’, ‘average’, ‘sum’, ‘max’ or ‘year’, the response will be returned accordingly.")

# Call the show function to run the app
if __name__ == "__main__":
    show()
