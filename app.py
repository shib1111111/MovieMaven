import streamlit as st
from imdb import IMDb

# Initialize the IMDb module
ia = IMDb()

# Set up the Streamlit app
st.set_page_config(page_title='Movie Details', page_icon=':movie_camera:')
st.title('Movie Details')
st.write('Enter a movie title (e.g. "The Godfather")')

# Define custom CSS styles
st.markdown("""
    <style>
        .stButton button {
            background-color: #5cb85c;
            border-color: #5cb85c;
        }

        .stButton button:hover {
            background-color: #4cae4c;
            border-color: #4cae4c;
        }
        
        .signature {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #666;
            margin-top: 1rem;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

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
        st.write(' ')

# Add signature
st.markdown('<div class="signature">Created by Shibkumar</div>', unsafe_allow_html=True)
