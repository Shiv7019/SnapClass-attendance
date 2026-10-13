
import streamlit as st

from src.screens.ui.base_layout import (
    load_fonts,
    style_base_layout,
    style_background_dashboard,
)


def teacher_dashboard():
    load_fonts()
    style_base_layout()
    style_background_dashboard()

    st.title("Teacher Dashboard")
    st.write("Welcome to the teacher dashboard!")
