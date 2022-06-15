import streamlit
import pandas 

streamlit.title("My Parents new healthy dinner")
streamlit.header("Breakfast Favorites")
streamlit.text("🥗 Omega 3 and Blueberry Oat Meal")
streamlit.text("🧃Kale, Spinach and Rocket smoothie")
streamlit.text("🥚 Hard Boiled - Free Range egg")
streamlit.text("🍞🥑 Avocado Toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

df = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(df)

