# imports
import streamlit as st
from frontend_modules import layouts, users

## configure page
st.set_page_config(
    page_title="SHIELD",
    page_icon=":shield:",
)


# define main function
def main():

    ## initialize authentication state
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    ## if user has been authenticated, grant access to corresponding content
    if st.session_state["authenticated"] == True:
        if st.session_state["admin"] == 2:
            layouts.admin()
        else:
            layouts.non_admin()
    ## else, show login page
    else:
        users.login()


# if file is executed as script
if __name__ == "__main__":

    ## run main function
    main()
