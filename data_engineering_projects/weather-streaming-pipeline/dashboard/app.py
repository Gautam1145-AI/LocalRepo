import streamlit as st
import pandas as pd

st.title('Weather Dashboard')

try:
    df = pd.read_csv('data/weather_data.csv', names=['city','temperature','humidity','timestamp'])
    st.line_chart(df['temperature'])
    st.dataframe(df.tail())
except:
    st.write('No data available yet')
