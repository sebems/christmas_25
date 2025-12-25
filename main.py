import streamlit as st

pg = st.navigation([
    st.Page("./pages/Home.py", title="Home", icon="🎄", default = True),
    st.Page("./pages/Family.py", url_path="family"),
    st.Page("./pages/Friends.py", url_path="friends"),
])
pg.run()