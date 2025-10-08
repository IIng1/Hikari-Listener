import streamlit as st
from src.p_objects import ProjectSettings

def init():
    if "page" not in st.session_state:
        st.session_state.page = "HOME"

    if "is_loaded" not in st.session_state:
        st.session_state.is_loaded = False

    if "p_settings" not in st.session_state:
        st.session_state.p_settings = ProjectSettings()

    if "generated_text" not in st.session_state:
        st.session_state.generated_text = None

    if "wav_path" not in st.session_state:
        st.session_state.wav_path = None

    if "is_google_tts" not in st.session_state:
        st.session_state.is_google_tts = False

    if "is_settings_opened" not in st.session_state:
        st.session_state.is_settings_opened = False

    if "calendar_activity" not in st.session_state:
        st.session_state.calendar_activity = {}

    if "calendar_rate" not in st.session_state:
        st.session_state.calendar_rate = {}

    if "input_block" not in st.session_state:
        st.session_state.input_block = True

    if "user_text" not in st.session_state:
        st.session_state.user_text = ""

    if "checked_text" not in st.session_state:
        st.session_state.checked_text = ""

    if "user_text_rate" not in st.session_state:
        st.session_state.user_text_rate = ""
