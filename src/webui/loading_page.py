# Provides a temporary UI while heavy modules and models are loading.
# Without this screen, users would see a frozen or empty interface,
# which may give the impression that the app has crashed.
# The loading page communicates progress and improves UX during startup.
import time
import streamlit as st
from src.core.loading import load_all

def show():
    st.header("LOADING")
    st.write("This may take some time. Please be patient!")
    for log in load_all():
        st.markdown(
            f"""
            <p style="
            background-color:#FFFDD0;
            color:black;
            padding:5px;
            border-radius:5px;
            white-space:pre-line;
            ">{log}
            </p>
            """,
            unsafe_allow_html=True
        )
    time.sleep(1)
    return