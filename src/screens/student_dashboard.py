
import streamlit as st

from src.screens.ui.base_layout import (
    load_fonts,
    style_base_layout,
    style_background_dashboard,
)


def student_dashboard():
    load_fonts()
    style_base_layout()
    style_background_dashboard()

    st.title("Student Dashboard")
    st.write("Welcome to the student dashboard!")
