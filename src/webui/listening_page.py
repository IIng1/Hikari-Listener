import streamlit as st
import src.webui.statistics_page as statistics
from ast import literal_eval
from src.generation.checking_template import s
from src.core.get_diff import html
from src.core.statistics_saving import save
from src.p_data import RATE

def show(text, wav_path):
    if st.button("BACK"):
        st.session_state.page = "HOME"
        st.rerun()

    audio_file = open(wav_path, "rb")
    audio_bytes = audio_file.read()

    st.audio(
        audio_bytes,
        format="audio/wav",
    )
    if st.session_state.input_block:
        user_text = st.text_input("Please write what you heard!")
        st.session_state.user_text = user_text
        if st.button("CHECK!"):
            # Handles cases where the model returns malformed JSON.
            # The system retries inference until a valid structure is produced.
            # Long-term solution: improve the dataset and fine-tuning for more stable outputs.
            while True:
                try:
                    output = s(text, user_text)
                    output = literal_eval(output)

                    st.session_state.checked_text = output[0]["FIXED"]
                    st.session_state.user_text_rate = int(output[1]["RATE"])

                    break
                except (ValueError, SyntaxError) as e:
                    print(f"'{output}' is an incorrect output format!")
                    print(e)
                except KeyError as e:
                    print(f"'{output}' is an incorrect output format!")
                    print(e)

            save(st.session_state.user_text_rate)
            st.session_state.input_block = False
            st.rerun()
    else:
        user_text = st.session_state.user_text
        checked_text = st.session_state.checked_text
        user_text_rate = st.session_state.user_text_rate

        html_diff = html(user_text, checked_text)
        user_text_rate = RATE[user_text_rate]

        st.markdown(html_diff, unsafe_allow_html=True)
        st.subheader(user_text_rate)

        col_next, col_statistics = st.columns([0.1, 1])

        with col_next:
            if st.button("NEXT"):
                st.session_state.page = "CONF"
                st.rerun()
        with col_statistics:
            if st.button("STATISTICS"):
                statistics.get()
                st.session_state.page = "STATISTICS"
                st.rerun()