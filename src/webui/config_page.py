import streamlit as st

from src.p_data import LANGUAGES, LANGUAGES_LEVELS
from src.p_objects import TextConfig
from src.generation.sentence_template import s as sentence
from src.generation.speech_template import s as speech

def show():
    if st.button("BACK"):
        st.session_state.page = "HOME"
        st.rerun()

    voice = None
    text_type = st.selectbox("Select the text type!", ["sentence"])
    language = st.selectbox("Select a language to improve your listening skills!", LANGUAGES)
    level = st.selectbox("Select your language level!", LANGUAGES_LEVELS[language])
    text_length = st.selectbox("Select the length of the text!", ["short", "medium", "long", "very long"])

    if not st.session_state.is_google_tts:
        voice = st.selectbox("Select a voice from the list!", range(1, 10))

    if st.button("GENERATE"):
        if language != "not selected":
            conf = TextConfig(language, level, text_type, text_length)
            text = sentence(conf)
            audio = speech(text, language, voice)

            return text, audio
        else:
            st.write(":red[Please select a language!]")

    return None, None