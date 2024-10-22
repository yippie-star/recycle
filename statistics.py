import streamlit as st
import pandas as pd
import plotly.express as px

def show():
    st.markdown("<h1 style='color: blue;'>Waste Generated and Waste Recycling Statistics</h1>", unsafe_allow_html=True)

    # Raw URL of the Excel file on GitHub
    file_url = "https://raw.githubusercontent.com/yippie-star/recycle/main/waste_recycling_2013_2023.xlsx"

    # Read the Excel file
    try:
        data = pd.read_excel(file_url, engine='openpyxl')
        data.columns = data.columns.str.strip().str.replace('\xa0', '', regex=True)

        # Display the charts
        if 'Year' in data.columns and 'Waste_Generated' in data.columns:
            fig = px.line(data, x='Year', y='Waste_Generated', title='Waste Generated (tonnes) from 2013 to 2023')
            st.plotly_chart(fig)

        if 'Waste_Recycled' in data.columns:
            fig2 = px.line(data, x='Year', y='Waste_Recycled', title='Waste Recycled (tonnes) from 2013 to 2023')
            st.plotly_chart(fig2)

        # Use Markdown to make the prompt larger
        st.markdown("<h5 style='text-align: left;'>Ask a question about the data from 2013 to 2023 (max 300 characters):</h5>", unsafe_allow_html=True)

        # User input for asking questions with a character limit
        user_question = st.text_input("", max_chars=300)

        # Add a button to return the response
        if st.button("Return Response"):
            # Function to handle complex queries
            def answer_question(question):
                question = question.lower().strip()  # Strip whitespace
                if not question:
                    return "Please enter a question."

                if "total" in question:
                    total_generated = data['Waste_Generated'].sum()
                    total_recycled = data['Waste_Recycled'].sum()
                    return f"The total waste generated is: {total_generated}, and the total waste recycled is: {total_recycled}."
                
                elif "average" in question:
                    avg_generated = data['Waste_Generated'].mean()
                    avg_recycled = data['Waste_Recycled'].mean()
                    return f"The average waste generated per year is: {avg_generated:.2f}, and the average waste recycled per year is: {avg_recycled:.2f}."

                elif "max" in question:
                    max_generated_year = data.loc[data['Waste_Generated'].idxmax(), 'Year']
                    max_generated_value = data['Waste_Generated'].max()
                    return f"The maximum waste generated was {max_generated_value} in the year {max_generated_year}."
                
                elif "year" in question:
                    return f"The available years in the data are: {data['Year'].unique()}."

                else:
                    return "I'm sorry, I can only answer questions about totals, averages, maximums, or available years."

            # Process the user question and display the answer
            response = answer_question(user_question)
            st.write(response)

    except Exception as e:
        st.error(f"Error reading the Excel file: {e}")

# Call the show function to run the app
if __name__ == "__main__":
    show()
