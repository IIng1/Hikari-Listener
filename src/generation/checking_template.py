import streamlit as st
from src.p_data import SYSTEM_PROMPT
from src.core.text_model import inference
from src.core.text_tokenize import tokenizer

def s(original_text, user_text):
    settings = st.session_state.p_settings

    request = f"[{{'task': 'check_translation'}}, {{'ORIGINAL': '{original_text}'}}, {{'USER': '{user_text}'}}]"
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT[1]},
        {"role": "user", "content": request}
    ]
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    return inference(
        LoRA_id=1,
        temperature=settings.checking_temperature,
        text=text
    )