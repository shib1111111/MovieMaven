# movie_search.py
import streamlit as st
from imdb import IMDb
from recommendation import generate_movie_recommendations  

def search_movie(movie_title):
    with st.spinner("Searching for movie..."):
        ia = IMDb()
        movies = ia.search_movie(movie_title)

        if len(movies) > 0:
            movie = movies[0]
            ia.update(movie)
            display_movie_details(movie)
        else:
            st.write(f"No movie found with the title '{movie_title}'")

def display_movie_details(movie):
    # Display the movie details
    col1, col2 = st.columns([3, 5])
    with col1:
        st.image(movie["full-size cover url"], use_column_width=True)
    with col2:
        st.markdown(f"<h2 class='Movie Details'>{movie['title']} ({movie['year']})</h2>",unsafe_allow_html=True)
        st.write("**Rating:**", movie["rating"])
        st.write("**Genres:**", ", ".join(movie["genres"]))
        if "plot" in movie:
            st.write("**Plot:**", movie["plot"][0])
        else:
            st.write("**Plot:** N/A")

        # Display the directors
        directors = movie.get('directors')
        if directors:
            directors_str = [director.get('name') for director in directors]
            st.write("**Directors:**", ", ".join(directors_str))
        else:
            st.write("**Directors:** N/A")

        # Display the top 10 cast members

        st.write("**Top 10 Cast Members:**")
        cast = movie["cast"][:10]

        # Create a formatted string with the name and character played for each cast member
        formatted_cast = ""
        for member in cast:
            name = member.get('name')
            character = member.get('character')
            if character:
                formatted_cast += f"{name} as {character}\n"
            else:
                formatted_cast += f"{name}\n"

        # Display the formatted cast list
        st.code(formatted_cast)
        # Display the writers
        writers = movie.get('writers')
        if writers:
            writers_str = [writer.get('name') if writer else '' for writer in writers]
            st.write("**Writers:**", ", ".join(writers_str))
        else:
                st.write("**Writers:** N/A")
        # Generate and display movie recommendations
        recommendations = generate_movie_recommendations(movie["title"])
        st.write("**Movie Recommendations:**")
        st.success(recommendations)
