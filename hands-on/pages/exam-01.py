import streamlit as st

def app():
    st.title("this is title")
    st.header("this is title")
    st.subheader("this is title")

    code = '''
    st.title("this is title")
    st.header("this is title")
    st.subheader("this is title")
    '''
    st.code(code, language="python")
