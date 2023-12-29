# app.py
import streamlit as st
from movie_search import search_movie
from styling import add_custom_css
from signature import display_signature
from imdb import IMDb
from recommedation import generate_movie_recommendations
st.set_page_config(
    page_title="MovieMaven",
    page_icon=":movie_camera:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

add_custom_css()

st.title("MovieMaven")
st.write('Enter a movie title (e.g. "The Godfather")')
movie_title = st.text_input("", "")

if st.button("Search"):
    search_movie(movie_title)
    generate_movie_recommendations(movie_title)

display_signature()
