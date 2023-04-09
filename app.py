import streamlit as st
import imdb

# Initialize the IMDbPY module
imdb_object = imdb.IMDb()

# Define the recommendation function
def recommend_movies(title):
    # Search for the movie
    search_result = imdb_object.search_movie(title)
    
    # Get the ID of the first search result
    movie_id = search_result[0].getID()
    
    # Get the movie object using the ID
    movie = imdb_object.get_movie(movie_id)
    
    # Get the keywords associated with the movie
    keywords = movie.get('keywords')
    
    # Get the recommended movies based on the keywords
    recommended_movies = []
    if keywords is not None:
        for keyword in keywords:
            keyword_movies = imdb_object.get_keyword(keyword)
            keyword_movies = [m for m in keyword_movies if m.getID() != movie_id]
            recommended_movies.extend(keyword_movies)
        
        # Filter the recommended movies to only include those with ratings near the top 250
        recommended_movies = sorted(recommended_movies, key=lambda x: x.get('rating'), reverse=True)
        top_250_rating = sorted([x.get('rating') for x in imdb_object.get_top250_movies()], reverse=True)[249]
        recommended_movies = [x for x in recommended_movies if abs(x.get('rating') - top_250_rating) < 1]
        
        # Limit the recommended movies to 10
        recommended_movies = recommended_movies[:10]
    
    # Display the recommended movies
    if recommended_movies:
        st.write('Top 10 recommended movies:')
        for i, movie in enumerate(recommended_movies):
            st.write(f"{i+1}. {movie.get('title')} ({movie.get('year')}) - Rating: {movie.get('rating')}")
    else:
        st.write('No recommendations found for this movie')
        st.write('Displaying top 10 movies of all time:')
        top_movies = imdb_object.get_top250_movies()
        for i, movie in enumerate(top_movies[:10]):
            st.write(f"{i+1}. {movie.get('title')} ({movie.get('year')}) - Rating: {movie.get('rating')}")

# Create the Streamlit app
st.title('Movie Recommendation App')
title = st.text_input('Enter a movie title')
if title:
    recommend_movies(title)
