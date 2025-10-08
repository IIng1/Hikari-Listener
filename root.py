# Entry point responsible for switching from the loading page to the main UI.
import streamlit as st
from src.core.session_state_init import init as ss_init

ss_init()

st.set_page_config(layout="centered")
st.markdown("""
    <style>
    .block-container {
        max-width: 900px;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

if not st.session_state.is_loaded:
    from src.webui.loading_page import show as loading
    loading()
    st.session_state.is_loaded = True
    st.rerun()
else:
    from src.webui.home_page import show as home
    home()