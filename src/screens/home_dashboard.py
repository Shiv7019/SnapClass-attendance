# src/screens/home_dashboard.py
import streamlit as st

from src.screens.components.header import header_home
from src.screens.ui.base_layout import (
    load_fonts,
    style_base_layout,
    style_background_home,
)


def home_dashboard():
    # 1. Styles first — before anything renders
    load_fonts()
    style_base_layout()
    style_background_home()

    # 2. Header (now inherits the fonts + background)
    header_home()

    # 3. Page content
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Teacher Login"):
            st.session_state["login_type"] = "teacher"
            st.rerun()
    with col2:
        if st.button("Student Login"):
            st.session_state["login_type"] = "student"
            st.rerun()