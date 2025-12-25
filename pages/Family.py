import streamlit as st

st.set_page_config(page_title = "Family")


friends = open("family.md", "r")
st.markdown(friends.read())