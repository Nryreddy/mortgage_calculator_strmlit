import streamlit as st
import pandas as pd


st.write('Hello there, welcome')
fav_movie = st.text_input('Which is your favourite movie?')

st.write(f"Your favourite movie is {fav_movie}")

