import streamlit as st
from imdb import IMDb

# Initialize the IMDb module
ia = IMDb()

# Set up the Streamlit app
st.set_page_config(
    page_title="Movie Details",
    page_icon=":clapper:",
    layout="wide",
    initial_sidebar_state="auto",
)
st.write(
    f"""
    <style>
        .sidebar .sidebar-content {{
            background-image: linear-gradient(to bottom, #222633, #313843);
            color: #FFF;
        }}
        .streamlit-expander {{
            background-color: #313843;
        }}
        .streamlit-expanderHeader {{
            color: #FFF;
        }}
        .streamlit-expanderArrow {{
            color: #FFF;
        }}
        .stButton {{
            background-color: #f63366;
            color: #FFF;
            font-weight: bold;
        }}
        .stTextInput > label {{
            color: #FFF;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)
st.title('Movie Details')
col1, col2 = st.beta_columns([2, 3])
with col1:
    st.image('https://cdn.pixabay.com/photo/2017/05/15/17/43/movie-2314449_960_720.png', width=150)
with col2:
    st.write('Enter a movie title (e.g. "The Godfather")')
    movie_title = st.text_input('', '')
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
        cast_list = ""
        for person in movie['cast'][:10]:
            cast_list += f"- {person}\n"
        st.text(cast_list)

        # Display the top 5 recommendations (if available)
        if 'recommendations' in movie:
            st.write('**Top 5 Recommendations:**')
            rec_list = ""
            for i, recommendation in enumerate(movie['recommendations'][:5]):
                rec_list += f"{i+1}. {recommendation['title']} ({recommendation['year']})\n"
            st.text(rec_list)
        else:
            st.write(' ')
