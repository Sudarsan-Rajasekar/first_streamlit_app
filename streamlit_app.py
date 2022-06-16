import streamlit
import pandas as pd
import requests 
import snowflake.connector
from urlib.error import URLError

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
streamlit.header('Fruitvise fruit Advice..!!')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error('Please enter a fruit to get information')
  else:      
  streamlit.write('User Entered: ',fruit_choice)
  fruitvise_response = requests.get('https://www.fruityvice.com/api/fruit/'+fruit_choice)
except URLError as e:
  streamlit.error()

streamlit.stop()

# raw data 
streamlit.text(fruitvise_response.json())
fruit_df = pd.json_normalize(fruitvise_response.json())
streamlit.dataframe(fruit_df)

# welcome from snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
my_data_rows = my_cur.fetchall()
streamlit.text("FRUIT_LOAD_LIST Data:")
streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input('What fruit would you like to add?')
streamlit.write("Thanks for adding ",add_my_fruit,"!")
