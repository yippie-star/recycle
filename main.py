import streamlit as st
import hmac
from home import show as show_home
from recycling_checker import show as show_recycling_checker
from guide_to_3Rs import show as show_guide_to_3Rs
from guide_to_reduce_food import show as show_guide_to_reduce_food
from recipe import show as show_recipe
from statistics import show as show_statistics
from about_us import show as show_about_us
from methodology import show as show_methodology

# Define the password check function (same as before)
def check_password():
    def password_entered():
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if st.session_state.get("password_correct", False):
        return True

    st.text_input("Password", type="password", on_change=password_entered, key="password")
    if "password_correct" in st.session_state and not st.session_state["password_correct"]:
        st.error("😕 Password incorrect")

    return False

# Main app logic
def main():
    if check_password():
        st.write("The 3R (Recycle, Reuse, Reduce) App for Households")
        st.sidebar.title("Navigation")
        page = st.sidebar.selectbox("Select a page:", ["Home", "Blue Recycling Bin Checker", "Guide to 3Rs Practices", "Guide to Reducing Food Wastage & Saving Money", "Recipe Suggestion for Excess Food", "Statistics", "About Us", "Methodology"])

        if page == "Home":
            show_home()
        elif page == "Blue Recycling Bin Checker":
            show_recycling_checker()
        elif page == "Guide to 3Rs Practices":
            show_guide_to_3Rs()
        elif page == "Guide to Reducing Food Wastage & Saving Money":
            show_guide_to_reduce_food()
        elif page == "Recipe Suggestion for Excess Food":
            show_recipe()
        elif page == "Statistics":
            show_statistics()
        elif page == "Methodology":
            show_methodology()
        elif page == "About Us":
            show_about_us()

        if "password_correct" in st.session_state and st.session_state["password_correct"]:
            if st.button("Logout"):
        # Set the password_correct state to False
                st.session_state["password_correct"] = False
        
        # Remove the password from session state
                st.session_state.pop("password", None)

        # Rerun the app to update the UI
                st.rerun()

if __name__ == "__main__":
    main()

