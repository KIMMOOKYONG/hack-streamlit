import streamlit as st
from PIL import Image

def app():
    #PIL 패키지에 이미지 모듈을 통해 이미지 열기 
    # Image.open('이미지 경로')

    col1,col2 = st.columns([2,3])
    with col1 :
        # column 1 에 담을 내용
        st.title('here is column1')
    with col2 :
        # column 2 에 담을 내용
        st.title('here is column2')

    # 컬럼2에 불러온 사진 표시하기
    col2.image("https://s3-us-west-2.amazonaws.com/uw-s3-cdn/wp-content/uploads/sites/6/2017/11/04133712/waterfall.jpg", width=400)

    code = '''
    import streamlit as st
    from PIL import Image

    col1,col2 = st.columns([2,3])

    with col1 :
        # column 1 에 담을 내용
        st.title('here is column1')
    with col2 :
        # column 2 에 담을 내용
        st.title('here is column2')
        st.checkbox('this is checkbox1 in col2 ')


    # 컬럼2에 불러온 사진 표시하기
    col2.image("https://s3-us-west-2.amazonaws.com/uw-s3-cdn/wp-content/uploads/sites/6/2017/11/04133712/waterfall.jpg", width=400)
    '''
    st.code(code, language="python")
