import streamlit as st

def show():
    st.title("About Us")
    st.write("""
### **Project Scope**
An application that can be used by households to understand the 3Rs (Recycle, Reuse, Reduce) and how to apply them in daily life.
This will be a useful platform to build a function for households to recycle and earn reward points for doing so.

### **Objectives**
To make the 3Rs (Recycle, Reuse, Reduce) an engaging and rewarding experience for households! 😊

### **Features**
There are 5 features in the 3Rs (Recycle, Reuse, Reduce) App for Households:
- Blue Recycling Bin Checker 🔵
- RAG Chatbot on 3Rs Practices for Household ♻️
- RAG Chatbot on Reducing Food Wastage & Saving Money 🥗💰
- Recipe Suggestion for your Food Excesses 🥗💰
- Waste Generated and Waste Recycling Statistics ♻️📊

### **Data Sources**
""")

    st.markdown("[Waste Minimisation and Recycling at Home](https://www.nea.gov.sg/our-services/waste-management/3r-programmes-and-resources/waste-minimisation-and-recycling/at-home)")
    st.markdown("['The 3Rs': A Guide to 3R Practices for Households](https://www.nea.gov.sg/docs/default-source/our-services/a-guide-to-3r-practices-for-households.pdf)")
    st.markdown("['Love Your Food': A Guide to Reducing Food Wastage and Saving Money](https://www.nea.gov.sg/docs/default-source/envision/food-waste/love-your-food-handy-guide.pdf)")
    st.markdown("['Waste Statistics and Overall Recycling](https://www.nea.gov.sg/our-services/waste-management/waste-statistics-and-overall-recycling)")

# Call the show function to run the app
if __name__ == "__main__":
    show()
