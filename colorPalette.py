import streamlit as st
import openai
from dotenv import dotenv_values
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
import json




secret_key = dotenv_values('.env')['OPEN_AI_API_KEY']
openai.api_key = st.secrets.secret_key

def display_colors(color_list):
    color_block = "".join([f'<div style="background-color: {color}; height: 400px; width: 100px; display: inline-block; margin-right: -4px;"></div>' for color in color_list])
    st.markdown(color_block, unsafe_allow_html=True)

@st.cache_data
def get_and_render_colors(msg):
  prompt = f"""
  You are a color palette generating assistant that responds to text prompts for color palettes.
  You should generate color palettes that fits the theme, mood or instructions in the prompt. 
  The palette should be between 2 and 8 colors. 

  Q: Shades of grey
  A: ['#D3D3D3','#A9A9A9','#696969','#2F4F4F','#000000','#808080','#C0C0C0','#F5F5F5']

  Q: Sunset color theme
  A: ['#243485','#572b9f','#9537a1','#d05379','#ff7552']

  Desired format: a JSON array of hexadecimal color codes
  Q: Convert the following verbal desciption of color palette in to list of colors: {msg}
  A:
  """
  response = openai.Completion.create(
    model = 'text-davinci-003',
    # model = 'gpt-3.5-turbo-instruct',
    prompt = prompt,
    max_tokens = 1250,
    echo = False
    # stop = 'Chatbot'
  )
  result = response['choices'][0]['text']
  color_list = json.loads(result.replace("'",'"'))
  return color_list





st.title('Color Palettes Generator.. 🌈!!')
st.write('---')
st.write('The app generates the color pallete that you ask for..')
st.info(
   """
**Some Examples to try out..**\n
Google Product Colors\n
Pastel colors\n
Vintage pallete\n
"""
)
vInput = st.text_input('Enter prompts for Color palette','Italian delight')
color_list = get_and_render_colors(vInput)
display_colors(color_list)
