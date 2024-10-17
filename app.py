import streamlit as st
st.write('안녕하세요.')
st.write('안녕하세요.')
st.write('안녕하세요.')
st.write('안녕하세요.')
st.image('Funny_Dog_H.png')
st.video('https://www.youtube.com/watch?v=lPAu7VAFaME')
st.link_button('네이버', 'https://www.naver.com')

import pandas as pd
df = pd.read_csv("InkjetDB_preprocessing.csv")
st.line_chart(df, x='Viscosity',y='Velocity')
st.scatter_chart(df, x='Viscosity',y='Velocity')