def text_background_css(color, text):
    return f"""
                <p style="
                background-color:{color};
                color:black;
                padding:5px;
                border-radius:5px;
                white-space:pre-line;
                ">{text}
                </p>
                """