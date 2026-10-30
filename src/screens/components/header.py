import streamlit as st

def header_home():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(
        f"""
        <div style="text-align: center;">
            <img src="{logo_url}" width="100" height="100">
             <h1 style="
                 text-align: center;
                 color: #E0E3FF;
                 margin: 0;
                 font-size: 32px;
                 "
             >
                 SNAPCLASS</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

def header_dashboard():

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(
        f"""
        <div style="display:flex; justify-content:center; align-items:center;">
            <img src="{logo_url}" height="85">
             <h2 style="
                 text-align: center;
                 color: #E865F2;
                 margin: 0;
                 font-size: 32px;
                 "
             >
                 SNAPCLASS</h2>
        </div>
        """,
        unsafe_allow_html=True
    )