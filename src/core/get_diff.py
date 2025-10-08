import difflib

def html(user_text, checked_text):
    diff = difflib.ndiff(user_text, checked_text)
    html_diff = ""
    for d in diff:
        if d.startswith(" "):
            html_diff += d[-1]
        elif d.startswith("-"):
            html_diff += f"<span style='background-color:#f88'>{d[-1]}</span>"
        elif d.startswith("+"):
            html_diff += f"<span style='background-color:#8f8'>{d[-1]}</span>"

    return html_diff