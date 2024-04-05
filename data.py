import streamlit as st
import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
st.write(data)