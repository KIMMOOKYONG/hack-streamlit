import numpy as np
import pandas as pd 
import streamlit as st

def app():

    iris_dataset = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"

    df= pd.read_csv(iris_dataset)
    df.columns= [ col_name.split(' (cm)')[0] for col_name in df.columns] # 컬럼명을 뒤에 cm 제거하였습니다

    st.subheader("this is table")
    st.table(df.head())

    st.subheader("this is data frame")
    st.dataframe(df.head())

    code = '''
        import numpy as np
        import pandas as pd 
        import streamlit as st

        iris_dataset = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"

        df= pd.read_csv(iris_dataset)
        df.columns= [ col_name.split(' (cm)')[0] for col_name in df.columns] # 컬럼명을 뒤에 cm 제거하였습니다

        st.subheader("this is table")
        st.table(df.head())

        st.subheader("this is data frame")
        st.dataframe(df.head())
    '''
    st.code(code, language="python")


