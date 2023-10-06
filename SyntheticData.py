import streamlit as st
from faker import Faker
import random
import numpy as np
import pandas as pd

st.set_page_config(layout='wide')
fake = Faker()

if 'entries' not in st.session_state:
    st.session_state.entries = []
if 'vProcessing' not in st.session_state:
    st.session_state.vProcessing = False 

dataOptions = ['Name','SSN','Email','Country','Free Text','URL','DOB','Gender','IP Address','Age','LatLong']
dataOptions.sort()

def getRandomData(dataType, vRows):
    if dataType == 'Name':
        return [fake.name() for _ in range(vRows)]
    elif dataType == 'SSN':
        return [fake.ssn() for _ in range(vRows)]
    elif dataType == 'Email':
        return [fake.email() for _ in range(vRows)]
    elif dataType == 'Country':
        return [fake.country() for _ in range(vRows)]
    elif dataType == 'Free Text':
        return [fake.text() for _ in range(vRows)]
    elif dataType == 'URL':
        return [fake.url() for _ in range(vRows)]
    elif dataType == 'DOB':
        return [fake.date_of_birth() for _ in range(vRows)]
    elif dataType == 'Gender':
        return np.random.choice(['M','F'],size=(vRows))
    elif dataType == 'IP Address':
        return [fake.ipv4_private() for _ in range(vRows)]
    elif dataType == 'Age':
        return np.random.randint(0,100,vRows)
    elif dataType == 'LatLong':
        return [f"({fake.latitude()},{fake.longitude()})" for _ in range(vRows)]
    else:
        return [np.random.randint(1,10) for _ in range(vRows)]


def getHelpText(dataType):
    if dataType == 'Name':
        return 'Customer Name'
    elif dataType == 'SSN':
        return 'Social Security Number'
    else:
        return ''

st.header('Synthetic Data Generator 🧪')
st.write('----')
st.write('App to cookup data.. 👩‍🍳')


mastercol1, mastercol2 = st.columns(2)

with mastercol2:
    st.write('Table Schema 📑')
    st.write('----')
    if len(st.session_state.entries) == 0:
        st.write('<span style="color: gray;">Table Schema goes here...</span>', unsafe_allow_html=True)
        
    else:
        col1, buff, col2, col3 = st.columns([1,0.25,1,0.5])
        col1.subheader('Column Name')
        col2.subheader('Column Type')
        col3.subheader('      ')
        for idx, entry in enumerate(st.session_state.entries):
            col1.markdown(f"##### {entry.get('columnName')}")
            col2.markdown(f"##### {entry.get('columnType')}")
            # col2.text(entry.get('columnType'))
            # if col3.button('Delete',key='Delete'+str(idx)):
            #     del st.session_state.entries[idx]
            #     st._experimental_rerun()
            
        st.write('----')    
        if st.button('Clear All 🧹'):
            st.session_state.entries = []
            st._experimental_rerun()




with mastercol1:
    with st.expander(label='Add Columns ➕', expanded=False):
        with st.form(key='Add Columns', clear_on_submit=True):
            vColumnName = st.text_input('Column Name')
            vColumnType = st.selectbox('Select Data Domain',dataOptions,index=None)
            # if vColumnType != '':
            #     st.info(getHelpText(vColumnType))
            if st.form_submit_button('Save'):
                if vColumnName != '' and vColumnType != '':
                    buttonDict = {
                        'columnName': vColumnName,
                        'columnType':vColumnType
                    }
                    st.session_state.entries.append(buttonDict)
                    st.toast('Column Added ✔')
                    st.experimental_rerun()
                    
_, recs = st.columns([5,1])
vRows = recs.selectbox('Number of Rows',np.linspace(5,500,100,dtype=np.int32))

df = pd.DataFrame()

for entry in st.session_state.entries:
    k = entry.get('columnName')
    v = getRandomData(entry.get('columnType'), vRows)
    df[k] = v

st.subheader('Sample Records 📖')
st.write(df)

if len(df)>0:
    csv = df.to_csv(index=False)
    st.download_button(
        label='Download CSV',
        data=csv,
        file_name='Synthetic.csv',
        key='download-button'
        )

# st.write(st.session_state)