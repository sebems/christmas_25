import streamlit as st

st.set_page_config(page_title = "Friends")


friends = open("friends.md", "r")
st.markdown(friends.read())

st.html(
    """
    <style>
        .moving_img {
        -webkit-transform: scaleX(-1);
        transform: scaleX(-1);
        }
    </style>
    
    <marquee behavior='scroll' direction='right' scrollamount='20'>
        <img class="moving_img" src="https://media.tenor.com/oir5PjIye9sAAAAj/sonic.gif" alt='sonic'">
        <img class="moving_img" src="https://media.tenor.com/Trfy7ALftrgAAAAm/mario.webp" alt='mario'">
        <img class="moving_img" src="https://media.tenor.com/2lFt6lp1KaMAAAAj/run-pokemon.gif" alt='pikachu'">
        <img class="moving_img" src="https://media.tenor.com/b-hHxC3jx_AAAAAj/kirby-spinning.gif" alt='kribo'">
        <img class="moving_img" width="200px" src="https://media.tenor.com/Muy5iqWr9lYAAAAi/santa-claus-santa.gif" alt='santa'">
    </marquee>
    """
)