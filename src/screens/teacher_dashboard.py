import streamlit as st
import time

from src.screens.database.db import (
    check_teacher_exists,
    create_teacher,
    teacher_login,
)
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

    if "teacher_login_type" not in st.session_state:
        st.session_state["teacher_login_type"] = "login"

    teacher_data = st.session_state.get("teacher_data")

    if teacher_data:
        teacher_logged_in_view()
        return

    st.title("Teacher Dashboard")

    if st.session_state["teacher_login_type"] == "login":
        teacher_screen_login()
    elif st.session_state["teacher_login_type"] == "register":
        teacher_screen_register()


def teacher_logged_in_view():
    teacher_data = st.session_state["teacher_data"]
    st.header(f"Welcome, {teacher_data['name']}")


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
            else:
                teacher_data = teacher_login(
                    teacher_username, teacher_password
                )

                if teacher_data:
                    teacher_data.pop("password", None)
                    st.session_state["teacher_data"] = teacher_data
                    st.toast("Welcome back!", icon="✅")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("Invalid username or password.")

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


def register_teacher(
    teacher_username,
    teacher_name,
    teacher_pass,
    teacher_pass_confirm,
):
    if not teacher_username or not teacher_name or not teacher_pass:
        return False, "All fields are required."

    if teacher_pass != teacher_pass_confirm:
        return False, "Passwords do not match."

    if check_teacher_exists(teacher_username):
        return False, "Username already taken. Try a different one."

    try:
        create_teacher(teacher_username, teacher_pass, teacher_name)
        return True, "Successfully created! Login now."
    except Exception:
        return False, "Registration failed. Please try again."


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
                st.toast(message, icon="🎉")
                time.sleep(2)
                st.session_state["teacher_login_type"] = "login"
                st.rerun()
            else:
                st.error(message)