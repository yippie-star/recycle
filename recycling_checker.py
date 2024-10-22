import streamlit as st

# Function to show the application
def show():
    # Recycling Checker
        st.markdown("<h1 style='color: blue;'>Blue Recycling Bin Checker</h1>", unsafe_allow_html=True)
        st.write("Type an item to check if it's okay for the blue recycling bin")

        # Function to load items from a file
        def load_items(filename):
            with open(filename, 'r') as file:
                return [line.strip().lower() for line in file.readlines()]

        # Load items
        ok_items = load_items('ok_items.txt')

        # User input
        user_query = st.text_input("Enter an item:")
        submit_button = st.button("Check")

        # Process the input
        if submit_button:
            item = user_query.lower().strip()
            if item in ok_items:
                st.success(f"{item.title()} is okay for the blue recycling bin!")
            else:
                st.warning("Item not found. Please check the [NEA website](https://www.nea.gov.sg/docs/default-source/our-services/waste-management/list-of-items-that-are-recyclable-and-not.pdf) for more info.")

        # Examples section
        st.subheader("Examples of Common Items")
        st.write("### OK for Blue Recycling Bin:")
        st.write("Clean Cardboard Box, Newspaper, Beverage Can, Plastic Beverage Bottle")
        st.write("### Not OK for Blue Recycling Bin:")
        st.write("Batteries, Power Banks, ICT Equipment")

# Call the show function to run the app
if __name__ == "__main__":
    show()
