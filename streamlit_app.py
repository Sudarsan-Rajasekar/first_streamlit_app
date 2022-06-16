import streamlit
import pandas as pd
import requests 

streamlit.title("My Parents new healthy dinner")
streamlit.header("Breakfast Favorites")
streamlit.text("🥗 Omega 3 and Blueberry Oat Meal")
streamlit.text("🧃Kale, Spinach and Rocket smoothie")
streamlit.text("🥚 Hard Boiled - Free Range egg")
streamlit.text("🍞🥑 Avocado Toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')




df = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
df = df.set_index('Fruit')

# list for the users to pick from 
fruit_selected = streamlit.multiselect("Pick from the list:",list(df.index),['Avocado','Strawberries'])

data = df.loc[fruit_selected]

# display the dataset
streamlit.dataframe(data)

# new section to display API calls 
fruitvise_response = requests.get('https://www.fruityvice.com/api/fruit/watermelon')
streamlit.text(fruitvise_response)
