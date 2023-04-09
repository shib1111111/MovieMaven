import streamlit as st
from imdb import IMDb

# Initialize the IMDb module
ia = IMDb()

# Set up the Streamlit app with Bootstrap styling
st.set_page_config(page_title='Movie details', page_icon=':movie_camera:', layout='wide')
st.markdown('<link rel="stylesheet" type="text/css" href="./style.css">', unsafe_allow_html=True)

# Display the title and search box
st.write('<h1 style="text-align:center;font-size:48px;font-weight:bold;font-family:Helvetica,Arial,sans-serif;margin-top:50px;margin-bottom:50px;">IMDb Movie Details</h1>', unsafe_allow_html=True)
movie_title = st.text_input('Enter a movie title (e.g. "The Godfather")', '')

# Handle the search button click with color change
if st.button('Search', key='search_button'):
    with st.spinner('Searching...'):
        # Search for the movie by title
        movie = ia.search_movie(movie_title)[0]
        ia.update(movie)

        # Display the movie details
        st.write(f'<h2 style="font-size:32px;font-weight:bold;font-family:Helvetica,Arial,sans-serif;margin-top:50px;margin-bottom:25px;">{movie["title"]} ({movie["year"]})</h2>', unsafe_allow_html=True)
        st.write('<div class="details-heading">Movie details:</div>', unsafe_allow_html=True)
        col1, col2 = st.columns([1, 3])
        with col1:
            st.write('**Rating:**')
            st.write('**Genres:**')
            st.write('**Plot:**')
            st.write('**Top 10 Cast Members:**')
            st.write('**Top 5 Recommendations:**')
        with col2:
            st.write(movie['rating'])
            st.write(', '.join(movie['genres']))
            if 'plot' in movie:
                st.write(movie['plot'][0])
            else:
                st.write('N/A')
            for i, person in enumerate(movie['cast'][:10]):
                st.write(f'<div class="cast-name">{i+1}. {person}</div>', unsafe_allow_html=True)
            if 'recommendations' in movie:
                for i, recommendation in enumerate(movie['recommendations'][:5]):
                    st.write(f'{i+1}. {recommendation["title"]} ({recommendation["year"]})')
            else:
                st.write(' ')

# Display the signature
st.sidebar.markdown('<div class="signature">Created by Shibkumar</div>', unsafe_allow_html=True)
