
# src/screens/home_dashboard.py
import streamlit as st

from src.screens.components.header import header_home
from src.screens.ui.base_layout import (
    load_fonts,
    style_base_layout,
    style_background_home,
)


def home_dashboard():
    load_fonts()
    style_base_layout()
    style_background_home()

    header_home()

    # Center the two login sections
    left, col1, col2, right = st.columns([0.5, 2, 2, 0.5], gap="medium")

    with col1:
        st.markdown(
            "<h2 style='text-align:center;'>I am a Teacher</h2>",
            unsafe_allow_html=True,
        )

        # Center the image within a fixed-height area
        st.markdown(
            """
            <div style="height:110px; display:flex;
                        justify-content:center; align-items:center;">
                <img src="https://i.ibb.co/CsmQQV6X/mascot-prof.png"
                     style="width:120px; height:100px; object-fit:contain;">
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button("Teacher Login", use_container_width=True, type="secondary"):
            st.session_state["login_type"] = "teacher"
            st.rerun()

    with col2:
        st.markdown(
            "<h2 style='text-align:center;'>I am a Student</h2>",
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div style="height:110px; display:flex;
                        justify-content:center; align-items:center;">
                <img src="https://i.ibb.co/844D9Lrt/mascot-student.png"
                     style="width:120px; height:100px; object-fit:contain;">
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button("Student Login", use_container_width=True, type="secondary"):
            st.session_state["login_type"] = "student"
            st.rerun()
