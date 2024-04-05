import streamlit as st


st.write('Hello there, welcome')
fav_movie = st.text_input('Which is your favourite movie?')

st.write(f"Your favourite movie is {fav_movie}")

