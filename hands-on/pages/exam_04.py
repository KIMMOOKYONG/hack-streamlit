import streamlit as st

def app():
    st.sidebar.title("this is sidebar")
    st.sidebar.checkbox("체크박스에 표시될 문구")

    code = '''
    import streamlit as st
    st.sidebar.title('this is sidebar')
    st.sidebar.checkbox('체크박스에 표시될 문구')
    '''
    st.code(code, language="python")
