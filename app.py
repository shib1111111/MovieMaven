import streamlit as st

# Set up the Streamlit app
st.set_page_config(
    page_title="MovieMaven",
    page_icon=":movie_camera:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Adding custom CSS
st.markdown(
    """
    <style>
    .stButton button, .stTextInput input {
    background-color: #2c6db8 !important;
    border-color: #2c6db8 !important;
    color: #fff !important;
    }
    .stButton:hover button, .stTextInput:hover input {
    background-color: #2c6db8 !important;
    border-color: #2c6db8 !important;
    color: #fff !important;
    }
    .stButton:active button {
    background-color: #ff4d4d !important;
    border-color: #ff4d4d !important;
    }
    .movie-details {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    height: 100%;
    }
    .movie-details h2 {
    margin-top: 0;
    }
    @media (max-width: 768px) {
    .stImage {
    float: none;
    margin-right: 0;
    margin-bottom: 1rem;
    }
    .movie-details {
    align-items: center;
    }
    }
    .animated-input {
    animation: hue 10s infinite linear;
    color: #007bff !important;
    }
    .animated-button:hover {
    background-color: #007bff !important;
    border-color: #007bff !important;
    }
    @keyframes hue {
    0% {
    filter: hue-rotate(0deg);
    }
    100% {
    filter: hue-rotate(360deg);
    }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Displaying the app title and input field
st.title("MovieMaven")
st.write('Enter a movie title (e.g. "The Godfather")')
movie_title = st.text_input("", "", key="input", css="animated-input")

# Handling the search button click
if st.button("Search", class_="animated-button"):
    with st.spinner("Searching for movie..."):
        # Initialize the IMDb module
        from imdb import IMDb

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
        else:
            st.write(f"No movie found with the title '{movie_title}'")





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
