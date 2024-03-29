import streamlit
import pandas as pd
import requests 
import snowflake.connector
from urllib.error import URLError

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

# create a function to get fruit info from fruityvice 
def get_fruityvice_data(this_fruit_choice):
    fruitvise_response = requests.get('https://www.fruityvice.com/api/fruit/'+fruit_choice)
    fruit_df = pd.json_normalize(fruitvise_response.json())
    return fruit_df

# new section to display API calls 
streamlit.header('Fruitvise fruit Advice..!!')
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
        streamlit.error('Please enter a fruit to get information')
    else:     
         fruit_df = get_fruityvice_data(fruit_choice)
         streamlit.dataframe(fruit_df)

except URLError as e:
  streamlit.error()






# welcome from snowflake
def get_fruit_load_list():
    with my_cnx.cursor() as mycur:
        mycur.execute("SELECT * FROM FRUIT_LOAD_LIST")
        return mycur.fetchall()


def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as mycur:
        mycur.execute("insert into fruit_load_list values ('"+new_fruit+"')")
        return "Thanks for adding "+new_fruit


streamlit.header('View our fruit list and add you favourite...!!')
if streamlit.button('Get fruit list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    data_rows = get_fruit_load_list()
    streamlit.dataframe(data_rows)


add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a fruit to the list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_fn = insert_row_snowflake(add_my_fruit)
    streamlit.write(back_from_fn)
