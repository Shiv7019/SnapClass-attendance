import streamlit as st
import time

from src.screens.database.db import check_teacher_exists, create_teacher, teacher_login
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

def teacher_dashboard():
    teacher_data = st.session_state.teacher_data

    st.header(f"""Welcome, {teacher_data['none']}""")

def teacher_screen_login():
    teacher_username = st.text_input(
        "Username",
        placeholder="Enter your username",
        key="login_username",
    )
    teacher_password = st.text_input(
        "Password",
        placeholder="Enter your password",
        type="password",
        key="login_password",
    )

    st.divider()

    btnc1, btnc2 = st.columns(2)

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
        if st.button(
            "Login",
            icon=":material/passkey:",
            type="primary",
            key="teacher_login",
            use_container_width=True,
        ):
            if not teacher_username or not teacher_password:
                st.warning("Please enter your username and password.")
            elif teacher_login(teacher_username, teacher_password):
                st.toast("Welcome Back!", icon="✅")
                time.sleep(1)
                # TODO: Navigate to the actual logged-in dashboard here
                st.rerun()
            else:
                st.error("Invalid Details!")

    with btnc2:
        if st.button(
            "Register Instead",
            icon=":material/person_add:",
            type="primary",
            key="teacher_register_switch",
            use_container_width=True,
        ):
            st.session_state["teacher_login_type"] = "register"
            st.rerun()


def register_teacher(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm):
    if not teacher_username or not teacher_name or not teacher_pass:
        return False, "All fields are required."
    if teacher_pass != teacher_pass_confirm:
        return False, "Passwords do not match."
    if check_teacher_exists(teacher_username):
        return False, "Username already taken. Try a different one."
    
    try:
        # Note: Your create_teacher function might require email. If it does, update this line.
        create_teacher(teacher_username, teacher_pass, teacher_name)
        return True, "Successfully created! Login now."
    except Exception as e:
        # This will print the exact database error to your screen so you can see why it failed
        st.error(f"Database Error: {e}") 
        return False, "Unexpected error! See details above."


def teacher_screen_register():
    teacher_username = st.text_input(
        "Username",
        placeholder="Enter your username",
        key="register_username",
    )

    teacher_name = st.text_input(
        "Full Name",
        placeholder="Enter your full name",
        key="register_name",
    )

    teacher_email = st.text_input(
        "Email",
        placeholder="Enter your email address",
        key="register_email",
        type="default",
    )

    teacher_password = st.text_input(
        "Password",
        placeholder="Create a password",
        type="password",
        key="register_password",
    )

    teacher_confirm_password = st.text_input(
        "Confirm Password",
        placeholder="Re-enter your password",
        type="password",
        key="register_confirm_password",
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
            success, message = register_teacher(
                teacher_username,
                teacher_name,
                teacher_password,
                teacher_confirm_password,
            )
            if success:
                # Show a toast notification so you can still see it after the page reloads
                st.toast(message, icon="🎉")
                time.sleep(2)
                st.session_state["teacher_login_type"] = "login"
                st.rerun()
            else:
                st.error(message)