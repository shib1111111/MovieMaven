import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import streamlit as st
from imdb import IMDb

# Initialize IMDbPY library
ia = IMDb()

# Create a Streamlit app
st.title('Movie Recommender System')

# Ask user for their favorite movie
user_movie = st.text_input('Enter your favorite movie:')

# Search for the movie on IMDb
try:
    search_results = ia.search_movie(user_movie)
    movie_id = search_results[0].getID()
    movie = ia.get_movie(movie_id)
except:
    st.write('Movie not found. Please try again.')
    movie_id = None

if movie_id is not None:
    # Get the movie details and ratings
    title = movie.get('title')
    year = movie.get('year')
    genres = ','.join(movie.get('genres'))
    rating = movie.get('rating')
    
    # Create a dataframe with the movie data
    movie_df = pd.DataFrame({'movieId': [movie_id], 'title': [title], 'year': [year], 'genres': [genres], 'rating': [rating]})
    
    # Save the movie dataframe to CSV
    movie_df.to_csv('movies.csv', index=False)
    
    # Get the movie ratings
    ratings = movie.get('votes')
    
    # Create a dataframe with the movie ratings
    ratings_df = pd.DataFrame({'movieId': [movie_id], 'userId': ['imdb'], 'rating': [ratings], 'timestamp': [None]})
    
    # Save the ratings dataframe to CSV
    ratings_df.to_csv('ratings.csv', index=False)
    
    # Load the dataset
    movies = pd.read_csv('movies.csv')
    ratings = pd.read_csv('ratings.csv')
    
    # Merge the movies and ratings dataframes
    df = pd.merge(movies, ratings, on='movieId')
    df = df.drop(['timestamp'], axis=1)
    
    # Pivot the data to create a user-item matrix
    matrix = df.pivot_table(index='userId', columns='title', values='rating')
    matrix = matrix.fillna(0)
    
    # Convert the user-item matrix to a sparse matrix
    sparse_matrix = csr_matrix(matrix)
    
    # Train the nearest neighbors algorithm on the sparse matrix
    model = NearestNeighbors(metric='cosine', algorithm='brute')
    model.fit(sparse_matrix)
    
    # Recommend similar movies
    distances, indices = model.kneighbors(sparse_matrix[movies[movies['title'] == title].index[0]], n_neighbors=11)
    recommended_movies = []
    for i in range(1, len(distances.flatten())):
        recommended_movies.append(movies['title'][indices.flatten()[i]])
    
    # Display recommended movies
    st.write('Recommended movies:')
    for movie in recommended_movies:
        st.write('- ' + movie)
