import streamlit as st
from PIL import Image
import numpy as np

from src.screens.components.navigation import dashboard_navigation
from src.screens.ui.base_layout import (
    load_fonts,
    style_base_layout,
    style_background_dashboard,
)


def student_dashboard():
    load_fonts()
    style_base_layout()
    style_background_dashboard()

    dashboard_navigation()
    student_screen()


def student_screen():
    st.title("Student Dashboard", text_alignment="center")
    st.header("Login using FaceID", text_alignment="center")

    photo_source = st.camera_input("Position your face in the center")

    if photo_source:
        image = Image.open(photo_source)
        image_array = np.array(image)
        st.image(image_array, caption="Captured image")