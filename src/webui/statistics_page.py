import json
import streamlit as st
from src.core.get_calendar import html
from src.p_data import STATISTICS_PATH as path

def get():
    data = {
        "ACTIVITY": {},
        "ALL_RATE": {},
        "RATE": {}
    }
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("STATISTICS FILE DOES NOT EXIST!")
    except json.JSONDecodeError:
        print("STATISTICAL FILE DECODING ERROR!")

    st.session_state.calendar_activity = html(data["ACTIVITY"], title="ACTIVITY")
    st.session_state.calendar_rate = html(data["RATE"], title="RATE", is_rate=True)

def show():
    if st.button("BACK"):
        st.session_state.page = "HOME"
        st.rerun()

    html_calendar_activity = st.session_state.calendar_activity
    html_calendar_rate = st.session_state.calendar_rate

    st.markdown(html_calendar_activity, unsafe_allow_html=True)
    st.markdown(html_calendar_rate, unsafe_allow_html=True)