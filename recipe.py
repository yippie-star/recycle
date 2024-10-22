import streamlit as st
import openai
import toml
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import tiktoken

def show():
    # Load API key from secrets.toml
    openai_api_key = secrets["openai"]["api_key"]

    # Set up OpenAI API client
    openai.api_key = openai_api_key

    # Initialize LangChain components
    llm = OpenAI(openai_api_key=openai_api_key)
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

    # Define the prompt template for recipe suggestions
    prompt_template = PromptTemplate(
        template="I have the following food items that I want to use: {ingredients}. Can you suggest a recipe based on these ingredients?",
        input_variables=["ingredients"]
    )

    # Create the chain
    recipe_chain = LLMChain(llm=llm, prompt=prompt_template)

    # Streamlit app layout
    st.markdown('<h1 style="color: #FF8C00;">Recipe Suggestion for your Food Excesses!</h1>', unsafe_allow_html=True)
    st.write("Enter the food items you have, and I'll suggest a recipe!")

    # User input for ingredients with a character limit
    user_input = st.text_area("Food excesses (max 300 characters):", max_chars=300)

    if st.button("Get Recipe Suggestion"):
        if len(user_input) > 300:
            st.error("Please enter a shorter input (max 300 characters).")
        elif user_input:
            # Check token count
            prompt_tokens = len(encoding.encode(user_input))
            
            if prompt_tokens > 256:
                st.error("Input exceeds the token limit. Please shorten it.")
            else:
                # Get recipe suggestion
                recipe = recipe_chain.run(ingredients=user_input)
                st.subheader("Recipe Suggestion:")
                st.write(recipe)
        else:
            st.error("Please enter some food items.")

# Call the show function to run the app
if __name__ == "__main__":
    show()
