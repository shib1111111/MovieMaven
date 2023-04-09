import streamlit as st
from imdb import IMDb

# Initialize the IMDb module
ia = IMDb()

# Set up the Streamlit app
st.set_page_config(page_title="IMDb Movie Details", page_icon=":movie_camera:", layout="wide")
st.title('IMDb Movie Details')
st.write('Enter a movie title (e.g. "The Godfather")')
movie_title = st.text_input('', '')

# Handle the search button click
if st.button('Search'):
    # Search for the movie by title
    movie_results = ia.search_movie(movie_title)
    if len(movie_results) == 0:
        st.write("No movies found with that title.")
    else:
        movie = ia.get_movie(movie_results[0].getID())
        ia.update(movie)

        # Display the movie details
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
        for i, person in enumerate(movie['cast'][:10]):
            st.write(f'{i+1}. {person}')

        # Display the top 5 recommendations
        st.write('**Top 5 Recommendations:**')
        for i, recommendation in enumerate(movie['recommendations'][:5]):
            st.write(f'{i+1}. {recommendation["title"]} ({recommendation["year"]})')
