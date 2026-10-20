import streamlit as st

from src.screens.components.header import header_dashboard
from src.screens.components.navigation import dashboard_navigation
from src.screens.ui.base_layout import (
    load_fonts,
    style_base_layout,
    style_background_dashboard,
)



def teacher_dashboard():
    load_fonts()
    style_base_layout()
    style_background_dashboard()
    dashboard_navigation()

    # Initialize session state
    if "teacher_login_type" not in st.session_state:
        st.session_state["teacher_login_type"] = "login"

    st.title("Teacher Dashboard")

    if st.session_state["teacher_login_type"] == "login":
        teacher_screen_login()

    elif st.session_state["teacher_login_type"] == "register":
        teacher_screen_register()


def teacher_screen_login():
   
    teacher_username = st.text_input("Username", placeholder="Enter your username")
    teacher_password = st.text_input("Password", placeholder="Enter your password", type="password")

    st.divider()

    btnc1, bntc2 = st.columns(2)
    st.markdown("""
    <style>
    /* Remove red border from buttons */
    .stButton > button {
        border: none !important;
        outline: none !important;
        box-shadow: none !important;
    }

    div.stButton > button[kind="primary"] p {
        color: #FFFFFF !important;
    }

    </style>
    """, unsafe_allow_html=True)
        
    with btnc1:
        st.button(
            "Login",
            icon=":material/passkey:",
            type="primary",
            key="teacher_login",
            use_container_width=True,
        )

    with bntc2:
         if st.button(
                "Resgister Instead",
                icon=":material/passkey:",
                type="primary",
                key="teacher_register",
                use_container_width=True
            ):
             st.session_state.teacher_login_type = 'register'



def teacher_screen_register():
    teacher_username = st.text_input(
        "Username",
        placeholder="Enter your username",
        key="register_username"
    )

    teacher_email = st.text_input(
        "Email",
        placeholder="Enter your email address",
        key="register_email",
        type="default"
    )

    teacher_password = st.text_input(
        "Password",
        placeholder="Create a password",
        type="password",
        key="register_password"
    )

    teacher_confirm_password = st.text_input(
        "Confirm Password",
        placeholder="Re-enter your password",
        type="password",
        key="register_confirm_password"
    )

    st.divider()

    btnc1, btnc2 = st.columns(2)

    with btnc1:
        if st.button(
            "Login Instead",
            icon=":material/login:",
            type="primary",
            key="register_login_button",
            use_container_width=True,
        ):
            st.session_state["teacher_login_type"] = "login"
            st.rerun()

    with btnc2:
        if st.button(
            "Register",
            icon=":material/person_add:",
            type="primary",
            key="teacher_register_submit",
            use_container_width=True,
        ):
            if not teacher_username or not teacher_email or not teacher_password:
                st.warning("Please fill in all fields.")

            elif teacher_password != teacher_confirm_password:
                st.error("Passwords do not match.")

            else:
                st.success("Form validated! Account creation is not connected yet.")
