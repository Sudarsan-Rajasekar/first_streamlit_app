from sklearn.datasets import load_iris
import streamlit as st
import pandas as pd

st.write("""
# My First app
Display iris data as a line chart 
         """)

data = pd.DataFrame(load_iris()['data'])
st.line_chart(data.iloc[:,0])
