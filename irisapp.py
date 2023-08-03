import streamlit as st
import sys
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Simple Iris Flower Prediction App
This app predicts the Iris flower type..!!
         
         """)

st.sidebar.header('User Input Params')

data = datasets.load_iris()['data']

mins, maxs = data.min(axis=0), data.max(axis=0)


def userInputFeatures():
    sepal_length = st.sidebar.slider('Sepal Length',mins[0],maxs[0], np.mean((mins[0],maxs[0])))
    sepal_width= st.sidebar.slider('Sepal Width',mins[1],maxs[1], np.mean((mins[1],maxs[1])))
    petal_length = st.sidebar.slider('Petal Length',mins[2],maxs[2], np.mean((mins[2],maxs[2])))
    petal_width = st.sidebar.slider('Petal Width',mins[3],maxs[3], np.mean((mins[3],maxs[3])))
    data = {
        'SepalLength':sepal_length,
        'SepalWidth':sepal_width,
        'PetalLength':petal_length,
        'PetalWidth':petal_width
    }
    df = pd.DataFrame(data, index=[0])
    return df

df = userInputFeatures()

st.subheader('User Params')
st.write(df)

X,y = datasets.load_iris()['data'], datasets.load_iris()['target']

clf = RandomForestClassifier()
clf.fit(X,y)

pred = clf.predict(df)
pred_proba = clf.predict_proba(df)
pred_proba_dict = {} 

st.write("""
## Predictions 👓
         """)

for idx, name in  enumerate(datasets.load_iris()['target_names']):
    pred_proba_dict[name] = pred_proba[0,idx]
st.write(
    pd.DataFrame(pred_proba_dict,index=[0])
)
