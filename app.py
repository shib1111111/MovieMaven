import streamlit as st
from imdb import IMDb

# Initialize the IMDb module
ia = IMDb()

# Set up the Streamlit app
st.set_page_config(page_title='IMDb Movie Details', page_icon=':clapper:', layout='wide')
st.title('IMDb Movie Details')
st.write('Enter a movie title (e.g. "The Godfather")')
movie_title = st.text_input('', '')

# Handle the search button click
if st.button('Search'):
    # Search for the movie by title
    movies = ia.search_movie(movie_title)

    # Display search results
    if not movies:
        st.write('No results found.')
    else:
        st.write(f'Search results for "{movie_title}":')
        for i, movie in enumerate(movies[:10]):
            st.write(f'{i+1}. {movie["title"]} ({movie["year"]})')
        
        # Prompt user to select a movie
        movie_index = st.selectbox('Select a movie:', [str(i+1) for i in range(min(10, len(movies)))])
        movie = movies[int(movie_index)-1]
        ia.update(movie)

        # Display the movie details
        st.write('---')
        st.write(f'**Title:** {movie["title"]}')
        st.write(f'**Year:** {movie["year"]}')
        st.write(f'**Genres:** {", ".join(movie["genres"])}')
        st.write(f'**Rating:** {movie.get("rating", "N/A")}')
        if 'plot' in movie:
            st.write(f'**Plot:** {movie["plot"][0]}')
        else:
            st.write('**Plot:** N/A')
        st.write('---')
        
        # Get recommended movies
        recommendations = ia.get_movie_recommendations(movie.getID())
        if not recommendations:
            st.write('No recommendations found.')
        else:
            st.write('Recommended movies:')
            for i, rec in enumerate(recommendations[:10]):
                st.write(f'{i+1}. {rec["title"]} ({rec["year"]})')
