import streamlit as st
from transformers import pipeline 

st.header('Sentimental Analysis 😊😟')

@st.cache_data
def get_model():
    return pipeline("sentiment-analysis")

classifier = get_model()

vSentence = st.text_input('Enter text to predict sentiment...')
st.write(vSentence)
if vSentence is not None or vSentence == '':
    result = classifier(vSentence)[0]
    if result['label'] == 'POSITIVE':
        st.success(f"😀 Positive Sentence.. ")
    else:
        st.error(f"😟 Negative Sentence..")

st.write("""
**Examples:**\n
I love this product. It's amazing!\n
This movie is terrible. I can't stand it.
""")