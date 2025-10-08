import streamlit as st
from torch import cuda
from src.css_gen.homeNNloading_css import text_background_css

def show():
    if not cuda.is_available() and not st.session_state.is_google_tts:
        col_text, col_button = st.columns([1.4, 1])
        with col_text:
            st.markdown(
                text_background_css(
                    color="lightcoral",
                    text=" THIS PROGRAM RUNS ON DEVICES WITHOUT CUDA. IT MAY BE SLOW."
                ),
                unsafe_allow_html=True
            )
        with col_button:
            if st.button("Use Google TTS"):
                st.session_state.is_google_tts = True
                st.rerun()