import streamlit as st
st.set_option("theme", "light")

# Set up the Streamlit app
st.set_page_config(
    page_title="Movie Details",
    page_icon=":movie_camera:",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# Add custom CSS
st.markdown(
    f"""
    <style>
        body {{
            background-color: {background_color};
            color: {font_color};
        }}
        .stButton button, .stTextInput input {{
            background-color: {primary_color} !important;
            border-color: {primary_color} !important;
            color: #fff !important;
        }}
        .stButton:hover button, .stTextInput:hover input {{
            background-color: #2c6db8 !important;
            border-color: #2c6db8 !important;
            color: #fff !important;
        }}
        .stButton:active button {{
            background-color: #ff4d4d !important;
            border-color: #ff4d4d !important;
        }}
        .stImage {{
            float: left;
            margin-right: 1rem;
        }}
        .movie-details {{
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: flex-start;
            height: 100%;
        }}
        .movie-details h2 {{
            margin-top: 0;
        }}
        @media (max-width: 768px) {{
            .stImage {{
                float: none;
                margin-right: 0;
                margin-bottom: 1rem;
            }}
            .movie-details {{
                align-items: center;
            }}
        }}
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
        col1, col2 = st.columns([3, 5])
        with col1:
            st.image(movie['full-size cover url'], use_column_width=True)
        with col2:
            st.markdown(f"<h2 class='movie-details'>{movie['title']} ({movie['year']})</h2>", unsafe_allow_html=True)
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
