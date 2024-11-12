import streamlit as st

from zack_practice_package import zack_practice

st.title('Demo: Streamlit')

num = st.text_input('Enter an integer', key = 'number')

if num is not None:
    num = int(num)
    st.write(zack_practice.sum_count(range(num)))