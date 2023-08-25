import numpy as np
import pandas as pd 
import streamlit as st

def app():

    iris_dataset = "https://raw.githubusercontent.com/pandas-dev/pandas/master/pandas/tests/data/iris.csv"

    df= pd.read_csv(iris_dataset)
    df.columns= [ col_name.split(' (cm)')[0] for col_name in df.columns] # 컬럼명을 뒤에 cm 제거하였습니다
    df['species']= iris_dataset.target 


    species_dict = {0 :'setosa', 1 :'versicolor', 2 :'virginica'} 

    def mapp_species(x):
        return species_dict[x]

    df['species'] = df['species'].apply(mapp_species)
    print(df)

    code = '''

    '''
    st.code(code, language="python")
