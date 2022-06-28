# App file

# ----- Imports -----
import os
import streamlit

import pandas as pd


# ----- Main code -----
# Variables
PATH = os.getcwd()

# Read fruits list
my_fruits_list = pd.read_csv(PATH + ".\resources\fruit_macros.csv")


# ----- Main display -----
streamlit.title("My Parents New Healthy Diner")

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text(" 🥑🍞 Avocado Toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.dataframe(my_fruits_list)