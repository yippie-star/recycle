import streamlit as st

def show():
    st.title("Home Page")
    st.write("Welcome! Please use the left navigation panel to go to your desired page!")
    with st.expander("Important Notice"):
        st.write("This web application is a prototype developed for educational purposes only.")
        st.write("The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.")
        st.write("Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.")
        st.write("Always consult with qualified professionals for accurate and personalized advice.")


