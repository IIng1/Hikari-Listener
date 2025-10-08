import src.webui.config_page as config
import src.webui.listening_page as listening
import src.webui.statistics_page as statistics
import src.webui.cuda_absence_notification as cuda
import src.webui.settings_block as settings_block
import streamlit as st
from src.p_data import WARNING_TEXT, RECOMMENDATIONS_FOR_STABILITY, ROADMAP
from src.css_gen.homeNNloading_css import text_background_css

def show():
    page = st.session_state.page

    st.title("Hikari Listener 🌸")

    if page == "HOME":
        st.header("WELCOME! 👋🎉")
        st.write("Improve your listening skills in different languages!")
        cuda.show()
        if st.button("IMPROVE"):
            st.session_state.page = "CONF"
            st.rerun()

    if page == "CONF":
        st.header("CONFIGURATION FOR LISTENING EXAMPLE")
        cuda.show()
        generated_text, wav_path = config.show()
        if generated_text is not None and wav_path is not None:
            st.session_state.page = "LISTENING"
            st.session_state.input_block = True
            st.session_state.generated_text = generated_text
            st.session_state.wav_path = wav_path
            st.rerun()

    if page == "LISTENING":
        st.header("EXAMPLE FOR LISTENING")
        listening.show(
            st.session_state.generated_text,
            st.session_state.wav_path
        )

    if page == "HOME":
        st.write("--")
        st.subheader("You can also view your statistics. But only if you do it locally.")
        if st.button("STATISTICS"):
            statistics.get()
            st.session_state.page = "STATISTICS"
            st.rerun()

    if page == "STATISTICS":
        st.header("YOUR STATISTICS FOR THE LAST THREE MONTHS")
        st.write("--")
        statistics.show()
        st.write("--")

    st.markdown(
        text_background_css(
            color="lightcoral",
            text=WARNING_TEXT
        ),
        unsafe_allow_html=True
    )

    st.markdown(
        text_background_css(
            color="lightcoral",
            text=RECOMMENDATIONS_FOR_STABILITY
        ),
        unsafe_allow_html=True
    )
    if st.session_state.is_settings_opened:
        settings_block.show()
    else:
        if st.button("SETTINGS"):
            st.session_state.is_settings_opened = True
            st.rerun()

    if page == "HOME":
        st.write("--")
        st.header("ROADMAP")
        st.subheader("DONE:")
        for c in ROADMAP["done"]:
            st.markdown(
                text_background_css(color="#FFFDD0", text=f" • {c}"),
                unsafe_allow_html=True
            )

        st.subheader("TO DO:")
        for c in ROADMAP["todo"]:
            st.markdown(
                text_background_css(color="#FFFDD0", text=f" • {c}"),
                unsafe_allow_html=True
            )