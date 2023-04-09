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


# Define app title and input field
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

                # Display the movie's directors
                directors = ia.get_directors(movie)
                if directors:
                    st.write("**Directors:**")
                    for director in directors:
                        st.write(f"{director['name']} ({director.get('birth date')})")
                        st.image(director.get('headshot'))
                else:
                    st.write("**Directors:** N/A")

                # Display the movie's writers
                writers = ia.get_writers(movie)
                if writers:
                    st.write("**Writers:**")
                    for writer in writers:
                        st.write(f"{writer['name']} ({writer.get('birth date')})")
                        st.image(writer.get('headshot'))
                else:
                    st.write("**Writers:** N/A")

                st.write("**Box Office Gross:**", movie.get('box office'))

                st.write("**Runtime:**", movie.get('runtimes'))

                st.write("**Release Date(s):**")
                for release in movie.get('release dates'):
                    st.write(f"{release['country']} ({release['date']})")

                st.write("**Languages:**")
                for lang in movie.get('languages'):
                    st.write(lang)

                st.write("**Awards:**")
                awards = ia.get_movie_awards(movie.getID())
                if awards:
                    for award_type in awards:
                        st.write(f"{award_type}: {awards[award_type]}")
                else:
                    st.write("N/A")

                st.write("**Top 10 Cast Members:**")
                cast = movie["cast"][:10]
                for member in cast:
                    st.write(f"{member['name']} as {member.currentRole}")

                st.write("**Plot:**")
                if "plot outline" in movie:
                    st.write(movie["plot outline"])
                elif "plot" in movie:
                    st.write(movie["plot"][0])
                else:
                    st.write("N/A")

                st.write("**Soundtrack:**")
                soundtrack = ia.get_movie_soundtrack(movie.getID())
                if soundtrack:
                    for track in soundtrack.get('data'):
                        st.write(f"{track.get('title')} by {track.get('performers')}")
                else:
                    st.write("N/A")
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
