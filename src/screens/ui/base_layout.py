
import streamlit as st


def load_fonts():
    """Load Google Fonts."""
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&family=Outfit:wght@400;500;600;700&display=swap');
        </style>
        """,
        unsafe_allow_html=True,
    )


def style_base_layout():
    """Apply common typography, spacing, and button styles."""
    st.markdown(
        """
        <style>
            /* Main application */
            .stApp {
                font-family: 'Outfit', sans-serif !important;
            }

            /* Hide Streamlit chrome */
            #MainMenu, footer, header {
                visibility: hidden;
            }

            /* Layout spacing */
            .block-container {
                padding-top: 1.5rem !important;
            }

            /* Body typography */
            [data-testid="stMarkdownContainer"],
            [data-testid="stWidgetLabel"],
            [data-testid="stCaptionContainer"] {
                font-family: 'Outfit', sans-serif !important;
            }

            /* Headings */
            h1, h2,
            [data-testid="stHeading"] h1,
            [data-testid="stHeading"] h2 {
                font-family: 'Oswald', sans-serif !important;
            }

            h1 {
                font-size: 3.5rem !important;
                line-height: 1.1 !important;
                margin-bottom: 1rem !important;
            }

            h3, h4, h5, h6 {
                font-family: 'Outfit', sans-serif !important;
            }

            /* Primary buttons */
            button[kind="primary"] {
                background-color: #5865F2 !important;
                color: white !important;
                border-radius: 1.5rem !important;
                padding: 10px 20px !important;
            }

            /* Secondary buttons */
            button[kind="secondary"] {
                background-color: #5B459E !important;
                color: white !important;
                border-radius: 1.5rem !important;
                padding: 10px 20px !important;
            }

            /* Button hover */
            button[kind="primary"]:hover,
            button[kind="secondary"]:hover {
                transform: scale(1.03);
                transition: transform 0.25s ease-in-out;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def style_background_home():
    st.markdown(
        """
        <style>
            .stApp {
                background: #5865F2 !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def style_background_dashboard():
    st.markdown(
        """
        <style>
            .stApp {
                background: #E0E3FF !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def style_background_layout():
    st.markdown(
        """
        <style>
            .stApp {
                background: #5865F2 !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
