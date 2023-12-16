import streamlit as st

def add_custom_css():
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
