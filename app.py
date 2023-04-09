import streamlit as st

# Set up the Streamlit app
st.set_page_config(page_title="Movie Details", page_icon=":movie_camera:", layout="wide")

# Add custom CSS
st.markdown(
    """
    <style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #333;
        background-color: #f5f5f5;
    }
    .stButton button, .stTextInput input {
        background-color: #4285F4 !important;
        border-color: #4285F4 !important;
        color: #fff !important;
    }
    .stButton:hover button, .stTextInput:hover input {
        background-color: #2c6db8 !important;
        border-color: #2c6db8 !important;
        color: #fff !important;
    }
    .stButton:active button {
        background-color: #ff4d4d !important;
        border-color: #ff4d4d !important;
    }
    .container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 20px;
    }
    .row {
        display: flex;
        flex-wrap: wrap;
        margin: 0 -10px;
    }
    .col {
        flex: 1;
        padding: 0 10px;
    }
    @media screen and (max-width: 768px) {
        .col {
            flex: 100%;
            padding: 0;
        }
    }
</style>

    """,
    unsafe_allow_html=True
)

# Display the app title and input field
st.title('Movie Details')
st.write('Enter a movie title (e.g. "The Godfather")')
movie_title = st.text_input('', '')

# Handle the search button click
if st.button('Search'):
    with st.spinner('Searching for movie...'):
        # Initialize the IMDb module
        from imdb import IMDb
        ia = IMDb()

        # Search for the movie by title
        movie = ia.search_movie(movie_title)[0]
        ia.update(movie)

        # Display the movie details
        col1, col2 = st.columns(2)
        col1.image(movie['full-size cover url'], use_column_width=True)
        with col2:
            st.write('**Title:**', movie['title'])
            st.write('**Year:**', movie['year'])
            st.write('**Rating:**', movie['rating'])
            st.write('**Genres:**', ', '.join(movie['genres']))
            if 'plot' in movie:
                st.write('**Plot:**', movie['plot'][0])
            else:
                st.write('**Plot:** N/A')

        # Display the top 10 cast members
        st.write('**Top 10 Cast Members:**')
        cast = movie['cast'][:10]
        for member in cast:
            st.write(member)

        # Display recommendations, if available
        if 'recommendations' in movie:
            st.write('**Top 5 Recommendations:**')
            for i, recommendation in enumerate(movie['recommendations'][:5]):
                st.write(f'{i+1}. {recommendation["title"]} ({recommendation["year"]})')
        else:
            st.write('  ')
