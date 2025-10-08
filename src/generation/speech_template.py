import streamlit as st
from src.core.speech_model import inference as local
from src.core.speech_google_tts import inference as google
from src.p_data import LANGUAGES_CODE

def s(text, lang, voice):
    language_code = LANGUAGES_CODE[lang]
    voice_preset = f"{language_code}_speaker_{voice}"

    if not st.session_state.is_google_tts:
        return local(text, voice_preset)
    else:
        return google(text, language_code)