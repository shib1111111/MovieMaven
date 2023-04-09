import streamlit as st
from imdb import IMDb
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
        .stButton button, .stTextInput input {{
            background-color: #2c6db8 !important;
            border-color: #2c6db8 !important;
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
    unsafe_allow_html=True,
)


def main():
    st.title("MovieMaven")
    st.write('Enter a movie title (e.g. "The Godfather")')
    movie_title = st.text_input("", "")

    # Handle the search button click
    if st.button("Search"):
        with st.spinner("Searching for movie..."):
            # Initialize the IMDb module
            ia = IMDb()

            # Search for the movie by title
            movies = ia.search_movie(movie_title)
            if len(movies) > 0:
                movie = movies[0]
                ia.update(movie)

                # Display the movie details
                col1, col2 = st.columns([3, 5])
                with col1:
                    st.image(movie["full-size cover url"], use_column_width=True)
                with col2:
                    st.markdown(
                        f"<h2 class='Movie Details'>{movie['title']} ({movie['year']})</h2>",
                        unsafe_allow_html=True,
                    )
                    st.write("**Rating:**", movie["rating"])
                    st.write("**Genres:**", ", ".join(movie["genres"]))
                    if "plot" in movie:
                        st.write("**Plot:**", movie["plot"][0])
                    else:
                        st.write("**Plot:** N/A")

                    # Display the top 10 cast members
                    st.write("**Top 10 Cast Members:**")
                    cast = movie["cast"][:10]
                    for member in cast:
                        st.write(member)

                    # Display recommendations, if available
                    if "recommendations" in movie:
                        st.write("**Top 5 Recommendations:**")
                        for i, recommendation in enumerate(movie["recommendations"][:5]):
                            st.write(
                                f'{i+1}. {recommendation["title"]} ({recommendation["year"]})'
                            )
                    else:
                        st.write("  ")

                # Save movie to favorites
                if st.button("Save to favorites"):
                    # Save the movie object to a file or database
                    st.write(f"{movie['title']} saved to favorites!")

                # View watchlist
                if st.button("View watchlist"):
                    # Retrieve list of saved movies and display them
                    st.write("Your watchlist:")
                    # Iterate over list of saved movies and display them

                # Filter and sort options
                filter_options = ["Sort by rating", "Sort by year", "Filter by genre"]
                filter_choice = st.selectbox("Filter and sort options:", filter_options)
                if filter_choice == "Sort by rating":
                    # Sort movies by rating and display them
                    pass
                elif filter_choice == "Sort by year":
                    # Sort movies by year and display them
                    pass
                elif filter_choice == "Filter by genre":
                    # Filter movies by genre and display them
                    pass

                # Additional movie details
                if st.button("View more details"):
                    # Retrieve additional details about the movie and display them
                    pass

            else:
                st.write(f"No movie found with the title '{movie_title}'")

if __name__ == "__main__":
    main()



# Define a function to display the signature
def display_signature():
    st.markdown(
        """
        <style>
        .signature {
            font-size: 1rem;
            font-style: italic;
            text-align: center;
            padding: 1rem 0;
            color: #333;
            transition: color 0.5s ease-in-out;
        }
        .signature:hover {
            color: #007bff;
        }
        </style>
        """
        , unsafe_allow_html=True
    )
    st.markdown(
        """
        <div class="signature">
        Made with ❤️ by Shib Kumar Saraf
        </div>
        """
        , unsafe_allow_html=True
    )

# Add the signature to your Streamlit app
display_signature()
