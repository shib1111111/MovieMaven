import streamlit as st
from imdb import IMDb

# Initialize the IMDb module
ia = IMDb()

# Set up the Streamlit app
st.title('IMDb Movie Details')
st.write('Enter a movie title (e.g. "The Godfather")')
movie_title = st.text_input('', '')

# Handle the search button click
if st.button('Search'):
    # Search for the movie by title
    movie = ia.search_movie(movie_title)[0]
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
    for person in movie['cast'][:10]:
        st.write(person)

    # Display the top 5 recommendations (if available)
    if 'recommendations' in movie:
        st.write('**Top 5 Recommendations:**')
        for i, recommendation in enumerate(movie['recommendations'][:5]):
            st.write(f'{i+1}. {recommendation["title"]} ({recommendation["year"]})')
    else:
        st.write('**Recommendations:** N/A')
