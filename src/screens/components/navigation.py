import streamlit as st


def dashboard_navigation():
    left, middle, right = st.columns(
        [9, 1.5, 3],
        gap="small",
    )

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

    with right:
        if st.button(
            "← Home",
            key="back_to_home",
            type="primary",
            use_container_width=True,
        ):
            st.session_state["login_type"] = None
            st.rerun()