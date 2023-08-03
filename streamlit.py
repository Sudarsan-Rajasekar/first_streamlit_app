import yfinance as yf
import streamlit as st
import pandas as pd
import sys


st.write(
    """
# Display Simple dataset

Display Wine dataset
"""
)


df = pd.read_csv(r'E:\Data\wine.csv' )
 
st.write(df)

st.line_chart(df['alcohol'])




