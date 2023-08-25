import streamlit as st

# Custom imports 
from multipage import MultiPage
# import your pages here
from pages import exam_01

# Create an instance of the app 
app = MultiPage()

# Title of the main page
st.title("Data Storyteller Application")

# Add all your applications (pages) here
app.add_page("Upload Data", exam_01.app)

# The main app
app.run()
