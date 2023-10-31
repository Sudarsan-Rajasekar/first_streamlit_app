import streamlit as st
from transformers import pipeline 

@st.cache_data
def get_model():
    return pipeline("sentiment-analysis")

classifier = get_model()

vSentence = st.text_input('Enter sentimental text here...')

if vSentence is not None or vSentence == '':
    result = classifier(vSentence)[0]
    if result['label'] == 'POSITIVE':
        st.success(f"😀 Positive Sentence.. ")
    else:
        st.error(f"😟 Negative Sentence..")
