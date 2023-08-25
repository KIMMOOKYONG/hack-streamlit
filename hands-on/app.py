import streamlit as st

# Custom imports 
from multipage import MultiPage
# import your pages here
from pages import exam_01, exam_02, exam_03, exam_04
from pages import exam_05

# Create an instance of the app 
app = MultiPage()

# Title of the main page
st.title("Data Storyteller Application")

# Add all your applications (pages) here
app.add_page("강조 문구", exam_01.app)
app.add_page("layout 짜기-column", exam_02.app)
app.add_page("layout 짜기-tab", exam_03.app)
app.add_page("layout 짜기-sidebar", exam_04.app)
app.add_page("이미지 불러오기", exam_05.app)

# The main app
app.run()
