import streamlit as st

# Add Bootstrap CSS
st.markdown("""
    <style>
        /* Set the background color */
        body {
            background-color: #f8f9fa;
        }

        /* Style the title */
        .title {
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 30px;
        }

        /* Style the search box */
        .search-box {
            margin-bottom: 30px;
        }

        /* Style the search button */
        .search-btn {
            background-color: #007bff;
            color: #fff;
            font-weight: bold;
            border-radius: 5px;
            padding: 10px 20px;
            border: none;
        }

        /* Style the movie details */
        .movie-details {
            margin-top: 30px;
        }

        /* Style the recommendations */
        .recommendations {
            margin-top: 30px;
        }

        /* Style the cast list */
        .cast-list {
            margin-top: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# Set up the Streamlit app
st.title('Movie Details')
st.markdown('<div class="title">Movie Details</div>', unsafe_allow_html=True)

# Add a search box
movie_title = st.text_input('Enter a movie title (e.g. "The Godfather")', '')
st.markdown('<div class="search-box"><input type="text" value="' + movie_title + '"></div>', unsafe_allow_html=True)

# Handle the search button click
if st.button('Search', class_='search-btn'):
    # Search for the movie by title
    movie = ia.search_movie(movie_title)[0]
    ia.update(movie)

    # Display the movie details
    st.markdown('<div class="movie-details"><strong>Title:</strong> ' + movie['title'] + '<br>' +
                '<strong>Year:</strong> ' + str(movie['year']) + '<br>' +
                '<strong>Rating:</strong> ' + str(movie['rating']) + '<br>' +
                '<strong>Genres:</strong> ' + ', '.join(movie['genres']) + '<br>' +
                '<strong>Plot:</strong> ' + (movie['plot'][0] if 'plot' in movie else 'N/A') + '</div>', unsafe_allow_html=True)

    # Display the top 10 cast members
    cast = movie['cast'][:10]
    st.markdown('<div class="cast-list"><strong>Top 10 Cast Members:</strong><br>' +
                '<ul>' + ''.join([f'<li>{member}</li>' for member in cast]) + '</ul></div>', unsafe_allow_html=True)

    # Display recommendations, if available
    if 'recommendations' in movie:
        st.markdown('<div class="recommendations"><strong>Top 5 Recommendations:</strong><br>' +
                    '<ol>' + ''.join([f'<li>{recommendation["title"]} ({recommendation["year"]})</li>'
                                      for recommendation in movie['recommendations'][:5]]) + '</ol></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="recommendations"> </div>', unsafe_allow_html=True)
