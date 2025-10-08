import streamlit as st

def show():
    settings = st.session_state.p_settings

    st.write("--")

    if st.button("CLOSE"):
        st.session_state.is_settings_opened = False
        st.rerun()

    sentence_t = st.slider(
        "Creativity in text generation",
        min_value=0.01,
        max_value=2.0,
        value=settings.sentence_temperature
    )
    checking_t = st.slider(
        "Creativity in text checking",
        min_value=0.01,
        max_value=2.0,
        value=settings.checking_temperature
    )

    if st.button("SAVE"):
        st.session_state.p_settings.sentence_temperature = sentence_t
        st.session_state.p_settings.checking_temperature = checking_t

        st.write(":red[Settings updated!]")